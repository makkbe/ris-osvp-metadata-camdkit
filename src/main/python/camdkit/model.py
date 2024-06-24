#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the SMTPE RIS OSVP Metadata Project

"""Data model"""

import numbers
import typing

from camdkit.framework import *

class ActiveSensorPhysicalDimensions(IntegerDimensionsParameter):
  "Height and width of the active area of the camera sensor"

  canonical_name = "activeSensorPhysicalDimensions"
  sampling = Sampling.STATIC
  units = "micron"


class Duration(StrictlyPositiveRationalParameter):
  """Duration of the clip"""

  canonical_name = "duration"
  sampling = Sampling.STATIC
  units = "second"


class CaptureFPS(StrictlyPositiveRationalParameter):
  """Capture frame frate of the camera"""

  canonical_name = "captureRate"
  sampling = Sampling.STATIC
  units = "hertz"


class ISO(StrictlyPositiveIntegerParameter):
  """Arithmetic ISO scale as defined in ISO 12232"""

  canonical_name = "isoSpeed"
  sampling = Sampling.STATIC
  units = "unit"


class LensSerialNumber(StringParameter):
  """Unique identifier of the lens"""

  canonical_name = "lensSerialNumber"
  sampling = Sampling.STATIC
  units = None

class LensMake(StringParameter):
  """Make of the lens"""

  canonical_name = "lensMake"
  sampling = Sampling.STATIC
  units = None

class LensModel(StringParameter):
  """Model of the lens"""

  canonical_name = "lensModel"
  sampling = Sampling.STATIC
  units = None

class LensFirmware(StringParameter):
  """Version identifier for the firmware of the lens"""

  canonical_name = "lensFirmwareVersion"
  sampling = Sampling.STATIC
  units = None

class CameraSerialNumber(StringParameter):
  """Unique identifier of the camera"""

  canonical_name = "cameraSerialNumber"
  sampling = Sampling.STATIC
  units = None

class CameraMake(StringParameter):
  """Make of the camera"""

  canonical_name = "cameraMake"
  sampling = Sampling.STATIC
  units = None

class CameraModel(StringParameter):
  """Model of the camera"""

  canonical_name = "cameraModel"
  sampling = Sampling.STATIC
  units = None

class CameraFirmware(StringParameter):
  """Version identifier for the firmware of the camera"""

  canonical_name = "cameraFirmwareVersion"
  sampling = Sampling.STATIC
  units = None

class TStop(StrictlyPositiveIntegerParameter):
  """The linear t-number of the lens, equal to the F-number of the lens divided
  by the square root of the transmittance of the lens."""

  canonical_name = "tStop"
  sampling = Sampling.REGULAR
  units = "0.001 unit"

class FStop(StrictlyPositiveIntegerParameter):
  """The linear f-number of the lens, equal to the focal length divided by the
  diameter of the entrance pupil."""

  canonical_name = "fStop"
  sampling = Sampling.REGULAR
  units = "0.001 unit"
  section = "lens"

class FocalLength(StrictlyPositiveIntegerParameter):
  """Nominal focal length of the lens. The number printed on the side of a prime
  lens, e.g. 50 mm, and undefined in the case of a zoom lens."""

  canonical_name = "focalLength"
  sampling = Sampling.REGULAR
  units = "millimeter"


class FocusPosition(StrictlyPositiveIntegerParameter):
  """Focus distance/position of the lens"""

  canonical_name = "focusPosition"
  sampling = Sampling.REGULAR
  units = "millimeter"


class EntrancePupilPosition(RationalParameter):
  """Position of the entrance pupil relative to the nominal imaging plane
  (positive if the entrance pupil is located on the side of the nominal imaging
  plane that is towards the object, and negative otherwise)"""

  canonical_name = "entrancePupilPosition"
  sampling = Sampling.REGULAR
  units = "millimeter"

