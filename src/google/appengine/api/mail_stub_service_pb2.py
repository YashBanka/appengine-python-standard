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
    'google/appengine/api/mail_stub_service.proto'
)


_sym_db = _symbol_database.Default()


from google.appengine.api import api_base_pb2 as google_dot_appengine_dot_api_dot_api__base__pb2
from google.appengine.api import mail_service_pb2 as google_dot_appengine_dot_api_dot_mail__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/appengine/api/mail_stub_service.proto\x12\x10google.appengine\x1a#google/appengine/api/api_base.proto\x1a\'google/appengine/api/mail_service.proto\"N\n\x17GetSentMessagesResponse\x12\x33\n\x0csent_message\x18\x01 \x03(\x0b\x32\x1d.google.appengine.MailMessage\"5\n\x19\x43learSentMessagesResponse\x12\x18\n\x10messages_cleared\x18\x01 \x01(\x05\"/\n\x16GetLogMailBodyResponse\x12\x15\n\rlog_mail_body\x18\x01 \x01(\x08\".\n\x15SetLogMailBodyRequest\x12\x15\n\rlog_mail_body\x18\x01 \x01(\x08\"1\n\x17GetLogMailLevelResponse\x12\x16\n\x0elog_mail_level\x18\x01 \x01(\t\"0\n\x16SetLogMailLevelRequest\x12\x16\n\x0elog_mail_level\x18\x01 \x01(\tB2\n\x1d\x63om.google.appengine.api.mailB\x11MailStubServicePb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.api.mail_stub_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.google.appengine.api.mailB\021MailStubServicePb'
  _globals['_GETSENTMESSAGESRESPONSE']._serialized_start=144
  _globals['_GETSENTMESSAGESRESPONSE']._serialized_end=222
  _globals['_CLEARSENTMESSAGESRESPONSE']._serialized_start=224
  _globals['_CLEARSENTMESSAGESRESPONSE']._serialized_end=277
  _globals['_GETLOGMAILBODYRESPONSE']._serialized_start=279
  _globals['_GETLOGMAILBODYRESPONSE']._serialized_end=326
  _globals['_SETLOGMAILBODYREQUEST']._serialized_start=328
  _globals['_SETLOGMAILBODYREQUEST']._serialized_end=374
  _globals['_GETLOGMAILLEVELRESPONSE']._serialized_start=376
  _globals['_GETLOGMAILLEVELRESPONSE']._serialized_end=425
  _globals['_SETLOGMAILLEVELREQUEST']._serialized_start=427
  _globals['_SETLOGMAILLEVELREQUEST']._serialized_end=475

