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
    'google/appengine/api/user_service.proto'
)


_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/appengine/api/user_service.proto\x12\x10google.appengine\"\x99\x01\n\x10UserServiceError\"\x84\x01\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x19\n\x15REDIRECT_URL_TOO_LONG\x10\x01\x12\x0f\n\x0bNOT_ALLOWED\x10\x02\x12\x17\n\x13OAUTH_INVALID_TOKEN\x10\x03\x12\x19\n\x15OAUTH_INVALID_REQUEST\x10\x04\x12\x0f\n\x0bOAUTH_ERROR\x10\x05\"a\n\x15\x43reateLoginURLRequest\x12\x17\n\x0f\x64\x65stination_url\x18\x01 \x01(\t\x12\x13\n\x0b\x61uth_domain\x18\x02 \x01(\t\x12\x1a\n\x12\x66\x65\x64\x65rated_identity\x18\x03 \x01(\t\"+\n\x16\x43reateLoginURLResponse\x12\x11\n\tlogin_url\x18\x01 \x01(\t\"F\n\x16\x43reateLogoutURLRequest\x12\x17\n\x0f\x64\x65stination_url\x18\x01 \x01(\t\x12\x13\n\x0b\x61uth_domain\x18\x02 \x01(\t\"-\n\x17\x43reateLogoutURLResponse\x12\x12\n\nlogout_url\x18\x01 \x01(\t\"[\n\x13GetOAuthUserRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0e\n\x06scopes\x18\x02 \x03(\t\x12%\n\x19request_writer_permission\x18\x03 \x01(\x08\x42\x02\x18\x01\"\xba\x01\n\x14GetOAuthUserResponse\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x13\n\x0b\x61uth_domain\x18\x03 \x01(\t\x12\x19\n\x11user_organization\x18\x04 \x01(\t\x12\x10\n\x08is_admin\x18\x05 \x01(\x08\x12\x11\n\tclient_id\x18\x06 \x01(\t\x12\x0e\n\x06scopes\x18\x07 \x03(\t\x12\x1d\n\x11is_project_writer\x18\x08 \x01(\x08\x42\x02\x18\x01\x42\x30\n\x1f\x63om.google.google.appengine.apiB\rUserServicePb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.api.user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.google.google.appengine.apiB\rUserServicePb'
  _globals['_GETOAUTHUSERREQUEST'].fields_by_name['request_writer_permission']._loaded_options = None
  _globals['_GETOAUTHUSERREQUEST'].fields_by_name['request_writer_permission']._serialized_options = b'\030\001'
  _globals['_GETOAUTHUSERRESPONSE'].fields_by_name['is_project_writer']._loaded_options = None
  _globals['_GETOAUTHUSERRESPONSE'].fields_by_name['is_project_writer']._serialized_options = b'\030\001'
  _globals['_USERSERVICEERROR']._serialized_start=62
  _globals['_USERSERVICEERROR']._serialized_end=215
  _globals['_USERSERVICEERROR_ERRORCODE']._serialized_start=83
  _globals['_USERSERVICEERROR_ERRORCODE']._serialized_end=215
  _globals['_CREATELOGINURLREQUEST']._serialized_start=217
  _globals['_CREATELOGINURLREQUEST']._serialized_end=314
  _globals['_CREATELOGINURLRESPONSE']._serialized_start=316
  _globals['_CREATELOGINURLRESPONSE']._serialized_end=359
  _globals['_CREATELOGOUTURLREQUEST']._serialized_start=361
  _globals['_CREATELOGOUTURLREQUEST']._serialized_end=431
  _globals['_CREATELOGOUTURLRESPONSE']._serialized_start=433
  _globals['_CREATELOGOUTURLRESPONSE']._serialized_end=478
  _globals['_GETOAUTHUSERREQUEST']._serialized_start=480
  _globals['_GETOAUTHUSERREQUEST']._serialized_end=571
  _globals['_GETOAUTHUSERRESPONSE']._serialized_start=574
  _globals['_GETOAUTHUSERRESPONSE']._serialized_end=760