class AnamorphicSqueeze(StrictlyPositiveIntegerParameter):
  """Nominal ratio of height to width of the image of an axis-aligned square
  captured by the camera sensor. It can be used to de-squeeze images but is not
  however an exact number over the entire captured area due to a lens' intrinsic
  analog nature."""

  canonical_name = "anamorphicSqueeze"
  sampling = Sampling.STATIC
  units = "0.01 unit"

class FDLLink(UUIDURNParameter):
  """Unique identifier of the FDL used by the camera."""

  canonical_name = "fdlLink"
  sampling = Sampling.STATIC
  units = None


class ShutterAngle(Parameter):
  """Shutter speed as a fraction of the capture frame rate. The shutter speed
  (in units of 1/s) is equal to the value of the parameter divided by 360 times
  the capture frame rate."""

  canonical_name = "shutterAngle"
  sampling = Sampling.STATIC
  units = "degrees (angular)"

  @staticmethod
  def validate(value) -> bool:
    """The parameter shall be an integer in the range (0..360000]."""

    return isinstance(value, numbers.Integral) and 0 < value <= 360000

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    return value

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    return int(value)

  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "integer",
      "minimum": 1,
      "maximum": 360000
    }
  
class MetadataStatus(StringParameter):
  """Free string that describes the status of the system - e.g. 'Optical Good' in a tracking system"""

  canonical_name = "status"
  sampling = Sampling.REGULAR
  units = None
  section = "metadata"
  
class MetadataRecording(BooleanParameter):
  """True if the system is recording data - e.g. tracking data"""
  
  canonical_name = "recording"
  sampling = Sampling.REGULAR
  section = "metadata"
  
class MetadataSlate(StringParameter):
  """Free string that describes the recording slate - e.g. 'A101_A_4'"""
  
  canonical_name = "slate"
  sampling = Sampling.REGULAR
  section = "metadata"
  
class MetadataNotes(StringParameter):
  """Free string for notes"""
  
  canonical_name = "notes"
  sampling = Sampling.REGULAR
  section = "metadata"

class MetadataRelatedPackets(ArrayParameter):
  """List of packet unique IDs that are related to this packet."""

  canonical_name = "relatedPackets"
  sampling = Sampling.REGULAR
  units = None
  item_class = UUIDURNParameter
  section = "metadata"

class PacketId(UUIDURNParameter):
  """Unique identifier of the packet in which data is being traansported."""

  canonical_name = "packetId"
  sampling = Sampling.REGULAR
  units = None
  
class Protocol(StringParameter):
  """Unique identifier of the packet in which data is being traansported."""

  canonical_name = "protocol"
  sampling = Sampling.REGULAR
  units = None

