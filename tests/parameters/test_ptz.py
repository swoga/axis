"""Test AXIS PTZ parameter management."""

import pytest

from axis.device import AxisDevice
from axis.vapix.interfaces.parameters.ptz import PtzParameterHandler

PTZ_RESPONSE = """root.PTZ.BoaProtPTZOperator=password
root.PTZ.CameraDefault=1
root.PTZ.NbrOfCameras=1
root.PTZ.NbrOfSerPorts=1
root.PTZ.CamPorts.Cam1Port=1
root.PTZ.ImageSource.I0.PTZEnabled=true
root.PTZ.Limit.L1.MaxBrightness=9999
root.PTZ.Limit.L1.MaxFieldAngle=623
root.PTZ.Limit.L1.MaxFocus=9999
root.PTZ.Limit.L1.MaxIris=9999
root.PTZ.Limit.L1.MaxPan=170
root.PTZ.Limit.L1.MaxTilt=90
root.PTZ.Limit.L1.MaxZoom=9999
root.PTZ.Limit.L1.MinBrightness=1
root.PTZ.Limit.L1.MinFieldAngle=22
root.PTZ.Limit.L1.MinFocus=770
root.PTZ.Limit.L1.MinIris=1
root.PTZ.Limit.L1.MinPan=-170
root.PTZ.Limit.L1.MinTilt=-20
root.PTZ.Limit.L1.MinZoom=1
root.PTZ.Preset.P0.HomePosition=1
root.PTZ.Preset.P0.ImageSource=0
root.PTZ.Preset.P0.Name=
root.PTZ.Preset.P0.Position.P1.Data=tilt=0.000000:focus=32766.000000:pan=0.000000:iris=32766.000000:zoom=1.000000
root.PTZ.Preset.P0.Position.P1.Name=Home
root.PTZ.PTZDriverStatuses.Driver1Status=3
root.PTZ.SerDriverStatuses.Ser1Status=3
root.PTZ.Support.S1.AbsoluteBrightness=true
root.PTZ.Support.S1.AbsoluteFocus=true
root.PTZ.Support.S1.AbsoluteIris=true
root.PTZ.Support.S1.AbsolutePan=true
root.PTZ.Support.S1.AbsoluteTilt=true
root.PTZ.Support.S1.AbsoluteZoom=true
root.PTZ.Support.S1.ActionNotification=true
root.PTZ.Support.S1.AreaZoom=true
root.PTZ.Support.S1.AutoFocus=true
root.PTZ.Support.S1.AutoIrCutFilter=true
root.PTZ.Support.S1.AutoIris=true
root.PTZ.Support.S1.Auxiliary=true
root.PTZ.Support.S1.BackLight=true
root.PTZ.Support.S1.ContinuousBrightness=false
root.PTZ.Support.S1.ContinuousFocus=true
root.PTZ.Support.S1.ContinuousIris=false
root.PTZ.Support.S1.ContinuousPan=true
root.PTZ.Support.S1.ContinuousTilt=true
root.PTZ.Support.S1.ContinuousZoom=true
root.PTZ.Support.S1.DevicePreset=false
root.PTZ.Support.S1.DigitalZoom=true
root.PTZ.Support.S1.GenericHTTP=false
root.PTZ.Support.S1.IrCutFilter=true
root.PTZ.Support.S1.JoyStickEmulation=true
root.PTZ.Support.S1.LensOffset=false
root.PTZ.Support.S1.OSDMenu=false
root.PTZ.Support.S1.ProportionalSpeed=true
root.PTZ.Support.S1.RelativeBrightness=true
root.PTZ.Support.S1.RelativeFocus=true
root.PTZ.Support.S1.RelativeIris=true
root.PTZ.Support.S1.RelativePan=true
root.PTZ.Support.S1.RelativeTilt=true
root.PTZ.Support.S1.RelativeZoom=true
root.PTZ.Support.S1.ServerPreset=true
root.PTZ.Support.S1.SpeedCtl=true
root.PTZ.UserAdv.U1.AdjustableZoomSpeedEnabled=true
root.PTZ.UserAdv.U1.DeviceModVer=model:0467, version:0310
root.PTZ.UserAdv.U1.DeviceStatus=cam=ok,pan=ok,tilt=ok
root.PTZ.UserAdv.U1.LastTestDate=Thu Oct 29 08:12:04 2020
root.PTZ.UserAdv.U1.MoveSpeed=100
root.PTZ.UserAdv.U1.WhiteBalanceOnePushModeEnabled=true
root.PTZ.UserCtlQueue.U0.Priority=10
root.PTZ.UserCtlQueue.U0.TimeoutTime=60
root.PTZ.UserCtlQueue.U0.TimeoutType=activity
root.PTZ.UserCtlQueue.U0.UseCookie=yes
root.PTZ.UserCtlQueue.U0.UserGroup=Administrator
root.PTZ.UserCtlQueue.U1.Priority=30
root.PTZ.UserCtlQueue.U1.TimeoutTime=60
root.PTZ.UserCtlQueue.U1.TimeoutType=activity
root.PTZ.UserCtlQueue.U1.UseCookie=yes
root.PTZ.UserCtlQueue.U1.UserGroup=Operator
root.PTZ.UserCtlQueue.U2.Priority=50
root.PTZ.UserCtlQueue.U2.TimeoutTime=60
root.PTZ.UserCtlQueue.U2.TimeoutType=timespan
root.PTZ.UserCtlQueue.U2.UseCookie=yes
root.PTZ.UserCtlQueue.U2.UserGroup=Viewer
root.PTZ.UserCtlQueue.U3.Priority=20
root.PTZ.UserCtlQueue.U3.TimeoutTime=20
root.PTZ.UserCtlQueue.U3.TimeoutType=activity
root.PTZ.UserCtlQueue.U3.UseCookie=no
root.PTZ.UserCtlQueue.U3.UserGroup=Event
root.PTZ.UserCtlQueue.U4.Priority=35
root.PTZ.UserCtlQueue.U4.TimeoutTime=60
root.PTZ.UserCtlQueue.U4.TimeoutType=infinity
root.PTZ.UserCtlQueue.U4.UseCookie=no
root.PTZ.UserCtlQueue.U4.UserGroup=Autotracking
root.PTZ.UserCtlQueue.U5.Priority=0
root.PTZ.UserCtlQueue.U5.TimeoutTime=60
root.PTZ.UserCtlQueue.U5.TimeoutType=infinity
root.PTZ.UserCtlQueue.U5.UseCookie=no
root.PTZ.UserCtlQueue.U5.UserGroup=Onvif
root.PTZ.Various.V1.AutoFocus=true
root.PTZ.Various.V1.AutoIris=true
root.PTZ.Various.V1.BackLight=false
root.PTZ.Various.V1.BackLightEnabled=true
root.PTZ.Various.V1.BrightnessEnabled=true
root.PTZ.Various.V1.CtlQueueing=false
root.PTZ.Various.V1.CtlQueueLimit=20
root.PTZ.Various.V1.CtlQueuePollTime=20
root.PTZ.Various.V1.FocusEnabled=true
root.PTZ.Various.V1.HomePresetSet=true
root.PTZ.Various.V1.IrCutFilter=auto
root.PTZ.Various.V1.IrCutFilterEnabled=true
root.PTZ.Various.V1.IrisEnabled=true
root.PTZ.Various.V1.MaxProportionalSpeed=200
root.PTZ.Various.V1.PanEnabled=true
root.PTZ.Various.V1.ProportionalSpeedEnabled=true
root.PTZ.Various.V1.PTZCounter=8
root.PTZ.Various.V1.ReturnToOverview=0
root.PTZ.Various.V1.SpeedCtlEnabled=true
root.PTZ.Various.V1.TiltEnabled=true
root.PTZ.Various.V1.ZoomEnabled=true"""


