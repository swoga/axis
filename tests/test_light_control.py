"""Test Axis Light Control API.

pytest --cov-report term-missing --cov=axis.light_control tests/test_light_control.py
"""

import pytest

from asynctest import Mock

from axis.light_control import LightControl


@pytest.fixture
def light_control() -> LightControl:
    """Returns the light_control mock object."""
    mock_request = Mock()
    mock_request.return_value = ""
    return LightControl({}, mock_request)


def test_get_supported_versions(light_control):
    """Test get supported versions api."""
    light_control._request.return_value = response_getSupportedVersions
    response = light_control.get_supported_versions()
    light_control._request.assert_called_with(
        "post", "/axis-cgi/lightcontrol.cgi", json={"method": "getSupportedVersions"},
    )

    assert response["data"] == {"apiVersions": ["1.1"]}


response_getSupportedVersions = {
    "method": "getSupportedVersions",
    "data": {"apiVersions": ["1.1"]},
}