class Transforms(Parameter):
  """
  X,Y,Z in metres of camera sensor relative to stage origin.
  The Z axis points upwards and the coordinate system is right-handed.
  Y points in the forward camera direction (when pan, tilt and roll are zero).
  For example in an LED volume Y would point towards the centre of the LED wall and so X would point to camera-right.
  Rotation expressed as euler angles in degrees of the camera sensor relative to stage origin
  Rotations are intrinsic and are measured around the axes ZXY, commonly referred to as [pan, tilt, roll]
  Notes on Euler angles:
  Euler angles are human readable and unlike quarternions, provide the ability for cycles (with angles >360 or <0 degrees).
  Where a tracking system is providing the pose of a virtual camera, gimbal lock does not present the physical challenges of a robotic system.
  Conversion to and from quarternions is trivial with an acceptable loss of precision
  """
  sampling = Sampling.REGULAR
  canonical_name = "transforms"
  units = "metres / degrees"

  @staticmethod
  def validate(value) -> bool:
    """Each component of each transform shall contain Real numbers."""

    if not isinstance(value, typing.Tuple):
      return False
    
    if len(value) == 0:
      return False

    for transform in value:
      if not isinstance(transform, Transform):
        return False
      if not isinstance(transform.translation, Vector3):
        return False
      if not isinstance(transform.rotation, Rotator3):
        return False
      # Scale is optional
      if transform.scale != None and not isinstance(transform.scale, Vector3):
        return False
      if not isinstance(transform.translation.x, numbers.Real) \
         or not isinstance(transform.translation.y, numbers.Real) \
         or not isinstance(transform.translation.z, numbers.Real):
        return False
      if not isinstance(transform.rotation.pan, numbers.Real) \
         or not isinstance(transform.rotation.tilt, numbers.Real) \
         or not isinstance(transform.rotation.roll, numbers.Real):
        return False
      if transform.scale != None:
        if not isinstance(transform.scale.x, numbers.Real) \
           or not isinstance(transform.scale.y, numbers.Real) \
           or not isinstance(transform.scale.z, numbers.Real):
          return False
      # Name and parent are optional
      if transform.name != None and not isinstance(transform.name, str):
        return False
      if transform.parent != None and not isinstance(transform.parent, str):
        return False

    return True

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    transforms = []
    for transform in value:
      # Factory ignores the optional fields
      transforms.append(dataclasses.asdict(transform, \
                                           dict_factory=lambda x: {k: v for (k, v) in x if v is not None}))
    return transforms  

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    transforms = ()
    for v in value:
      transforms += (Transform(**v), )
    return transforms
  
  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "array",
      "minItems": 1,
      "uniqueItems": False,
      "items": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
          "translation": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
              "x": {
                  "type": "number",
              },
              "y": {
                  "type": "number",
              },
              "z": {
                  "type": "number"
              }
            }
          },
          "rotation": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
              "pan": {
                  "type": "number",
              },
              "tilt": {
                  "type": "number",
              },
              "roll": {
                  "type": "number"
              }
            }
          },
          "scale": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
              "x": {
                  "type": "number",
              },
              "y": {
                  "type": "number",
              },
              "z": {
                  "type": "number"
              }
            }
          }
        },
        "required": ["translation", "rotation"]
      }
    }
  
  
class TimingMode(EnumParameter):
  """
  'external' timing mode describes the case where the transport packet has inherent timing, so no explicit timing data is required in the data).
  'internal' mode indicates the transport packet does not have inherent timing, so a PTP timestamp must be provided.
  """
  sampling = Sampling.REGULAR
  canonical_name = "mode"
  section = "timing"
  units = None

class TimingSynchronization(Parameter):
  """
  TODO doc
  """
  
  sampling = Sampling.REGULAR
  canonical_name = "synchronization"
  section = "timing"
  units = None

  @staticmethod
  def validate(value) -> bool:
    """
    The parameter shall contain the required valid fields.
    """
    if not isinstance(value, Synchronization):
      return False
    if not (isinstance(value.frequency, float) and value.frequency > 0.0):
      return False
    if not isinstance(value.locked, bool):
      return False
    if not isinstance(value.source, SynchronizationSourceEnum):
      return False
    # Validate MAC address
    if value.ptp_master != None and not (isinstance(value.ptp_master,str) and 
                                         re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$",
                                                  value.ptp_master.lower())):
      return False
    if value.ptp_offset != None and not isinstance(value.ptp_offset, float):
      return False
    if value.ptp_domain != None and not (isinstance(value.ptp_domain, int) and value.ptp_domain >= 0):
      return False
    if value.offsets != None and not value.offsets.validate():
      return False
    if value.enabled != None and not isinstance(value.enabled, bool):
      return False

    return True

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    d = {k: v for k, v in dataclasses.asdict(value).items() if v is not None}
    d["source"] = str(d["source"])
    return d

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    return Synchronization(**value)

  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "object",
      "additionalProperties": False,
      "properties": {
        "frequency": { "type": "number", "minimum": 0.0 },
        "locked": { "type": "boolean" },
        "source": { "type": "string", "enum": [e.value for e in SynchronizationSourceEnum] },
        "ptp_master": { "type": "string", "pattern": "^([A-F0-9]{2}:){5}[A-F0-9]{2}$" },
        "ptp_offset": { "type": "number" },
        "ptp_domain": { "type": "integer", "minimum": 0 },
        "offsets": {
          "type": "object",
          "additionalProperties": False,
          "properties": {
            "translation": { "type": "number" },
            "rotation": { "type": "number" },
            "encoders": { "type": "number" }
          }
        },
        "enabled": { "type": "boolean" }
      },
      "required": ["frequency", "locked", "source"]
    }