PTZ_5_51_M1054_RESPONSE = """root.PTZ.NbrOfSerPorts=0
root.PTZ.NbrOfCameras=1
root.PTZ.CameraDefault=1
root.PTZ.BoaProtPTZOperator=password
root.PTZ.CamPorts.Cam1Port=1
root.PTZ.ImageSource.I0.PTZEnabled=false
root.PTZ.Limit.L1.MinPan=-180
root.PTZ.Limit.L1.MaxPan=180
root.PTZ.Limit.L1.MinTilt=-180
root.PTZ.Limit.L1.MaxTilt=180
root.PTZ.Limit.L1.MinZoom=1
root.PTZ.Limit.L1.MaxZoom=9999
root.PTZ.Preset.P0.Name=
root.PTZ.Preset.P0.ImageSource=0
root.PTZ.Preset.P0.HomePosition=1
root.PTZ.Preset.P0.Position.P1.Name=Home
root.PTZ.Preset.P0.Position.P1.Data=tilt=0.000000:pan=0.000000:zoom=1.000000
root.PTZ.PTZDriverStatuses.Driver1Status=3
root.PTZ.Support.S1.AbsolutePan=true
root.PTZ.Support.S1.RelativePan=true
root.PTZ.Support.S1.AbsoluteTilt=true
root.PTZ.Support.S1.RelativeTilt=true
root.PTZ.Support.S1.AbsoluteZoom=true
root.PTZ.Support.S1.RelativeZoom=true
root.PTZ.Support.S1.DigitalZoom=false
root.PTZ.Support.S1.AbsoluteFocus=false
root.PTZ.Support.S1.RelativeFocus=false
root.PTZ.Support.S1.AutoFocus=false
root.PTZ.Support.S1.AbsoluteIris=false
root.PTZ.Support.S1.RelativeIris=false
root.PTZ.Support.S1.AutoIris=false
root.PTZ.Support.S1.AbsoluteBrightness=false
root.PTZ.Support.S1.RelativeBrightness=false
root.PTZ.Support.S1.ContinuousPan=true
root.PTZ.Support.S1.ContinuousTilt=true
root.PTZ.Support.S1.ContinuousZoom=true
root.PTZ.Support.S1.ContinuousFocus=false
root.PTZ.Support.S1.ContinuousIris=false
root.PTZ.Support.S1.ContinuousBrightness=false
root.PTZ.Support.S1.Auxiliary=false
root.PTZ.Support.S1.ServerPreset=true
root.PTZ.Support.S1.DevicePreset=false
root.PTZ.Support.S1.SpeedCtl=true
root.PTZ.Support.S1.JoyStickEmulation=true
root.PTZ.Support.S1.IrCutFilter=false
root.PTZ.Support.S1.AutoIrCutFilter=false
root.PTZ.Support.S1.BackLight=false
root.PTZ.Support.S1.OSDMenu=false
root.PTZ.Support.S1.ActionNotification=true
root.PTZ.Support.S1.ProportionalSpeed=true
root.PTZ.Support.S1.GenericHTTP=false
root.PTZ.Support.S1.LensOffset=false
root.PTZ.Support.S1.AreaZoom=true
root.PTZ.UserAdv.U1.MoveSpeed=100
root.PTZ.UserCtlQueue.U0.UserGroup=Administrator
root.PTZ.UserCtlQueue.U0.UseCookie=yes
root.PTZ.UserCtlQueue.U0.Priority=10
root.PTZ.UserCtlQueue.U0.TimeoutType=activity
root.PTZ.UserCtlQueue.U0.TimeoutTime=60
root.PTZ.UserCtlQueue.U1.UserGroup=Operator
root.PTZ.UserCtlQueue.U1.UseCookie=yes
root.PTZ.UserCtlQueue.U1.Priority=30
root.PTZ.UserCtlQueue.U1.TimeoutType=activity
root.PTZ.UserCtlQueue.U1.TimeoutTime=60
root.PTZ.UserCtlQueue.U2.UserGroup=Viewer
root.PTZ.UserCtlQueue.U2.UseCookie=yes
root.PTZ.UserCtlQueue.U2.Priority=50
root.PTZ.UserCtlQueue.U2.TimeoutType=timespan
root.PTZ.UserCtlQueue.U2.TimeoutTime=60
root.PTZ.UserCtlQueue.U3.UserGroup=Event
root.PTZ.UserCtlQueue.U3.UseCookie=no
root.PTZ.UserCtlQueue.U3.Priority=20
root.PTZ.UserCtlQueue.U3.TimeoutType=activity
root.PTZ.UserCtlQueue.U3.TimeoutTime=20
root.PTZ.UserCtlQueue.U4.UserGroup=Guardtour
root.PTZ.UserCtlQueue.U4.UseCookie=no
root.PTZ.UserCtlQueue.U4.Priority=40
root.PTZ.UserCtlQueue.U4.TimeoutType=infinity
root.PTZ.UserCtlQueue.U4.TimeoutTime=60
root.PTZ.UserCtlQueue.U5.UserGroup=Autotracking
root.PTZ.UserCtlQueue.U5.UseCookie=no
root.PTZ.UserCtlQueue.U5.Priority=35
root.PTZ.UserCtlQueue.U5.TimeoutType=infinity
root.PTZ.UserCtlQueue.U5.TimeoutTime=60
root.PTZ.UserCtlQueue.U6.UserGroup=Onvif
root.PTZ.UserCtlQueue.U6.UseCookie=no
root.PTZ.UserCtlQueue.U6.Priority=1
root.PTZ.UserCtlQueue.U6.TimeoutType=infinity
root.PTZ.UserCtlQueue.U6.TimeoutTime=60
root.PTZ.Various.V1.CtlQueueing=false
root.PTZ.Various.V1.CtlQueueLimit=20
root.PTZ.Various.V1.CtlQueuePollTime=20
root.PTZ.Various.V1.PanEnabled=true
root.PTZ.Various.V1.TiltEnabled=true
root.PTZ.Various.V1.ZoomEnabled=true
root.PTZ.Various.V1.SpeedCtlEnabled=true
root.PTZ.Various.V1.HomePresetSet=true
root.PTZ.Various.V1.ProportionalSpeedEnabled=true
root.PTZ.Various.V1.MaxProportionalSpeed=200
root.PTZ.Various.V1.ReturnToOverview=30
root.PTZ.Various.V1.Locked=true
"""

PTZ_5_51_M3024_RESPONSE = """root.PTZ.NbrOfSerPorts=0
root.PTZ.CameraDefault=1
root.PTZ.BoaProtPTZOperator=password
root.PTZ.CamPorts.Cam1Port=1
root.PTZ.ImageSource.I0.PTZEnabled=false
root.PTZ.Limit.L1.MinPan=-180
root.PTZ.Limit.L1.MaxPan=180
root.PTZ.Limit.L1.MinTilt=-180
root.PTZ.Limit.L1.MaxTilt=180
root.PTZ.Limit.L1.MinZoom=1
root.PTZ.Limit.L1.MaxZoom=9999
root.PTZ.Preset.P0.Name=
root.PTZ.Preset.P0.ImageSource=0
root.PTZ.Preset.P0.HomePosition=1
root.PTZ.Preset.P0.Position.P1.Name=Home
root.PTZ.Preset.P0.Position.P1.Data=tilt=0.000000:pan=0.000000:zoom=1.000000
root.PTZ.PTZDriverStatuses.Driver1Status=3
root.PTZ.Support.S1.AbsolutePan=true
root.PTZ.Support.S1.RelativePan=true
root.PTZ.Support.S1.AbsoluteTilt=true
root.PTZ.Support.S1.RelativeTilt=true
root.PTZ.Support.S1.AbsoluteZoom=true
root.PTZ.Support.S1.RelativeZoom=true
root.PTZ.Support.S1.DigitalZoom=false
root.PTZ.Support.S1.AbsoluteFocus=false
root.PTZ.Support.S1.RelativeFocus=false
root.PTZ.Support.S1.AutoFocus=false
root.PTZ.Support.S1.AbsoluteIris=false
root.PTZ.Support.S1.RelativeIris=false
root.PTZ.Support.S1.AutoIris=false
root.PTZ.Support.S1.AbsoluteBrightness=false
root.PTZ.Support.S1.RelativeBrightness=false
root.PTZ.Support.S1.ContinuousPan=true
root.PTZ.Support.S1.ContinuousTilt=true
root.PTZ.Support.S1.ContinuousZoom=true
root.PTZ.Support.S1.ContinuousFocus=false
root.PTZ.Support.S1.ContinuousIris=false
root.PTZ.Support.S1.ContinuousBrightness=false
root.PTZ.Support.S1.Auxiliary=false
root.PTZ.Support.S1.ServerPreset=true
root.PTZ.Support.S1.DevicePreset=false
root.PTZ.Support.S1.SpeedCtl=true
root.PTZ.Support.S1.JoyStickEmulation=true
root.PTZ.Support.S1.IrCutFilter=false
root.PTZ.Support.S1.AutoIrCutFilter=false
root.PTZ.Support.S1.BackLight=false
root.PTZ.Support.S1.OSDMenu=false
root.PTZ.Support.S1.ActionNotification=true
root.PTZ.Support.S1.ProportionalSpeed=true
root.PTZ.Support.S1.GenericHTTP=false
root.PTZ.Support.S1.LensOffset=false
root.PTZ.Support.S1.AreaZoom=true
root.PTZ.UserAdv.U1.MoveSpeed=100
root.PTZ.Various.V1.CtlQueueing=false
root.PTZ.Various.V1.CtlQueueLimit=20
root.PTZ.Various.V1.CtlQueuePollTime=20
root.PTZ.Various.V1.PanEnabled=true
root.PTZ.Various.V1.TiltEnabled=true
root.PTZ.Various.V1.ZoomEnabled=true
root.PTZ.Various.V1.SpeedCtlEnabled=true
root.PTZ.Various.V1.HomePresetSet=true
root.PTZ.Various.V1.ProportionalSpeedEnabled=true
root.PTZ.Various.V1.MaxProportionalSpeed=200
root.PTZ.Various.V1.ReturnToOverview=30
root.PTZ.Various.V1.Locked=true
"""

