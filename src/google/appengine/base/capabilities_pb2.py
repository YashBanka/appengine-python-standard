#!/usr/bin/env python
#
# Copyright 2007 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#





"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    1,
    '',
    'google/appengine/base/capabilities.proto'
)


_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/appengine/base/capabilities.proto\x12\x10google.appengine\"\x86\x01\n\x14\x43\x61pabilityConfigList\x12\x32\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\".google.appengine.CapabilityConfig\x12:\n\x0e\x64\x65\x66\x61ult_config\x18\x02 \x01(\x0b\x32\".google.appengine.CapabilityConfig\"\xa9\x02\n\x10\x43\x61pabilityConfig\x12\x0f\n\x07package\x18\x01 \x01(\t\x12\x12\n\ncapability\x18\x02 \x01(\t\x12\x42\n\x06status\x18\x03 \x01(\x0e\x32).google.appengine.CapabilityConfig.Status:\x07UNKNOWN\x12\x16\n\x0escheduled_time\x18\x07 \x01(\t\x12\x18\n\x10internal_message\x18\x04 \x01(\t\x12\x15\n\radmin_message\x18\x05 \x01(\t\x12\x15\n\rerror_message\x18\x06 \x01(\t\"L\n\x06Status\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\r\n\tSCHEDULED\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04\x42:\n%com.google.appengine.api.capabilitiesB\x0e\x43\x61pabilitiesPb\xf8\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.base.capabilities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.appengine.api.capabilitiesB\016CapabilitiesPb\370\001\001'
  _globals['_CAPABILITYCONFIGLIST']._serialized_start=63
  _globals['_CAPABILITYCONFIGLIST']._serialized_end=197
  _globals['_CAPABILITYCONFIG']._serialized_start=200
  _globals['_CAPABILITYCONFIG']._serialized_end=497
  _globals['_CAPABILITYCONFIG_STATUS']._serialized_start=421
  _globals['_CAPABILITYCONFIG_STATUS']._serialized_end=497