class LensEncoders(Parameter):
  """
  TODO doc
  """
  sampling = Sampling.REGULAR
  canonical_name = "encoders"
  section = "lens"
  units = None

  @staticmethod
  def validate(value) -> bool:
    """
    The parameter shall contain at least one normalised values (0..1) for the FIZ encoders.
    """
    if not isinstance(value, Encoders):
      return False
    if value.focus == None and value.iris == None and value.zoom == None:
      return False
    for test in [value.focus, value.iris, value.zoom]:
      if test != None and not (isinstance(test, float) and test >= 0.0 and test <= 1.0):
        return False
    return True

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    return {k: v for k, v in dataclasses.asdict(value).items() if v is not None}

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    return Encoders(**value)

  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "object",
      "additionalProperties": False,
      "properties": {
        "focus": {
          "type": "number",
          "minimum": 0.0,
          "maximum": 1.0
        },
        "iris": {
          "type": "number",
          "minimum": 0.0,
          "maximum": 1.0
        },
        "zoom": {
          "type": "number",
          "minimum": 0.0,
          "maximum": 1.0
        }
      },
      "anyOf": [ {"required": ["focus"]}, {"required": ["iris"]}, {"required": ["zoom"]}
      ]
    }
  
class TimingMode(EnumParameter):
  """
  'external' timing mode describes the case where the transport packet has inherent timing, so no explicit timing data is required in the data).
  'internal' mode indicates the transport packet does not have inherent timing, so a PTP timestamp must be provided.
  """
  sampling = Sampling.REGULAR
  canonical_name = "mode"
  section = "timing"
  units = None

class TimingTimestamp(Parameter):
  """
  TODO doc
  """
  sampling = Sampling.REGULAR
  canonical_name = "timestamp"
  section = "timing"
  units = None

  @staticmethod
  def validate(value) -> bool:
    """
    The parameter shall contain valid number of seconds, nanoseconds and optionally
    attoseconds elapsed since the start of the epoch.
    """
    if not isinstance(value, Timestamp):
      return False
    if not (isinstance(value.seconds, int) and value.seconds >= 0 and value.seconds <= UINT48_MAX):
      return False
    if not (isinstance(value.nanoseconds, int) and value.nanoseconds >= 0 and value.nanoseconds <= UINT_MAX):
      return False
    if value.attoseconds != None:
      if not (isinstance(value.attoseconds, int) and value.attoseconds >= 0 and value.attoseconds <= UINT_MAX):
        return False
    return True

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    d = dataclasses.asdict(value)
    if d["attoseconds"] == None:
      del d["attoseconds"]
    return d

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    return Timestamp(**value)

  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "object",
      "additionalProperties": False,
      "properties": {
        "seconds": {
          "type": "integer",
          "minimum": 0,
          "maximum": UINT48_MAX
        },
        "nanoseconds": {
          "type": "integer",
          "minimum": 0,
          "maximum": UINT_MAX
        },
        "attoseconds": {
          "type": "integer",
          "minimum": 0,
          "maximum": UINT_MAX
        }
      },
      "required": ["seconds", "nanoseconds"]
    }

class TimingSequenceNumber(NonNegativeIntegerParameter):
  """
  TODO doc
  """
  sampling = Sampling.REGULAR
  canonical_name = "sequence_number"
  section = "timing"
  units = None

class TimingFrameRate(NonNegativeRealParameter):
  """
  TODO doc
  """
  sampling = Sampling.REGULAR
  canonical_name = "frameRate"
  section = "timing"
  units = None