PTZ_5_51_Q1921_RESPONSE = """root.PTZ.NbrOfSerPorts=1
root.PTZ.NbrOfCameras=1
root.PTZ.CameraDefault=1
root.PTZ.BoaProtPTZOperator=password
root.PTZ.CamPorts.Cam1Port=-1
root.PTZ.ImageSource.I0.PTZEnabled=true
root.PTZ.Preset.P0.Name=
root.PTZ.Preset.P0.ImageSource=0
root.PTZ.Preset.P0.HomePosition=-1
root.PTZ.PTZDriverFirmwares.Driver1Major=none
root.PTZ.PTZDriverFirmwares.Driver1Minor=none
root.PTZ.PTZDrivers.Driver1=none
root.PTZ.PTZDrivers.DriverNone=none
root.PTZ.PTZDriverStatuses.Driver1Status=0
root.PTZ.PTZDriverVersions.Driver1Version=none
root.PTZ.SerDriverStatuses.Ser1Status=0
root.PTZ.TargetFirmwares.Driver1Major=none
root.PTZ.TargetFirmwares.Driver1Minor=none
root.PTZ.UserCtlQueue.U0.UserGroup=Administrator
root.PTZ.UserCtlQueue.U0.UseCookie=yes
root.PTZ.UserCtlQueue.U0.Priority=10
root.PTZ.UserCtlQueue.U0.TimeoutType=activity
root.PTZ.UserCtlQueue.U0.TimeoutTime=60
root.PTZ.UserCtlQueue.U1.UserGroup=Operator
root.PTZ.UserCtlQueue.U1.UseCookie=yes
root.PTZ.UserCtlQueue.U1.Priority=30
root.PTZ.UserCtlQueue.U1.TimeoutType=activity
root.PTZ.UserCtlQueue.U1.TimeoutTime=60
root.PTZ.UserCtlQueue.U2.UserGroup=Viewer
root.PTZ.UserCtlQueue.U2.UseCookie=yes
root.PTZ.UserCtlQueue.U2.Priority=50
root.PTZ.UserCtlQueue.U2.TimeoutType=timespan
root.PTZ.UserCtlQueue.U2.TimeoutTime=60
root.PTZ.UserCtlQueue.U3.UserGroup=Event
root.PTZ.UserCtlQueue.U3.UseCookie=no
root.PTZ.UserCtlQueue.U3.Priority=20
root.PTZ.UserCtlQueue.U3.TimeoutType=activity
root.PTZ.UserCtlQueue.U3.TimeoutTime=20
root.PTZ.UserCtlQueue.U4.UserGroup=Guardtour
root.PTZ.UserCtlQueue.U4.UseCookie=no
root.PTZ.UserCtlQueue.U4.Priority=40
root.PTZ.UserCtlQueue.U4.TimeoutType=infinity
root.PTZ.UserCtlQueue.U4.TimeoutTime=60
root.PTZ.UserCtlQueue.U5.UserGroup=Autotracking
root.PTZ.UserCtlQueue.U5.UseCookie=no
root.PTZ.UserCtlQueue.U5.Priority=1
root.PTZ.UserCtlQueue.U5.TimeoutType=infinity
root.PTZ.UserCtlQueue.U5.TimeoutTime=60
root.PTZ.UserCtlQueue.U6.UserGroup=Onvif
root.PTZ.UserCtlQueue.U6.UseCookie=no
root.PTZ.UserCtlQueue.U6.Priority=1
root.PTZ.UserCtlQueue.U6.TimeoutType=activity
root.PTZ.UserCtlQueue.U6.TimeoutTime=60
"""

PTZ_11_9_Q1798_RESPONSE = """root.PTZ.BoaProtPTZOperator=password
root.PTZ.CameraDefault=1
root.PTZ.NbrOfCameras=1
root.PTZ.NbrOfSerPorts=0
root.PTZ.PresetNameMaxLen=95
root.PTZ.ResponseEncoding=iso-8859-1
root.PTZ.CamPorts.Cam1Port=1
root.PTZ.ImageSource.I0.PTZEnabled=true
root.PTZ.Limit.L1.MaxFieldAngle=731
root.PTZ.Limit.L1.MaxFocus=9999
root.PTZ.Limit.L1.MaxZoom=9999
root.PTZ.Limit.L1.MinFieldAngle=210
root.PTZ.Limit.L1.MinFocus=1
root.PTZ.Limit.L1.MinZoom=1
root.PTZ.Preset.P0.HomePosition=1
root.PTZ.Preset.P0.ImageSource=0
root.PTZ.Preset.P0.Name=
root.PTZ.Preset.P0.Position.P1.Data=zoom=1
root.PTZ.Preset.P0.Position.P1.Name=Home
root.PTZ.PTZDriverStatuses.Driver1Status=3
root.PTZ.Support.S1.AbsoluteBrightness=false
root.PTZ.Support.S1.AbsoluteFocus=true
root.PTZ.Support.S1.AbsoluteIris=false
root.PTZ.Support.S1.AbsolutePan=false
root.PTZ.Support.S1.AbsoluteTilt=false
root.PTZ.Support.S1.AbsoluteZoom=true
root.PTZ.Support.S1.ActionNotification=true
root.PTZ.Support.S1.AreaZoom=false
root.PTZ.Support.S1.AutoFocus=true
root.PTZ.Support.S1.AutoIrCutFilter=false
root.PTZ.Support.S1.AutoIris=false
root.PTZ.Support.S1.Auxiliary=true
root.PTZ.Support.S1.BackLight=false
root.PTZ.Support.S1.ContinuousBrightness=false
root.PTZ.Support.S1.ContinuousFocus=true
root.PTZ.Support.S1.ContinuousIris=false
root.PTZ.Support.S1.ContinuousPan=false
root.PTZ.Support.S1.ContinuousTilt=false
root.PTZ.Support.S1.ContinuousZoom=true
root.PTZ.Support.S1.DevicePreset=false
root.PTZ.Support.S1.DigitalZoom=true
root.PTZ.Support.S1.GenericHTTP=false
root.PTZ.Support.S1.IrCutFilter=false
root.PTZ.Support.S1.JoyStickEmulation=false
root.PTZ.Support.S1.LensOffset=false
root.PTZ.Support.S1.OSDMenu=false
root.PTZ.Support.S1.ProportionalSpeed=false
root.PTZ.Support.S1.RelativeBrightness=false
root.PTZ.Support.S1.RelativeFocus=true
root.PTZ.Support.S1.RelativeIris=false
root.PTZ.Support.S1.RelativePan=false
root.PTZ.Support.S1.RelativeTilt=false
root.PTZ.Support.S1.RelativeZoom=true
root.PTZ.Support.S1.ServerPreset=true
root.PTZ.Support.S1.SpeedCtl=false
root.PTZ.UserAdv.U1.DeviceModVer=
root.PTZ.UserAdv.U1.DeviceStatus=cam=ok
root.PTZ.UserAdv.U1.ImageFreeze=off
root.PTZ.UserAdv.U1.LastTestDate=Mon Mar  4 14:54:32 2024
root.PTZ.UserCtlQueue.U0.Priority=10
root.PTZ.UserCtlQueue.U0.TimeoutTime=60
root.PTZ.UserCtlQueue.U0.TimeoutType=activity
root.PTZ.UserCtlQueue.U0.UseCookie=no
root.PTZ.UserCtlQueue.U0.UserGroup=Administrator
root.PTZ.UserCtlQueue.U1.Priority=30
root.PTZ.UserCtlQueue.U1.TimeoutTime=60
root.PTZ.UserCtlQueue.U1.TimeoutType=activity
root.PTZ.UserCtlQueue.U1.UseCookie=no
root.PTZ.UserCtlQueue.U1.UserGroup=Operator
root.PTZ.UserCtlQueue.U2.Priority=50
root.PTZ.UserCtlQueue.U2.TimeoutTime=60
root.PTZ.UserCtlQueue.U2.TimeoutType=timespan
root.PTZ.UserCtlQueue.U2.UseCookie=no
root.PTZ.UserCtlQueue.U2.UserGroup=Viewer
root.PTZ.UserCtlQueue.U3.Priority=20
root.PTZ.UserCtlQueue.U3.TimeoutTime=20
root.PTZ.UserCtlQueue.U3.TimeoutType=activity
root.PTZ.UserCtlQueue.U3.UseCookie=no
root.PTZ.UserCtlQueue.U3.UserGroup=Event
root.PTZ.UserCtlQueue.U4.Priority=40
root.PTZ.UserCtlQueue.U4.TimeoutTime=60
root.PTZ.UserCtlQueue.U4.TimeoutType=infinity
root.PTZ.UserCtlQueue.U4.UseCookie=no
root.PTZ.UserCtlQueue.U4.UserGroup=Guardtour
root.PTZ.UserCtlQueue.U5.Priority=35
root.PTZ.UserCtlQueue.U5.TimeoutTime=60
root.PTZ.UserCtlQueue.U5.TimeoutType=infinity
root.PTZ.UserCtlQueue.U5.UseCookie=no
root.PTZ.UserCtlQueue.U5.UserGroup=Autotracking
root.PTZ.UserCtlQueue.U6.Priority=1
root.PTZ.UserCtlQueue.U6.TimeoutTime=60
root.PTZ.UserCtlQueue.U6.TimeoutType=activity
root.PTZ.UserCtlQueue.U6.UseCookie=no
root.PTZ.UserCtlQueue.U6.UserGroup=Onvif
root.PTZ.UserCtlQueue.U7.Priority=33
root.PTZ.UserCtlQueue.U7.TimeoutTime=60
root.PTZ.UserCtlQueue.U7.TimeoutType=infinity
root.PTZ.UserCtlQueue.U7.UseCookie=no
root.PTZ.UserCtlQueue.U7.UserGroup=Focuswindow
root.PTZ.Various.V1.AutoFocus=true
root.PTZ.Various.V1.CtlQueueing=false
root.PTZ.Various.V1.CtlQueueLimit=20
root.PTZ.Various.V1.CtlQueuePollTime=20
root.PTZ.Various.V1.FocusEnabled=true
root.PTZ.Various.V1.HomePresetSet=true
root.PTZ.Various.V1.ReturnToOverview=0
root.PTZ.Various.V1.ZoomEnabled=true
"""

