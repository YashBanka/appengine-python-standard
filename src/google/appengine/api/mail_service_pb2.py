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
    'google/appengine/api/mail_service.proto'
)


_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/appengine/api/mail_service.proto\x12\x10google.appengine\"\xb4\x01\n\x10MailServiceError\"\x9f\x01\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x02\x12\x17\n\x13UNAUTHORIZED_SENDER\x10\x03\x12\x1b\n\x17INVALID_ATTACHMENT_TYPE\x10\x04\x12\x17\n\x13INVALID_HEADER_NAME\x10\x05\x12\x16\n\x12INVALID_CONTENT_ID\x10\x06\"i\n\x0eMailAttachment\x12\x10\n\x08\x46ileName\x18\x01 \x01(\t\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\x0c\x12\x11\n\tContentID\x18\x03 \x01(\t\x12$\n\x18\x44\x45PRECATED_ContentID_set\x18\r \x01(\x08\x42\x02\x18\x01\")\n\nMailHeader\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x81\x02\n\x0bMailMessage\x12\x0e\n\x06Sender\x18\x01 \x01(\t\x12\x0f\n\x07ReplyTo\x18\x02 \x01(\t\x12\n\n\x02To\x18\x03 \x03(\t\x12\n\n\x02\x43\x63\x18\x04 \x03(\t\x12\x0b\n\x03\x42\x63\x63\x18\x05 \x03(\t\x12\x0f\n\x07Subject\x18\x06 \x01(\t\x12\x10\n\x08TextBody\x18\x07 \x01(\t\x12\x10\n\x08HtmlBody\x18\x08 \x01(\t\x12\x13\n\x0b\x41mpHtmlBody\x18\x0b \x01(\t\x12\x34\n\nAttachment\x18\t \x03(\x0b\x32 .google.appengine.MailAttachment\x12,\n\x06Header\x18\n \x03(\x0b\x32\x1c.google.appengine.MailHeaderB.\n\x1d\x63om.google.appengine.api.mailB\rMailServicePb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.api.mail_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.google.appengine.api.mailB\rMailServicePb'
  _globals['_MAILATTACHMENT'].fields_by_name['DEPRECATED_ContentID_set']._loaded_options = None
  _globals['_MAILATTACHMENT'].fields_by_name['DEPRECATED_ContentID_set']._serialized_options = b'\030\001'
  _globals['_MAILSERVICEERROR']._serialized_start=62
  _globals['_MAILSERVICEERROR']._serialized_end=242
  _globals['_MAILSERVICEERROR_ERRORCODE']._serialized_start=83
  _globals['_MAILSERVICEERROR_ERRORCODE']._serialized_end=242
  _globals['_MAILATTACHMENT']._serialized_start=244
  _globals['_MAILATTACHMENT']._serialized_end=349
  _globals['_MAILHEADER']._serialized_start=351
  _globals['_MAILHEADER']._serialized_end=392
  _globals['_MAILMESSAGE']._serialized_start=395
  _globals['_MAILMESSAGE']._serialized_end=652

