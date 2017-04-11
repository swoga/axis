from .stream import MetaDataStream

import logging
import requests
from requests.auth import HTTPDigestAuth # , HTTPBasicAuth
import re

_LOGGER = logging.getLogger(__name__)

MESSAGE = re.compile('(?<=PropertyOperation)="(?P<operation>\w+)"')
TOPIC = re.compile('(?<=<wsnt:Topic).*>(?P<topic>.*)(?=<\/wsnt:Topic>)')
SOURCE = re.compile('(?<=<tt:Source>).*Name="(?P<name>\w+)"' +
                    '.*Value="(?P<value>\w+)".*(?=<\/tt:Source>)')
DATA = re.compile('(?<=<tt:Data>).*Name="(?P<name>\w*)"' +
                  '.*Value="(?P<value>\w*)".*(?=<\/tt:Data>)')
PARAM_URL = 'http://{0}/axis-cgi/{1}?action=list&group={2}'

# Externt pypi paket
class AxisDevice(object):
    """Creates a new Axis device."""

    def __init__(self, config):
        """Initialize device."""

        _LOGGER.debug("Initializing new Axis device at: %s", config['host'])

        # Device configuration
        self._alias = config['alias']  # Used as unique identifier internally
        self._name = config['name']
        self._url = config['host']
        self._username = config['username']
        self._password = config['password']
        self._location = config['location']
        self._config = config

        # Metadatastream
        self._metadatastream = None  # Instance of metadatastream
        self._event_topics = None  # Topics to subscribe on metadatastream
        self.initialize_new_event = None  # Metadata initialize callback
        self.events = {}  # Active device events

        # Device data needs to be aqcuired manually
        self._version = self.get_param('Properties.Firmware.Version')
        self._model = self.get_param('Brand.ProdNbr')
        self._serial_number = self.get_param('Properties.System.SerialNumber')

        # Unsupported configuration
        self._video = 0  # No support for this yet
        self._audio = 0  # No support for this yet

        print(self._name, self._url, self._username, self._password)

    def get_param(self, param):
        """Get parameter and remove descriptive part of response"""
        cgi = 'param.cgi'
        r = self.do_request(cgi, param)
        return r[param]

    def do_request(self, cgi, param):
        """Do HTTP request and return response as dictionary"""
        url = PARAM_URL.format(self._url, cgi, param)
        auth = HTTPDigestAuth(self._username, self._password)
        r = requests.get(url, auth=auth)
        v = {}
        for s in filter(None, r.text.split('\n')):
            key, value = s.split('=')
            v[key] = value
        return v

    @property
    def metadata_url(self):
        """Set up url for metadatastream"""
        rtsp = "rtsp://{0}:{1}@{2}/axis-media/media.amp?".format(
            self._username, self._password, self._url)
        source = 'video={0}&audio={1}&even=on&eventtopic={2}'.format(
            self._video, self._audio, self._event_topics)
        return rtsp + source

    @property
    def name(self):
        """Device name"""
        return self._name

    def add_event_topic(self, event_topic):
        """Add new event topic to subscribe to on metadatastream"""
        if self._event_topics is None:
            self._event_topics = event_topic
        else:
            self._event_topics = '{}|{}'.format(self._event_topics,
                                                event_topic)

    def initiate_metadatastream(self):
        """Set up gstreamer pipeline and data callback for metadatastream """
        self._metadatastream = MetaDataStream(self.metadata_url)
        self._metadatastream.signal_parent = self.new_metadata
        self._metadatastream.start()

    def start_metadatastream(self):
        """Start metadatastream."""
        self._metadatastream.start()

    def stop_metadatastream(self):
        """Stop metadatastream."""
        self._metadatastream.stop()

    def parse_metadata(self, metadata):
        """Parse metadata xml."""
        output = {}

        message = MESSAGE.search(metadata)
        if message:
            output['Operation'] = message.group('operation')

        topic = TOPIC.search(metadata)
        if topic:
            output['Topic'] = topic.group('topic')

        source = SOURCE.search(metadata)
        if source:
            output['Source_name'] = source.group('name')
            output['Source_value'] = source.group('value')

        data = DATA.search(metadata)
        if data:
            output['Data_name'] = data.group('name')
            output['Data_value'] = data.group('value')

        print(output)
        return output

    def new_metadata(self):
        """Received new metadata."""
        metadata = self._metadatastream.data
        data = self.parse_metadata(metadata)
        if 'Operation' not in data:
            return False

        elif data['Operation'] == 'Initialized':
            new_event = AxisEvent(data, self)
            if new_event.name not in self.events:
                self.events[new_event.name] = new_event
                self.initialize_new_event(new_event)
                # self.initialize_new_event(self._alias, new_event.name)

        elif data['Operation'] == 'Changed':
            event_name = '{}_{}'.format(data['Topic'], data['Source_value'])
            self.events[event_name].state = data['Data_value']

        elif data['Operation'] == 'Deleted':
            print("Deleted event from stream")
            # keep a list of deleted events and a follow up timer of X,
            # then clean up. This should also take care of rebooting a camera

        else:
            print("Unexpected response: {}".format(data))


class AxisEvent(object):  # pylint: disable=R0904
    """Class to represent each Axis device event."""

    def __init__(self, data, device):
        """Setup an Axis event."""
        print("New AxisEvent {}".format(data))
        self._device = device
        self._topic = data['Topic']
        self._id = data['Source_value']
        self._type = data['Data_name']
        self._source = data['Source_name']

        self._state = None
        self.callback = None

    @property
    def device_name(self):
        """Return device name that the event belongs to."""
        return self._device.name

    @property
    def topic(self):
        """The Topic which the event belongs to."""
        return self._topic

    @property
    def id(self):
        """Source ID for the event."""
        return self._id

    @property
    def type(self):
        """The Type of event."""
        return self._type

    @property
    def source(self):
        """The Source of the event."""
        return self._source

    @property
    def name(self):
        """Uniquely identifying name for the event within the device."""
        return '{}_{}'.format(self._topic, self._id)

    @property
    def state(self):
        """The State of the event."""
        return self._state

    @state.setter
    def state(self, state):
        """Update state of event and trigger callback for notification."""
        self._state = state
        if self.callback:
            self.callback()
        else:
            print("state.setter has no callback")

    @property
    def location(self):
        """Where the device is placed."""
        return self._device._location

    @property
    def is_tripped(self):
        """Event is tripped now."""
        return self._state == '1'