PTZ_10_12_M3058_RESPONSE = """root.PTZ.BoaProtPTZOperator=password
root.PTZ.CameraDefault=1
root.PTZ.NbrOfCameras=12
root.PTZ.NbrOfSerPorts=0
root.PTZ.PresetNameMaxLen=95
root.PTZ.ResponseEncoding=iso-8859-1
root.PTZ.CamPorts.Cam10Port=10
root.PTZ.CamPorts.Cam11Port=11
root.PTZ.CamPorts.Cam12Port=12
root.PTZ.CamPorts.Cam1Port=1
root.PTZ.CamPorts.Cam2Port=2
root.PTZ.CamPorts.Cam3Port=3
root.PTZ.CamPorts.Cam4Port=4
root.PTZ.CamPorts.Cam5Port=5
root.PTZ.CamPorts.Cam6Port=6
root.PTZ.CamPorts.Cam7Port=7
root.PTZ.CamPorts.Cam8Port=8
root.PTZ.CamPorts.Cam9Port=9
root.PTZ.ImageSource.I0.PTZEnabled=true
root.PTZ.Limit.L10.MaxPan=180
root.PTZ.Limit.L10.MaxTilt=7
root.PTZ.Limit.L10.MinPan=-180
root.PTZ.Limit.L10.MinTilt=-30
root.PTZ.Limit.L11.MaxPan=180
root.PTZ.Limit.L11.MaxTilt=7
root.PTZ.Limit.L11.MinPan=-180
root.PTZ.Limit.L11.MinTilt=-30
root.PTZ.Limit.L12.MaxPan=180
root.PTZ.Limit.L12.MaxTilt=-48
root.PTZ.Limit.L12.MinPan=-180
root.PTZ.Limit.L12.MinTilt=-90
root.PTZ.Limit.L2.MaxPan=180
root.PTZ.Limit.L2.MaxTilt=7
root.PTZ.Limit.L2.MinPan=-180
root.PTZ.Limit.L2.MinTilt=-30
root.PTZ.Limit.L3.MaxPan=180
root.PTZ.Limit.L3.MaxTilt=7
root.PTZ.Limit.L3.MinPan=-180
root.PTZ.Limit.L3.MinTilt=-30
root.PTZ.Limit.L4.MaxPan=180
root.PTZ.Limit.L4.MaxTilt=-29
root.PTZ.Limit.L4.MinPan=-180
root.PTZ.Limit.L4.MinTilt=-90
root.PTZ.Limit.L5.MaxFieldAngle=106
root.PTZ.Limit.L5.MaxPan=180
root.PTZ.Limit.L5.MaxTilt=0
root.PTZ.Limit.L5.MaxZoom=9999
root.PTZ.Limit.L5.MinFieldAngle=1
root.PTZ.Limit.L5.MinPan=-180
root.PTZ.Limit.L5.MinTilt=-90
root.PTZ.Limit.L5.MinZoom=1
root.PTZ.Limit.L6.MaxFieldAngle=106
root.PTZ.Limit.L6.MaxPan=180
root.PTZ.Limit.L6.MaxTilt=0
root.PTZ.Limit.L6.MaxZoom=9999
root.PTZ.Limit.L6.MinFieldAngle=1
root.PTZ.Limit.L6.MinPan=-180
root.PTZ.Limit.L6.MinTilt=-90
root.PTZ.Limit.L6.MinZoom=1
root.PTZ.Limit.L7.MaxFieldAngle=106
root.PTZ.Limit.L7.MaxPan=180
root.PTZ.Limit.L7.MaxTilt=0
root.PTZ.Limit.L7.MaxZoom=9999
root.PTZ.Limit.L7.MinFieldAngle=1
root.PTZ.Limit.L7.MinPan=-180
root.PTZ.Limit.L7.MinTilt=-90
root.PTZ.Limit.L7.MinZoom=1
root.PTZ.Limit.L8.MaxFieldAngle=106
root.PTZ.Limit.L8.MaxPan=180
root.PTZ.Limit.L8.MaxTilt=0
root.PTZ.Limit.L8.MaxZoom=9999
root.PTZ.Limit.L8.MinFieldAngle=1
root.PTZ.Limit.L8.MinPan=-180
root.PTZ.Limit.L8.MinTilt=-90
root.PTZ.Limit.L8.MinZoom=1
root.PTZ.Limit.L9.MaxPan=180
root.PTZ.Limit.L9.MaxTilt=7
root.PTZ.Limit.L9.MinPan=-180
root.PTZ.Limit.L9.MinTilt=-30
root.PTZ.Preset.P0.HomePosition=-1
root.PTZ.Preset.P0.ImageSource=0
root.PTZ.Preset.P0.Name=
root.PTZ.Preset.P1.HomePosition=1
root.PTZ.Preset.P1.ImageSource=1
root.PTZ.Preset.P1.Name=
root.PTZ.Preset.P1.Position.P1.Data=pan=103.093414:tilt=0.538361
root.PTZ.Preset.P1.Position.P1.Name=Home
root.PTZ.Preset.P10.HomePosition=1
root.PTZ.Preset.P10.ImageSource=10
root.PTZ.Preset.P10.Name=
root.PTZ.Preset.P10.Position.P1.Data=pan=0.000000:tilt=-20.000000
root.PTZ.Preset.P10.Position.P1.Name=Home
root.PTZ.Preset.P11.HomePosition=1
root.PTZ.Preset.P11.ImageSource=11
root.PTZ.Preset.P11.Name=
root.PTZ.Preset.P11.Position.P1.Data=pan=0.000000:tilt=-51.000000
root.PTZ.Preset.P11.Position.P1.Name=Home
root.PTZ.Preset.P2.HomePosition=1
root.PTZ.Preset.P2.ImageSource=2
root.PTZ.Preset.P2.Name=
root.PTZ.Preset.P2.Position.P1.Data=pan=103.598602:tilt=0.823395
root.PTZ.Preset.P2.Position.P1.Name=Home
root.PTZ.Preset.P3.HomePosition=1
root.PTZ.Preset.P3.ImageSource=3
root.PTZ.Preset.P3.Name=
root.PTZ.Preset.P3.Position.P1.Data=pan=-39.198059:tilt=-37.055649
root.PTZ.Preset.P3.Position.P1.Name=Home
root.PTZ.Preset.P4.HomePosition=1
root.PTZ.Preset.P4.ImageSource=4
root.PTZ.Preset.P4.Name=
root.PTZ.Preset.P4.Position.P1.Data=pan=45.000000:tilt=-51.000000:zoom=1.000000
root.PTZ.Preset.P4.Position.P1.Name=Home
root.PTZ.Preset.P5.HomePosition=1
root.PTZ.Preset.P5.ImageSource=5
root.PTZ.Preset.P5.Name=
root.PTZ.Preset.P5.Position.P1.Data=pan=-40.546646:tilt=-42.884506:zoom=1.000000
root.PTZ.Preset.P5.Position.P1.Name=Home
root.PTZ.Preset.P6.HomePosition=1
root.PTZ.Preset.P6.ImageSource=6
root.PTZ.Preset.P6.Name=
root.PTZ.Preset.P6.Position.P1.Data=pan=-135.000000:tilt=-51.000000:zoom=1.000000
root.PTZ.Preset.P6.Position.P1.Name=Home
root.PTZ.Preset.P7.HomePosition=1
root.PTZ.Preset.P7.ImageSource=7
root.PTZ.Preset.P7.Name=
root.PTZ.Preset.P7.Position.P1.Data=pan=141.015686:tilt=-41.977783:zoom=1.000000
root.PTZ.Preset.P7.Position.P1.Name=Home
root.PTZ.Preset.P8.HomePosition=1
root.PTZ.Preset.P8.ImageSource=8
root.PTZ.Preset.P8.Name=
root.PTZ.Preset.P8.Position.P1.Data=pan=0.000000:tilt=-20.000000
root.PTZ.Preset.P8.Position.P1.Name=Home
root.PTZ.Preset.P9.HomePosition=1
root.PTZ.Preset.P9.ImageSource=9
root.PTZ.Preset.P9.Name=
root.PTZ.Preset.P9.Position.P1.Data=pan=0.000000:tilt=-20.000000
root.PTZ.Preset.P9.Position.P1.Name=Home
root.PTZ.PTZDriverStatuses.Driver10Status=3
root.PTZ.PTZDriverStatuses.Driver11Status=3
root.PTZ.PTZDriverStatuses.Driver12Status=3
root.PTZ.PTZDriverStatuses.Driver1Status=3
root.PTZ.PTZDriverStatuses.Driver2Status=3
root.PTZ.PTZDriverStatuses.Driver3Status=3
root.PTZ.PTZDriverStatuses.Driver4Status=3
root.PTZ.PTZDriverStatuses.Driver5Status=3
root.PTZ.PTZDriverStatuses.Driver6Status=3
root.PTZ.PTZDriverStatuses.Driver7Status=3
root.PTZ.PTZDriverStatuses.Driver8Status=3
root.PTZ.PTZDriverStatuses.Driver9Status=3
root.PTZ.Support.S1.AbsoluteBrightness=false
root.PTZ.Support.S1.AbsoluteFocus=false
root.PTZ.Support.S1.AbsoluteIris=false
root.PTZ.Support.S1.AbsolutePan=false
root.PTZ.Support.S1.AbsoluteTilt=false
root.PTZ.Support.S1.AbsoluteZoom=false
root.PTZ.Support.S1.ActionNotification=false
root.PTZ.Support.S1.AreaZoom=false
root.PTZ.Support.S1.AutoFocus=false
root.PTZ.Support.S1.AutoIrCutFilter=false
root.PTZ.Support.S1.AutoIris=false
root.PTZ.Support.S1.Auxiliary=false
root.PTZ.Support.S1.BackLight=false
root.PTZ.Support.S1.ContinuousBrightness=false
root.PTZ.Support.S1.ContinuousFocus=false
root.PTZ.Support.S1.ContinuousIris=false
root.PTZ.Support.S1.ContinuousPan=false
root.PTZ.Support.S1.ContinuousTilt=false
root.PTZ.Support.S1.ContinuousZoom=false
root.PTZ.Support.S1.DevicePreset=false
root.PTZ.Support.S1.DigitalZoom=false
root.PTZ.Support.S1.GenericHTTP=false
root.PTZ.Support.S1.IrCutFilter=false
root.PTZ.Support.S1.JoyStickEmulation=false
root.PTZ.Support.S1.LensOffset=false
root.PTZ.Support.S1.OSDMenu=false
root.PTZ.Support.S1.ProportionalSpeed=false
root.PTZ.Support.S1.RelativeBrightness=false
root.PTZ.Support.S1.RelativeFocus=false
root.PTZ.Support.S1.RelativeIris=false
root.PTZ.Support.S1.RelativePan=false
root.PTZ.Support.S1.RelativeTilt=false
root.PTZ.Support.S1.RelativeZoom=false
root.PTZ.Support.S1.ServerPreset=false
root.PTZ.Support.S1.SpeedCtl=false
root.PTZ.Support.S10.AbsoluteBrightness=false
root.PTZ.Support.S10.AbsoluteFocus=false
root.PTZ.Support.S10.AbsoluteIris=false
root.PTZ.Support.S10.AbsolutePan=true
root.PTZ.Support.S10.AbsoluteTilt=true
root.PTZ.Support.S10.AbsoluteZoom=false
root.PTZ.Support.S10.ActionNotification=true
root.PTZ.Support.S10.AreaZoom=false
root.PTZ.Support.S10.AutoFocus=false
root.PTZ.Support.S10.AutoIrCutFilter=false
root.PTZ.Support.S10.AutoIris=false
root.PTZ.Support.S10.Auxiliary=false
root.PTZ.Support.S10.BackLight=false
root.PTZ.Support.S10.ContinuousBrightness=false
root.PTZ.Support.S10.ContinuousFocus=false
root.PTZ.Support.S10.ContinuousIris=false
root.PTZ.Support.S10.ContinuousPan=true
root.PTZ.Support.S10.ContinuousTilt=true
root.PTZ.Support.S10.ContinuousZoom=false
root.PTZ.Support.S10.DevicePreset=false
root.PTZ.Support.S10.DigitalZoom=false
root.PTZ.Support.S10.GenericHTTP=false
root.PTZ.Support.S10.IrCutFilter=false
root.PTZ.Support.S10.JoyStickEmulation=false
root.PTZ.Support.S10.LensOffset=false
root.PTZ.Support.S10.OSDMenu=false
root.PTZ.Support.S10.ProportionalSpeed=false
root.PTZ.Support.S10.RelativeBrightness=false
root.PTZ.Support.S10.RelativeFocus=false
root.PTZ.Support.S10.RelativeIris=false
root.PTZ.Support.S10.RelativePan=true
root.PTZ.Support.S10.RelativeTilt=true
root.PTZ.Support.S10.RelativeZoom=false
root.PTZ.Support.S10.ServerPreset=true
root.PTZ.Support.S10.SpeedCtl=false
root.PTZ.Support.S11.AbsoluteBrightness=false
root.PTZ.Support.S11.AbsoluteFocus=false
root.PTZ.Support.S11.AbsoluteIris=false
root.PTZ.Support.S11.AbsolutePan=true
root.PTZ.Support.S11.AbsoluteTilt=true
root.PTZ.Support.S11.AbsoluteZoom=false
root.PTZ.Support.S11.ActionNotification=true
root.PTZ.Support.S11.AreaZoom=false
root.PTZ.Support.S11.AutoFocus=false
root.PTZ.Support.S11.AutoIrCutFilter=false
root.PTZ.Support.S11.AutoIris=false
root.PTZ.Support.S11.Auxiliary=false
root.PTZ.Support.S11.BackLight=false
root.PTZ.Support.S11.ContinuousBrightness=false
root.PTZ.Support.S11.ContinuousFocus=false
root.PTZ.Support.S11.ContinuousIris=false
root.PTZ.Support.S11.ContinuousPan=true
root.PTZ.Support.S11.ContinuousTilt=true
root.PTZ.Support.S11.ContinuousZoom=false
root.PTZ.Support.S11.DevicePreset=false
root.PTZ.Support.S11.DigitalZoom=false
root.PTZ.Support.S11.GenericHTTP=false
root.PTZ.Support.S11.IrCutFilter=false
root.PTZ.Support.S11.JoyStickEmulation=false
root.PTZ.Support.S11.LensOffset=false
root.PTZ.Support.S11.OSDMenu=false
root.PTZ.Support.S11.ProportionalSpeed=false
root.PTZ.Support.S11.RelativeBrightness=false
root.PTZ.Support.S11.RelativeFocus=false
root.PTZ.Support.S11.RelativeIris=false
root.PTZ.Support.S11.RelativePan=true
root.PTZ.Support.S11.RelativeTilt=true
root.PTZ.Support.S11.RelativeZoom=false
root.PTZ.Support.S11.ServerPreset=true
root.PTZ.Support.S11.SpeedCtl=false
root.PTZ.Support.S12.AbsoluteBrightness=false
root.PTZ.Support.S12.AbsoluteFocus=false
root.PTZ.Support.S12.AbsoluteIris=false
root.PTZ.Support.S12.AbsolutePan=true
root.PTZ.Support.S12.AbsoluteTilt=true
root.PTZ.Support.S12.AbsoluteZoom=false
root.PTZ.Support.S12.ActionNotification=true
root.PTZ.Support.S12.AreaZoom=false
root.PTZ.Support.S12.AutoFocus=false
root.PTZ.Support.S12.AutoIrCutFilter=false
root.PTZ.Support.S12.AutoIris=false
root.PTZ.Support.S12.Auxiliary=false
root.PTZ.Support.S12.BackLight=false
root.PTZ.Support.S12.ContinuousBrightness=false
root.PTZ.Support.S12.ContinuousFocus=false
root.PTZ.Support.S12.ContinuousIris=false
root.PTZ.Support.S12.ContinuousPan=true
root.PTZ.Support.S12.ContinuousTilt=true
root.PTZ.Support.S12.ContinuousZoom=false
root.PTZ.Support.S12.DevicePreset=false
root.PTZ.Support.S12.DigitalZoom=false
root.PTZ.Support.S12.GenericHTTP=false
root.PTZ.Support.S12.IrCutFilter=false
root.PTZ.Support.S12.JoyStickEmulation=false
root.PTZ.Support.S12.LensOffset=false
root.PTZ.Support.S12.OSDMenu=false
root.PTZ.Support.S12.ProportionalSpeed=false
root.PTZ.Support.S12.RelativeBrightness=false
root.PTZ.Support.S12.RelativeFocus=false
root.PTZ.Support.S12.RelativeIris=false
root.PTZ.Support.S12.RelativePan=true
root.PTZ.Support.S12.RelativeTilt=true
root.PTZ.Support.S12.RelativeZoom=false
root.PTZ.Support.S12.ServerPreset=true
root.PTZ.Support.S12.SpeedCtl=false
root.PTZ.Support.S2.AbsoluteBrightness=false
root.PTZ.Support.S2.AbsoluteFocus=false
root.PTZ.Support.S2.AbsoluteIris=false
root.PTZ.Support.S2.AbsolutePan=true
root.PTZ.Support.S2.AbsoluteTilt=true
root.PTZ.Support.S2.AbsoluteZoom=false
root.PTZ.Support.S2.ActionNotification=true
root.PTZ.Support.S2.AreaZoom=false
root.PTZ.Support.S2.AutoFocus=false
root.PTZ.Support.S2.AutoIrCutFilter=false
root.PTZ.Support.S2.AutoIris=false
root.PTZ.Support.S2.Auxiliary=false
root.PTZ.Support.S2.BackLight=false
root.PTZ.Support.S2.ContinuousBrightness=false
root.PTZ.Support.S2.ContinuousFocus=false
root.PTZ.Support.S2.ContinuousIris=false
root.PTZ.Support.S2.ContinuousPan=true
root.PTZ.Support.S2.ContinuousTilt=true
root.PTZ.Support.S2.ContinuousZoom=false
root.PTZ.Support.S2.DevicePreset=false
root.PTZ.Support.S2.DigitalZoom=false
root.PTZ.Support.S2.GenericHTTP=false
root.PTZ.Support.S2.IrCutFilter=false
root.PTZ.Support.S2.JoyStickEmulation=false
root.PTZ.Support.S2.LensOffset=false
root.PTZ.Support.S2.OSDMenu=false
root.PTZ.Support.S2.ProportionalSpeed=false
root.PTZ.Support.S2.RelativeBrightness=false
root.PTZ.Support.S2.RelativeFocus=false
root.PTZ.Support.S2.RelativeIris=false
root.PTZ.Support.S2.RelativePan=true
root.PTZ.Support.S2.RelativeTilt=true
root.PTZ.Support.S2.RelativeZoom=false
root.PTZ.Support.S2.ServerPreset=true
root.PTZ.Support.S2.SpeedCtl=false
root.PTZ.Support.S3.AbsoluteBrightness=false
root.PTZ.Support.S3.AbsoluteFocus=false
root.PTZ.Support.S3.AbsoluteIris=false
root.PTZ.Support.S3.AbsolutePan=true
root.PTZ.Support.S3.AbsoluteTilt=true
root.PTZ.Support.S3.AbsoluteZoom=false
root.PTZ.Support.S3.ActionNotification=true
root.PTZ.Support.S3.AreaZoom=false
root.PTZ.Support.S3.AutoFocus=false
root.PTZ.Support.S3.AutoIrCutFilter=false
root.PTZ.Support.S3.AutoIris=false
root.PTZ.Support.S3.Auxiliary=false
root.PTZ.Support.S3.BackLight=false
root.PTZ.Support.S3.ContinuousBrightness=false
root.PTZ.Support.S3.ContinuousFocus=false
root.PTZ.Support.S3.ContinuousIris=false
root.PTZ.Support.S3.ContinuousPan=true
root.PTZ.Support.S3.ContinuousTilt=true
root.PTZ.Support.S3.ContinuousZoom=false
root.PTZ.Support.S3.DevicePreset=false
root.PTZ.Support.S3.DigitalZoom=false
root.PTZ.Support.S3.GenericHTTP=false
root.PTZ.Support.S3.IrCutFilter=false
root.PTZ.Support.S3.JoyStickEmulation=false
root.PTZ.Support.S3.LensOffset=false
root.PTZ.Support.S3.OSDMenu=false
root.PTZ.Support.S3.ProportionalSpeed=false
root.PTZ.Support.S3.RelativeBrightness=false
root.PTZ.Support.S3.RelativeFocus=false
root.PTZ.Support.S3.RelativeIris=false
root.PTZ.Support.S3.RelativePan=true
root.PTZ.Support.S3.RelativeTilt=true
root.PTZ.Support.S3.RelativeZoom=false
root.PTZ.Support.S3.ServerPreset=true
root.PTZ.Support.S3.SpeedCtl=false
root.PTZ.Support.S4.AbsoluteBrightness=false
root.PTZ.Support.S4.AbsoluteFocus=false
root.PTZ.Support.S4.AbsoluteIris=false
root.PTZ.Support.S4.AbsolutePan=true
root.PTZ.Support.S4.AbsoluteTilt=true
root.PTZ.Support.S4.AbsoluteZoom=false
root.PTZ.Support.S4.ActionNotification=true
root.PTZ.Support.S4.AreaZoom=false
root.PTZ.Support.S4.AutoFocus=false
root.PTZ.Support.S4.AutoIrCutFilter=false
root.PTZ.Support.S4.AutoIris=false
root.PTZ.Support.S4.Auxiliary=true
root.PTZ.Support.S4.BackLight=false
root.PTZ.Support.S4.ContinuousBrightness=false
root.PTZ.Support.S4.ContinuousFocus=false
root.PTZ.Support.S4.ContinuousIris=false
root.PTZ.Support.S4.ContinuousPan=true
root.PTZ.Support.S4.ContinuousTilt=true
root.PTZ.Support.S4.ContinuousZoom=false
root.PTZ.Support.S4.DevicePreset=false
root.PTZ.Support.S4.DigitalZoom=false
root.PTZ.Support.S4.GenericHTTP=false
root.PTZ.Support.S4.IrCutFilter=false
root.PTZ.Support.S4.JoyStickEmulation=false
root.PTZ.Support.S4.LensOffset=false
root.PTZ.Support.S4.OSDMenu=false
root.PTZ.Support.S4.ProportionalSpeed=false
root.PTZ.Support.S4.RelativeBrightness=false
root.PTZ.Support.S4.RelativeFocus=false
root.PTZ.Support.S4.RelativeIris=false
root.PTZ.Support.S4.RelativePan=true
root.PTZ.Support.S4.RelativeTilt=true
root.PTZ.Support.S4.RelativeZoom=false
root.PTZ.Support.S4.ServerPreset=true
root.PTZ.Support.S4.SpeedCtl=false
root.PTZ.Support.S5.AbsoluteBrightness=false
root.PTZ.Support.S5.AbsoluteFocus=false
root.PTZ.Support.S5.AbsoluteIris=false
root.PTZ.Support.S5.AbsolutePan=true
root.PTZ.Support.S5.AbsoluteTilt=true
root.PTZ.Support.S5.AbsoluteZoom=true
root.PTZ.Support.S5.ActionNotification=true
root.PTZ.Support.S5.AreaZoom=true
root.PTZ.Support.S5.AutoFocus=false
root.PTZ.Support.S5.AutoIrCutFilter=false
root.PTZ.Support.S5.AutoIris=false
root.PTZ.Support.S5.Auxiliary=true
root.PTZ.Support.S5.BackLight=false
root.PTZ.Support.S5.ContinuousBrightness=false
root.PTZ.Support.S5.ContinuousFocus=false
root.PTZ.Support.S5.ContinuousIris=false
root.PTZ.Support.S5.ContinuousPan=true
root.PTZ.Support.S5.ContinuousTilt=true
root.PTZ.Support.S5.ContinuousZoom=true
root.PTZ.Support.S5.DevicePreset=false
root.PTZ.Support.S5.DigitalZoom=false
root.PTZ.Support.S5.GenericHTTP=false
root.PTZ.Support.S5.IrCutFilter=false
root.PTZ.Support.S5.JoyStickEmulation=true
root.PTZ.Support.S5.LensOffset=false
root.PTZ.Support.S5.OSDMenu=false
root.PTZ.Support.S5.ProportionalSpeed=true
root.PTZ.Support.S5.RelativeBrightness=false
root.PTZ.Support.S5.RelativeFocus=false
root.PTZ.Support.S5.RelativeIris=false
root.PTZ.Support.S5.RelativePan=true
root.PTZ.Support.S5.RelativeTilt=true
root.PTZ.Support.S5.RelativeZoom=true
root.PTZ.Support.S5.ServerPreset=true
root.PTZ.Support.S5.SpeedCtl=true
root.PTZ.Support.S6.AbsoluteBrightness=false
root.PTZ.Support.S6.AbsoluteFocus=false
root.PTZ.Support.S6.AbsoluteIris=false
root.PTZ.Support.S6.AbsolutePan=true
root.PTZ.Support.S6.AbsoluteTilt=true
root.PTZ.Support.S6.AbsoluteZoom=true
root.PTZ.Support.S6.ActionNotification=true
root.PTZ.Support.S6.AreaZoom=true
root.PTZ.Support.S6.AutoFocus=false
root.PTZ.Support.S6.AutoIrCutFilter=false
root.PTZ.Support.S6.AutoIris=false
root.PTZ.Support.S6.Auxiliary=true
root.PTZ.Support.S6.BackLight=false
root.PTZ.Support.S6.ContinuousBrightness=false
root.PTZ.Support.S6.ContinuousFocus=false
root.PTZ.Support.S6.ContinuousIris=false
root.PTZ.Support.S6.ContinuousPan=true
root.PTZ.Support.S6.ContinuousTilt=true
root.PTZ.Support.S6.ContinuousZoom=true
root.PTZ.Support.S6.DevicePreset=false
root.PTZ.Support.S6.DigitalZoom=false
root.PTZ.Support.S6.GenericHTTP=false
root.PTZ.Support.S6.IrCutFilter=false
root.PTZ.Support.S6.JoyStickEmulation=true
root.PTZ.Support.S6.LensOffset=false
root.PTZ.Support.S6.OSDMenu=false
root.PTZ.Support.S6.ProportionalSpeed=true
root.PTZ.Support.S6.RelativeBrightness=false
root.PTZ.Support.S6.RelativeFocus=false
root.PTZ.Support.S6.RelativeIris=false
root.PTZ.Support.S6.RelativePan=true
root.PTZ.Support.S6.RelativeTilt=true
root.PTZ.Support.S6.RelativeZoom=true
root.PTZ.Support.S6.ServerPreset=true
root.PTZ.Support.S6.SpeedCtl=true
root.PTZ.Support.S7.AbsoluteBrightness=false
root.PTZ.Support.S7.AbsoluteFocus=false
root.PTZ.Support.S7.AbsoluteIris=false
root.PTZ.Support.S7.AbsolutePan=true
root.PTZ.Support.S7.AbsoluteTilt=true
root.PTZ.Support.S7.AbsoluteZoom=true
root.PTZ.Support.S7.ActionNotification=true
root.PTZ.Support.S7.AreaZoom=true
root.PTZ.Support.S7.AutoFocus=false
root.PTZ.Support.S7.AutoIrCutFilter=false
root.PTZ.Support.S7.AutoIris=false
root.PTZ.Support.S7.Auxiliary=true
root.PTZ.Support.S7.BackLight=false
root.PTZ.Support.S7.ContinuousBrightness=false
root.PTZ.Support.S7.ContinuousFocus=false
root.PTZ.Support.S7.ContinuousIris=false
root.PTZ.Support.S7.ContinuousPan=true
root.PTZ.Support.S7.ContinuousTilt=true
root.PTZ.Support.S7.ContinuousZoom=true
root.PTZ.Support.S7.DevicePreset=false
root.PTZ.Support.S7.DigitalZoom=false
root.PTZ.Support.S7.GenericHTTP=false
root.PTZ.Support.S7.IrCutFilter=false
root.PTZ.Support.S7.JoyStickEmulation=true
root.PTZ.Support.S7.LensOffset=false
root.PTZ.Support.S7.OSDMenu=false
root.PTZ.Support.S7.ProportionalSpeed=true
root.PTZ.Support.S7.RelativeBrightness=false
root.PTZ.Support.S7.RelativeFocus=false
root.PTZ.Support.S7.RelativeIris=false
root.PTZ.Support.S7.RelativePan=true
root.PTZ.Support.S7.RelativeTilt=true
root.PTZ.Support.S7.RelativeZoom=true
root.PTZ.Support.S7.ServerPreset=true
root.PTZ.Support.S7.SpeedCtl=true
root.PTZ.Support.S8.AbsoluteBrightness=false
root.PTZ.Support.S8.AbsoluteFocus=false
root.PTZ.Support.S8.AbsoluteIris=false
root.PTZ.Support.S8.AbsolutePan=true
root.PTZ.Support.S8.AbsoluteTilt=true
root.PTZ.Support.S8.AbsoluteZoom=true
root.PTZ.Support.S8.ActionNotification=true
root.PTZ.Support.S8.AreaZoom=true
root.PTZ.Support.S8.AutoFocus=false
root.PTZ.Support.S8.AutoIrCutFilter=false
root.PTZ.Support.S8.AutoIris=false
root.PTZ.Support.S8.Auxiliary=true
root.PTZ.Support.S8.BackLight=false
root.PTZ.Support.S8.ContinuousBrightness=false
root.PTZ.Support.S8.ContinuousFocus=false
root.PTZ.Support.S8.ContinuousIris=false
root.PTZ.Support.S8.ContinuousPan=true
root.PTZ.Support.S8.ContinuousTilt=true
root.PTZ.Support.S8.ContinuousZoom=true
root.PTZ.Support.S8.DevicePreset=false
root.PTZ.Support.S8.DigitalZoom=false
root.PTZ.Support.S8.GenericHTTP=false
root.PTZ.Support.S8.IrCutFilter=false
root.PTZ.Support.S8.JoyStickEmulation=true
root.PTZ.Support.S8.LensOffset=false
root.PTZ.Support.S8.OSDMenu=false
root.PTZ.Support.S8.ProportionalSpeed=true
root.PTZ.Support.S8.RelativeBrightness=false
root.PTZ.Support.S8.RelativeFocus=false
root.PTZ.Support.S8.RelativeIris=false
root.PTZ.Support.S8.RelativePan=true
root.PTZ.Support.S8.RelativeTilt=true
root.PTZ.Support.S8.RelativeZoom=true
root.PTZ.Support.S8.ServerPreset=true
root.PTZ.Support.S8.SpeedCtl=true
root.PTZ.Support.S9.AbsoluteBrightness=false
root.PTZ.Support.S9.AbsoluteFocus=false
root.PTZ.Support.S9.AbsoluteIris=false
root.PTZ.Support.S9.AbsolutePan=true
root.PTZ.Support.S9.AbsoluteTilt=true
root.PTZ.Support.S9.AbsoluteZoom=false
root.PTZ.Support.S9.ActionNotification=true
root.PTZ.Support.S9.AreaZoom=false
root.PTZ.Support.S9.AutoFocus=false
root.PTZ.Support.S9.AutoIrCutFilter=false
root.PTZ.Support.S9.AutoIris=false
root.PTZ.Support.S9.Auxiliary=false
root.PTZ.Support.S9.BackLight=false
root.PTZ.Support.S9.ContinuousBrightness=false
root.PTZ.Support.S9.ContinuousFocus=false
root.PTZ.Support.S9.ContinuousIris=false
root.PTZ.Support.S9.ContinuousPan=true
root.PTZ.Support.S9.ContinuousTilt=true
root.PTZ.Support.S9.ContinuousZoom=false
root.PTZ.Support.S9.DevicePreset=false
root.PTZ.Support.S9.DigitalZoom=false
root.PTZ.Support.S9.GenericHTTP=false
root.PTZ.Support.S9.IrCutFilter=false
root.PTZ.Support.S9.JoyStickEmulation=false
root.PTZ.Support.S9.LensOffset=false
root.PTZ.Support.S9.OSDMenu=false
root.PTZ.Support.S9.ProportionalSpeed=false
root.PTZ.Support.S9.RelativeBrightness=false
root.PTZ.Support.S9.RelativeFocus=false
root.PTZ.Support.S9.RelativeIris=false
root.PTZ.Support.S9.RelativePan=true
root.PTZ.Support.S9.RelativeTilt=true
root.PTZ.Support.S9.RelativeZoom=false
root.PTZ.Support.S9.ServerPreset=true
root.PTZ.Support.S9.SpeedCtl=false
root.PTZ.UserAdv.U10.MoveSpeed=100
root.PTZ.UserAdv.U11.MoveSpeed=100
root.PTZ.UserAdv.U12.MoveSpeed=100
root.PTZ.UserAdv.U2.MoveSpeed=100
root.PTZ.UserAdv.U3.MoveSpeed=100
root.PTZ.UserAdv.U4.MoveSpeed=100
root.PTZ.UserAdv.U5.MoveSpeed=100
root.PTZ.UserAdv.U6.MoveSpeed=100
root.PTZ.UserAdv.U7.MoveSpeed=100
root.PTZ.UserAdv.U8.MoveSpeed=100
root.PTZ.UserAdv.U9.MoveSpeed=100
root.PTZ.UserCtlQueue.U0.Priority=10
root.PTZ.UserCtlQueue.U0.TimeoutTime=60
root.PTZ.UserCtlQueue.U0.TimeoutType=activity
root.PTZ.UserCtlQueue.U0.UseCookie=no
root.PTZ.UserCtlQueue.U0.UserGroup=Administrator
root.PTZ.UserCtlQueue.U1.Priority=30
root.PTZ.UserCtlQueue.U1.TimeoutTime=60
root.PTZ.UserCtlQueue.U1.TimeoutType=activity
root.PTZ.UserCtlQueue.U1.UseCookie=no
root.PTZ.UserCtlQueue.U1.UserGroup=Operator
root.PTZ.UserCtlQueue.U2.Priority=50
root.PTZ.UserCtlQueue.U2.TimeoutTime=60
root.PTZ.UserCtlQueue.U2.TimeoutType=timespan
root.PTZ.UserCtlQueue.U2.UseCookie=no
root.PTZ.UserCtlQueue.U2.UserGroup=Viewer
root.PTZ.UserCtlQueue.U3.Priority=20
root.PTZ.UserCtlQueue.U3.TimeoutTime=20
root.PTZ.UserCtlQueue.U3.TimeoutType=activity
root.PTZ.UserCtlQueue.U3.UseCookie=no
root.PTZ.UserCtlQueue.U3.UserGroup=Event
root.PTZ.UserCtlQueue.U4.Priority=40
root.PTZ.UserCtlQueue.U4.TimeoutTime=60
root.PTZ.UserCtlQueue.U4.TimeoutType=infinity
root.PTZ.UserCtlQueue.U4.UseCookie=no
root.PTZ.UserCtlQueue.U4.UserGroup=Guardtour
root.PTZ.UserCtlQueue.U5.Priority=35
root.PTZ.UserCtlQueue.U5.TimeoutTime=60
root.PTZ.UserCtlQueue.U5.TimeoutType=infinity
root.PTZ.UserCtlQueue.U5.UseCookie=no
root.PTZ.UserCtlQueue.U5.UserGroup=Autotracking
root.PTZ.UserCtlQueue.U6.Priority=1
root.PTZ.UserCtlQueue.U6.TimeoutTime=60
root.PTZ.UserCtlQueue.U6.TimeoutType=activity
root.PTZ.UserCtlQueue.U6.UseCookie=no
root.PTZ.UserCtlQueue.U6.UserGroup=Onvif
root.PTZ.Various.V10.CtlQueueing=false
root.PTZ.Various.V10.CtlQueueLimit=20
root.PTZ.Various.V10.CtlQueuePollTime=20
root.PTZ.Various.V10.HomePresetSet=true
root.PTZ.Various.V10.Locked=false
root.PTZ.Various.V10.PanEnabled=true
root.PTZ.Various.V10.ReturnToOverview=0
root.PTZ.Various.V10.TiltEnabled=true
root.PTZ.Various.V11.CtlQueueing=false
root.PTZ.Various.V11.CtlQueueLimit=20
root.PTZ.Various.V11.CtlQueuePollTime=20
root.PTZ.Various.V11.HomePresetSet=true
root.PTZ.Various.V11.Locked=false
root.PTZ.Various.V11.PanEnabled=true
root.PTZ.Various.V11.ReturnToOverview=0
root.PTZ.Various.V11.TiltEnabled=true
root.PTZ.Various.V12.CtlQueueing=false
root.PTZ.Various.V12.CtlQueueLimit=20
root.PTZ.Various.V12.CtlQueuePollTime=20
root.PTZ.Various.V12.HomePresetSet=true
root.PTZ.Various.V12.Locked=false
root.PTZ.Various.V12.PanEnabled=true
root.PTZ.Various.V12.ReturnToOverview=0
root.PTZ.Various.V12.TiltEnabled=true
root.PTZ.Various.V2.CtlQueueing=false
root.PTZ.Various.V2.CtlQueueLimit=20
root.PTZ.Various.V2.CtlQueuePollTime=20
root.PTZ.Various.V2.HomePresetSet=true
root.PTZ.Various.V2.Locked=false
root.PTZ.Various.V2.PanEnabled=true
root.PTZ.Various.V2.ReturnToOverview=0
root.PTZ.Various.V2.TiltEnabled=true
root.PTZ.Various.V3.CtlQueueing=false
root.PTZ.Various.V3.CtlQueueLimit=20
root.PTZ.Various.V3.CtlQueuePollTime=20
root.PTZ.Various.V3.HomePresetSet=true
root.PTZ.Various.V3.Locked=false
root.PTZ.Various.V3.PanEnabled=true
root.PTZ.Various.V3.ReturnToOverview=0
root.PTZ.Various.V3.TiltEnabled=true
root.PTZ.Various.V4.CtlQueueing=false
root.PTZ.Various.V4.CtlQueueLimit=20
root.PTZ.Various.V4.CtlQueuePollTime=20
root.PTZ.Various.V4.HomePresetSet=true
root.PTZ.Various.V4.Locked=false
root.PTZ.Various.V4.PanEnabled=true
root.PTZ.Various.V4.ReturnToOverview=0
root.PTZ.Various.V4.TiltEnabled=true
root.PTZ.Various.V5.CtlQueueing=false
root.PTZ.Various.V5.CtlQueueLimit=20
root.PTZ.Various.V5.CtlQueuePollTime=20
root.PTZ.Various.V5.HomePresetSet=true
root.PTZ.Various.V5.Locked=false
root.PTZ.Various.V5.MaxProportionalSpeed=200
root.PTZ.Various.V5.PanEnabled=true
root.PTZ.Various.V5.ProportionalSpeedEnabled=true
root.PTZ.Various.V5.ReturnToOverview=0
root.PTZ.Various.V5.SpeedCtlEnabled=true
root.PTZ.Various.V5.TiltEnabled=true
root.PTZ.Various.V5.ZoomEnabled=true
root.PTZ.Various.V6.CtlQueueing=false
root.PTZ.Various.V6.CtlQueueLimit=20
root.PTZ.Various.V6.CtlQueuePollTime=20
root.PTZ.Various.V6.HomePresetSet=true
root.PTZ.Various.V6.Locked=false
root.PTZ.Various.V6.MaxProportionalSpeed=200
root.PTZ.Various.V6.PanEnabled=true
root.PTZ.Various.V6.ProportionalSpeedEnabled=true
root.PTZ.Various.V6.ReturnToOverview=0
root.PTZ.Various.V6.SpeedCtlEnabled=true
root.PTZ.Various.V6.TiltEnabled=true
root.PTZ.Various.V6.ZoomEnabled=true
root.PTZ.Various.V7.CtlQueueing=false
root.PTZ.Various.V7.CtlQueueLimit=20
root.PTZ.Various.V7.CtlQueuePollTime=20
root.PTZ.Various.V7.HomePresetSet=true
root.PTZ.Various.V7.Locked=false
root.PTZ.Various.V7.MaxProportionalSpeed=200
root.PTZ.Various.V7.PanEnabled=true
root.PTZ.Various.V7.ProportionalSpeedEnabled=true
root.PTZ.Various.V7.ReturnToOverview=0
root.PTZ.Various.V7.SpeedCtlEnabled=true
root.PTZ.Various.V7.TiltEnabled=true
root.PTZ.Various.V7.ZoomEnabled=true
root.PTZ.Various.V8.CtlQueueing=false
root.PTZ.Various.V8.CtlQueueLimit=20
root.PTZ.Various.V8.CtlQueuePollTime=20
root.PTZ.Various.V8.HomePresetSet=true
root.PTZ.Various.V8.Locked=false
root.PTZ.Various.V8.MaxProportionalSpeed=200
root.PTZ.Various.V8.PanEnabled=true
root.PTZ.Various.V8.ProportionalSpeedEnabled=true
root.PTZ.Various.V8.ReturnToOverview=0
root.PTZ.Various.V8.SpeedCtlEnabled=true
root.PTZ.Various.V8.TiltEnabled=true
root.PTZ.Various.V8.ZoomEnabled=true
root.PTZ.Various.V9.CtlQueueing=false
root.PTZ.Various.V9.CtlQueueLimit=20
root.PTZ.Various.V9.CtlQueuePollTime=20
root.PTZ.Various.V9.HomePresetSet=true
root.PTZ.Various.V9.Locked=false
root.PTZ.Various.V9.PanEnabled=true
root.PTZ.Various.V9.ReturnToOverview=0
root.PTZ.Various.V9.TiltEnabled=true
"""