class TimingTimecode(Parameter):
  """
  TODO doc
  """
  sampling = Sampling.REGULAR
  canonical_name = "timecode"
  section = "timing"
  units = None

  @staticmethod
  def validate(value) -> bool:
    """
    The parameter shall contain a valid format and hours, minutes, seconds and frames with
    appropriate min/max values.
    """

    if not isinstance(value, Timecode):
      return False
    if not isinstance(value.format, TimecodeFormat):
      return False
    if not (isinstance(value.hours, int) and value.hours >= 0 and value.hours < 24):
      return False
    if not (isinstance(value.minutes, int) and value.minutes >= 0 and value.minutes < 60):
      return False
    if not (isinstance(value.seconds, int) and value.seconds >= 0 and value.seconds < 60):
      return False
    if not (isinstance(value.frames, int) and value.frames >= 0 and value.frames < TimecodeFormat.to_int(value.format)):
      return False
    return True

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    d = dataclasses.asdict(value)
    d["format"] = str(d["format"])
    return d

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    return Timecode(value["hours"], value["minutes"], value["seconds"], value["frames"],
                    TimecodeFormat.from_string(value["format"]))

  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "object",
      "additionalProperties": False,
      "properties": {
        "hours": {
          "type": "integer",
          "minimum": 0,
          "maximum": 23
        },
        "minutes": {
          "type": "integer",
          "minimum": 0,
          "maximum": 59
        },
        "seconds": {
          "type": "integer",
          "minimum": 0,
          "maximum": 59
        },
        "frames": {
          "type": "integer",
          "minimum": 0,
          "maximum": 29
        },
        "format": {
          "type": "string",
          "enum": ["24", "24D", "25", "30", "30D"]
        }
      }
    }


class LensFoVScale(Parameter):
  """Scaling factor on horizontal and vertical field-of-view for tweaking lens calibrations"""

  sampling = Sampling.REGULAR
  canonical_name = "fovScale"
  section = "lens"
  units = None

  @staticmethod
  def validate(value) -> bool:
    """The horizontal and vertical measurements shall be each be a real non-negative number."""

    if not isinstance(value, Orientations):
      return False

    if not isinstance(value.horizontal, numbers.Real) or not isinstance(value.vertical, numbers.Real):
      return False

    if value.horizontal < 0.0 or value.vertical < 0.0:
      return False

    return True

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    return dataclasses.asdict(value)

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    return Orientations(**value)

  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "object",
      "additionalProperties": False,
      "required": [
          "horizontal",
          "vertical"
      ],
      "properties": {
        "horizontal": {
            "type": "number",
            "minimum": 0.0
        },
        "vertical": {
            "type": "number",
            "minimum": 0.0
        }
      }
    }
  
class LensExposureFalloff(Parameter):
  """Coefficients for calculating the exposure fall-off (vignetting) of a lens"""

  sampling = Sampling.REGULAR
  canonical_name = "exposureFalloff"
  section = "lens"
  units = None

  @staticmethod
  def validate(value) -> bool:
    """The coefficients shall each be real numbers."""

    if not isinstance(value, ExposureFalloff):
      return False
 
    # a1 is required
    if value.a1 == None:
      return False

    for v in [value.a1, value.a2, value.a3]:
      if v is not None and not isinstance(v, numbers.Real):
        return False

    return True

  @staticmethod
  def to_json(value: typing.Any) -> typing.Any:
    return dataclasses.asdict(value)

  @staticmethod
  def from_json(value: typing.Any) -> typing.Any:
    return ExposureFalloff(**value)

  @staticmethod
  def make_json_schema() -> dict:
    return {
      "type": "object",
      "additionalProperties": False,
      "required": ["a1"],
      "properties": {
        "a1": {
            "type": "number"
        },
        "a2": {
            "type": "number"
        },
        "a3": {
            "type": "number"
        }
      }
    }

class Clip(ParameterContainer):
  """Metadata for a camera clip.
  """
  duration: typing.Optional[numbers.Rational] = Duration()
  capture_fps: typing.Optional[numbers.Rational] = CaptureFPS()
  active_sensor_physical_dimensions: typing.Optional[Dimensions] = ActiveSensorPhysicalDimensions()
  lens_make: typing.Optional[str] = LensMake()
  lens_model: typing.Optional[str] = LensModel()
  lens_serial_number: typing.Optional[str] = LensSerialNumber()
  lens_firmware: typing.Optional[str] = LensFirmware()
  camera_make: typing.Optional[str] = CameraMake()
  camera_model: typing.Optional[str] = CameraModel()
  camera_firmware: typing.Optional[str] = CameraFirmware()
  camera_serial_number: typing.Optional[str] = CameraSerialNumber()
  iso: typing.Optional[numbers.Integral] = ISO()
  t_number: typing.Optional[typing.Tuple[numbers.Integral]] = TStop()
  f_number: typing.Optional[typing.Tuple[numbers.Integral]] = FStop()
  focal_length: typing.Optional[typing.Tuple[numbers.Integral]] = FocalLength()
  focus_position: typing.Optional[typing.Tuple[numbers.Integral]] = FocusPosition()
  entrance_pupil_position: typing.Optional[typing.Tuple[numbers.Rational]] = EntrancePupilPosition()
  anamorphic_squeeze: typing.Optional[numbers.Rational] = AnamorphicSqueeze()
  fdl_link: typing.Optional[str] = FDLLink()
  shutter_angle: typing.Optional[numbers.Integral] = ShutterAngle()
  # TODO JU rest of the tracking model! Also re-order sensibly
  packet_id: typing.Optional[typing.Tuple[str]] = PacketId()
  protocol: typing.Optional[typing.Tuple[str]] = Protocol()
  metadata_status: typing.Optional[typing.Tuple[str]] = MetadataStatus()
  metadata_recording: typing.Optional[typing.Tuple[bool]] = MetadataRecording()
  metadata_slate: typing.Optional[typing.Tuple[str]] = MetadataSlate()
  metadata_notes: typing.Optional[typing.Tuple[str]] = MetadataNotes()
  metadata_related_packets: typing.Optional[typing.Tuple[tuple]] = MetadataRelatedPackets()
  timing_mode: typing.Optional[typing.Tuple[TimingMode]] = TimingMode()
  timing_timestamp: typing.Optional[typing.Tuple[TimingTimestamp]] = TimingTimestamp()
  timing_sequence_number: typing.Optional[typing.Tuple[NonNegativeIntegerParameter]] = TimingSequenceNumber()
  timing_frame_rate: typing.Optional[typing.Tuple[NonNegativeRealParameter]] = TimingFrameRate()
  timing_timecode: typing.Optional[typing.Tuple[TimingTimecode]] = TimingTimecode()
  timing_synchronization: typing.Optional[typing.Tuple[Synchronization]] = TimingSynchronization()
  transforms: typing.Optional[typing.Tuple[Transforms]] = Transforms()
  lens_encoders: typing.Optional[typing.Tuple[LensEncoders]] = LensEncoders()
  lens_fov_scale: typing.Optional[typing.Tuple[Orientations]] = LensFoVScale()
  lens_exposure_falloff: typing.Optional[typing.Tuple[Orientations]] = LensExposureFalloff()


  def append(self, clip):
    "Helper to add another clip's parameters to this clip's REGULAR data tuples"
    if not isinstance(clip, Clip):
      raise ValueError
    for prop, desc in self._params.items():
      if clip._values[prop] != None and desc.sampling == Sampling.REGULAR:
        self._values[prop] += clip._values[prop]

  def __getitem__(self, i):
    "Helper to convert to a single STATIC data frame for JSON output"
    clip = Clip()
    for f in dir(self):
      desc = getattr(self, f)
      if not isinstance(desc, tuple):
        continue
      setattr(clip, f, desc[i])
    return clip
  
  @classmethod
  def make_static_json_schema(cls) -> dict:
    "Helper to create a static json schema representation of a single frame"
    # Remove all the existing STATIC parameters and make the REGULAR parameters STATIC
    for prop, desc in cls._params.copy().items():
      if desc.sampling == Sampling.STATIC:
        del cls._params[prop]
        continue
      desc.sampling = Sampling.STATIC
    return super().make_json_schema()
  