@pytest.fixture
def ptz_handler(axis_device: AxisDevice) -> PtzParameterHandler:
    """Return the PTZ control mock object."""
    return axis_device.vapix.params.ptz_handler


async def test_update_ptz(respx_mock, ptz_handler: PtzParameterHandler):
    """Verify that update ptz works."""
    route = respx_mock.post(
        "/axis-cgi/param.cgi",
        data={"action": "list", "group": "root.PTZ"},
    ).respond(
        text=PTZ_RESPONSE,
        headers={"Content-Type": "text/plain"},
    )
    assert not ptz_handler.initialized

    await ptz_handler.update()

    assert route.called
    assert route.calls.last.request.method == "POST"
    assert route.calls.last.request.url.path == "/axis-cgi/param.cgi"

    assert ptz_handler.initialized
    ptz = ptz_handler["0"]
    assert ptz.camera_default == 1
    assert ptz.number_of_cameras == 1
    assert ptz.number_of_serial_ports == 1
    assert ptz.cam_ports == {"Cam1Port": 1}

    assert len(ptz.limits) == 1
    limit = ptz.limits["1"]
    assert limit.max_brightness == 9999
    assert limit.min_brightness == 1
    assert limit.max_field_angle == 623
    assert limit.min_field_angle == 22
    assert limit.max_focus == 9999
    assert limit.min_focus == 770
    assert limit.max_iris == 9999
    assert limit.min_iris == 1
    assert limit.max_pan == 170
    assert limit.min_pan == -170
    assert limit.max_tilt == 90
    assert limit.min_tilt == -20
    assert limit.max_zoom == 9999
    assert limit.min_zoom == 1

    assert len(ptz.support) == 1
    support = ptz.support["1"]
    assert support.absolute_brightness
    assert support.absolute_focus
    assert support.absolute_iris
    assert support.absolute_pan
    assert support.absolute_tilt
    assert support.absolute_zoom
    assert support.action_notification
    assert support.area_zoom
    assert support.auto_focus
    assert support.auto_ir_cut_filter
    assert support.auto_iris
    assert support.auxiliary
    assert support.backLight
    assert support.continuous_brightness is False
    assert support.continuous_focus
    assert support.continuous_iris is False
    assert support.continuous_pan
    assert support.continuous_tilt
    assert support.continuousZoom
    assert support.device_preset is False
    assert support.digital_zoom
    assert support.generic_http is False
    assert support.ir_cut_filter
    assert support.joystick_emulation
    assert support.lens_offset is False
    assert support.osd_menu is False
    assert support.proportional_speed
    assert support.relative_brightness
    assert support.relative_focus
    assert support.relative_iris
    assert support.relative_pan
    assert support.relative_tilt
    assert support.relative_zoom
    assert support.server_preset
    assert support.speed_control

    assert len(ptz.various) == 1
    various = ptz.various["1"]
    assert various.control_queueing is False
    assert various.control_queue_limit
    assert various.control_queue_poll_time == 20
    assert various.home_preset_set
    assert various.locked is False
    assert various.max_proportional_speed == 200
    assert various.pan_enabled
    assert various.proportional_speed_enabled
    assert various.return_to_overview == 0
    assert various.speed_control_enabled
    assert various.tilt_enabled
    assert various.zoom_enabled

    await ptz_handler.update()


@pytest.mark.parametrize(
    ("ptz_response"),
    [
        PTZ_5_51_M1054_RESPONSE,
        PTZ_5_51_M3024_RESPONSE,
        PTZ_5_51_Q1921_RESPONSE,
        PTZ_10_12_M3058_RESPONSE,
        PTZ_11_9_Q1798_RESPONSE,
    ],
)
async def test_ptz_5_51(respx_mock, ptz_handler: PtzParameterHandler, ptz_response):
    """Verify that update ptz works.

    Max/Min Field Angle not reported.
    NbrOfCameras not reported.
    """
    respx_mock.post(
        "/axis-cgi/param.cgi", data={"action": "list", "group": "root.PTZ"}
    ).respond(text=ptz_response, headers={"Content-Type": "text/plain"})

    await ptz_handler.update()
