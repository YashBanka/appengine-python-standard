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
    'google/appengine/api/taskqueue/taskqueue_service_bytes.proto'
)


_sym_db = _symbol_database.Default()


from google.appengine.datastore import datastore_v3_bytes_pb2 as google_dot_appengine_dot_datastore_dot_datastore__v3__bytes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/appengine/api/taskqueue/taskqueue_service_bytes.proto\x12\x10\x61pphosting_bytes\x1a\x33google/appengine/datastore/datastore_v3_bytes.proto\"\xa0\n\n\x15TaskQueueServiceError\"\x86\n\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x11\n\rUNKNOWN_QUEUE\x10\x01\x12\x13\n\x0fTRANSIENT_ERROR\x10\x02\x12\x12\n\x0eINTERNAL_ERROR\x10\x03\x12\x12\n\x0eTASK_TOO_LARGE\x10\x04\x12\x15\n\x11INVALID_TASK_NAME\x10\x05\x12\x16\n\x12INVALID_QUEUE_NAME\x10\x06\x12\x0f\n\x0bINVALID_URL\x10\x07\x12\x16\n\x12INVALID_QUEUE_RATE\x10\x08\x12\x15\n\x11PERMISSION_DENIED\x10\t\x12\x17\n\x13TASK_ALREADY_EXISTS\x10\n\x12\x13\n\x0fTOMBSTONED_TASK\x10\x0b\x12\x0f\n\x0bINVALID_ETA\x10\x0c\x12\x13\n\x0fINVALID_REQUEST\x10\r\x12\x10\n\x0cUNKNOWN_TASK\x10\x0e\x12\x14\n\x10TOMBSTONED_QUEUE\x10\x0f\x12\x17\n\x13\x44UPLICATE_TASK_NAME\x10\x10\x12\x0b\n\x07SKIPPED\x10\x11\x12\x12\n\x0eTOO_MANY_TASKS\x10\x12\x12\x13\n\x0fINVALID_PAYLOAD\x10\x13\x12\x1c\n\x18INVALID_RETRY_PARAMETERS\x10\x14\x12\x16\n\x12INVALID_QUEUE_MODE\x10\x15\x12\x14\n\x10\x41\x43L_LOOKUP_ERROR\x10\x16\x12#\n\x1fTRANSACTIONAL_REQUEST_TOO_LARGE\x10\x17\x12\x1a\n\x16INCORRECT_CREATOR_NAME\x10\x18\x12\x16\n\x12TASK_LEASE_EXPIRED\x10\x19\x12\x10\n\x0cQUEUE_PAUSED\x10\x1a\x12\x0f\n\x0bINVALID_TAG\x10\x1b\x12\x1a\n\x16INVALID_LOGGING_CONFIG\x10\x1c\x12\x1d\n\x19INVALID_DISPATCH_DEADLINE\x10\x1d\x12\x14\n\x0f\x44\x41TASTORE_ERROR\x10\x90N\x12\x1a\n\x15\x44\x41TASTORE_BAD_REQUEST\x10\x91N\x12%\n DATASTORE_CONCURRENT_TRANSACTION\x10\x92N\x12\x1d\n\x18\x44\x41TASTORE_INTERNAL_ERROR\x10\x93N\x12\x19\n\x14\x44\x41TASTORE_NEED_INDEX\x10\x94N\x12\x16\n\x11\x44\x41TASTORE_TIMEOUT\x10\x95N\x12 \n\x1b\x44\x41TASTORE_PERMISSION_DENIED\x10\x96N\x12\x1d\n\x18\x44\x41TASTORE_BIGTABLE_ERROR\x10\x97N\x12+\n&DATASTORE_COMMITTED_BUT_STILL_APPLYING\x10\x98N\x12\"\n\x1d\x44\x41TASTORE_CAPABILITY_DISABLED\x10\x99N\x12$\n\x1f\x44\x41TASTORE_TRY_ALTERNATE_BACKEND\x10\x9aN\x12 \n\x1b\x44\x41TASTORE_SAFE_TIME_TOO_OLD\x10\x9bN\x12!\n\x1c\x44\x41TASTORE_RESOURCE_EXHAUSTED\x10\x9cN\x12\x18\n\x13\x44\x41TASTORE_NOT_FOUND\x10\x9dN\x12\x1d\n\x18\x44\x41TASTORE_ALREADY_EXISTS\x10\x9eN\x12\"\n\x1d\x44\x41TASTORE_FAILED_PRECONDITION\x10\x9fN\x12\x1e\n\x19\x44\x41TASTORE_UNAUTHENTICATED\x10\xa0N\x12\x16\n\x11\x44\x41TASTORE_ABORTED\x10\xa1N\x12\'\n\"DATASTORE_SNAPSHOT_VERSION_TOO_OLD\x10\xa2N\"\x1b\n\x0bTaskPayload*\x08\x08\n\x10\xff\xff\xff\xff\x07:\x02\x08\x01\"\x9e\x01\n\x18TaskQueueRetryParameters\x12\x13\n\x0bretry_limit\x18\x01 \x01(\x05\x12\x15\n\rage_limit_sec\x18\x02 \x01(\x03\x12\x1c\n\x0fmin_backoff_sec\x18\x03 \x01(\x01:\x03\x30.1\x12\x1d\n\x0fmax_backoff_sec\x18\x04 \x01(\x01:\x04\x33\x36\x30\x30\x12\x19\n\rmax_doublings\x18\x05 \x01(\x05:\x02\x31\x36\"8\n\x0cTaskQueueAcl\x12\x12\n\nuser_email\x18\x01 \x03(\x0c\x12\x14\n\x0cwriter_email\x18\x02 \x03(\x0c\"1\n\x13TaskQueueHttpHeader\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"+\n\rTaskQueueMode\"\x1a\n\x04Mode\x12\x08\n\x04PUSH\x10\x00\x12\x08\n\x04PULL\x10\x01\"\x87\x07\n\x13TaskQueueAddRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\x0c\x12\x11\n\ttask_name\x18\x02 \x01(\x0c\x12\x10\n\x08\x65ta_usec\x18\x03 \x01(\x03\x12I\n\x06method\x18\x05 \x01(\x0e\x32\x33.apphosting_bytes.TaskQueueAddRequest.RequestMethod:\x04POST\x12\x0b\n\x03url\x18\x04 \x01(\x0c\x12<\n\x06header\x18\x06 \x03(\n2,.apphosting_bytes.TaskQueueAddRequest.Header\x12\x10\n\x04\x62ody\x18\t \x01(\x0c\x42\x02\x08\x01\x12?\n\x0btransaction\x18\n \x01(\x0b\x32*.apphosting_datastore_v3_bytes.Transaction\x12\x1d\n\x15\x64\x61tastore_transaction\x18\x15 \x01(\x0c\x12\x0e\n\x06\x61pp_id\x18\x0b \x01(\x0c\x12J\n\rcrontimetable\x18\x0c \x01(\n23.apphosting_bytes.TaskQueueAddRequest.CronTimetable\x12\x13\n\x0b\x64\x65scription\x18\x0f \x01(\x0c\x12.\n\x07payload\x18\x10 \x01(\x0b\x32\x1d.apphosting_bytes.TaskPayload\x12\x44\n\x10retry_parameters\x18\x11 \x01(\x0b\x32*.apphosting_bytes.TaskQueueRetryParameters\x12\x32\n\x04mode\x18\x12 \x01(\x0e\x32$.apphosting_bytes.TaskQueueMode.Mode\x12\x0b\n\x03tag\x18\x13 \x01(\x0c\x12I\n\x15\x63ron_retry_parameters\x18\x14 \x01(\x0b\x32*.apphosting_bytes.TaskQueueRetryParameters\x12\x1e\n\x16\x64ispatch_deadline_usec\x18\x16 \x01(\x03\x1a$\n\x06Header\x12\x0b\n\x03key\x18\x07 \x01(\x0c\x12\r\n\x05value\x18\x08 \x01(\x0c\x1a\x33\n\rCronTimetable\x12\x10\n\x08schedule\x18\r \x01(\x0c\x12\x10\n\x08timezone\x18\x0e \x01(\x0c\"A\n\rRequestMethod\x12\x07\n\x03GET\x10\x01\x12\x08\n\x04POST\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\"0\n\x14TaskQueueAddResponse\x12\x18\n\x10\x63hosen_task_name\x18\x01 \x01(\x0c\"U\n\x17TaskQueueBulkAddRequest\x12:\n\x0b\x61\x64\x64_request\x18\x01 \x03(\x0b\x32%.apphosting_bytes.TaskQueueAddRequest\"\xd0\x01\n\x18TaskQueueBulkAddResponse\x12I\n\ntaskresult\x18\x01 \x03(\n25.apphosting_bytes.TaskQueueBulkAddResponse.TaskResult\x1ai\n\nTaskResult\x12\x41\n\x06result\x18\x02 \x01(\x0e\x32\x31.apphosting_bytes.TaskQueueServiceError.ErrorCode\x12\x18\n\x10\x63hosen_task_name\x18\x03 \x01(\x0c\"O\n\x16TaskQueueDeleteRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\x0c\x12\x11\n\ttask_name\x18\x02 \x03(\x0c\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\x0c\"\\\n\x17TaskQueueDeleteResponse\x12\x41\n\x06result\x18\x03 \x03(\x0e\x32\x31.apphosting_bytes.TaskQueueServiceError.ErrorCode\"Q\n\x18TaskQueueForceRunRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\x12\x11\n\ttask_name\x18\x03 \x01(\x0c\"^\n\x19TaskQueueForceRunResponse\x12\x41\n\x06result\x18\x03 \x01(\x0e\x32\x31.apphosting_bytes.TaskQueueServiceError.ErrorCode\"\xa1\x03\n\x1bTaskQueueUpdateQueueRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\x12 \n\x18\x62ucket_refill_per_second\x18\x03 \x01(\x01\x12\x17\n\x0f\x62ucket_capacity\x18\x04 \x01(\x05\x12\x1b\n\x13user_specified_rate\x18\x05 \x01(\t\x12\x44\n\x10retry_parameters\x18\x06 \x01(\x0b\x32*.apphosting_bytes.TaskQueueRetryParameters\x12\x1f\n\x17max_concurrent_requests\x18\x07 \x01(\x05\x12\x32\n\x04mode\x18\x08 \x01(\x0e\x32$.apphosting_bytes.TaskQueueMode.Mode\x12+\n\x03\x61\x63l\x18\t \x01(\x0b\x32\x1e.apphosting_bytes.TaskQueueAcl\x12>\n\x0fheader_override\x18\n \x03(\x0b\x32%.apphosting_bytes.TaskQueueHttpHeader\"\x1e\n\x1cTaskQueueUpdateQueueResponse\"?\n\x1bTaskQueueFetchQueuesRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x10\n\x08max_rows\x18\x02 \x01(\x05\"\x97\x04\n\x1cTaskQueueFetchQueuesResponse\x12\x43\n\x05queue\x18\x01 \x03(\n24.apphosting_bytes.TaskQueueFetchQueuesResponse.Queue\x1a\xb1\x03\n\x05Queue\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\x12 \n\x18\x62ucket_refill_per_second\x18\x03 \x01(\x01\x12\x17\n\x0f\x62ucket_capacity\x18\x04 \x01(\x01\x12\x1b\n\x13user_specified_rate\x18\x05 \x01(\t\x12\x0e\n\x06paused\x18\x06 \x01(\x08\x12\x44\n\x10retry_parameters\x18\x07 \x01(\x0b\x32*.apphosting_bytes.TaskQueueRetryParameters\x12\x1f\n\x17max_concurrent_requests\x18\x08 \x01(\x05\x12\x32\n\x04mode\x18\t \x01(\x0e\x32$.apphosting_bytes.TaskQueueMode.Mode\x12+\n\x03\x61\x63l\x18\n \x01(\x0b\x32\x1e.apphosting_bytes.TaskQueueAcl\x12>\n\x0fheader_override\x18\x0b \x03(\x0b\x32%.apphosting_bytes.TaskQueueHttpHeader\x12$\n\x0c\x63reator_name\x18\x0c \x01(\t:\napphostingB\x02\x08\x01\"\\\n\x1fTaskQueueFetchQueueStatsRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x03(\x0c\x12\x15\n\rmax_num_tasks\x18\x03 \x01(\x05\"\xab\x01\n\x19TaskQueueScannerQueueInfo\x12\x1c\n\x14\x65xecuted_last_minute\x18\x01 \x01(\x03\x12\x1a\n\x12\x65xecuted_last_hour\x18\x02 \x01(\x03\x12!\n\x19sampling_duration_seconds\x18\x03 \x01(\x01\x12\x1a\n\x12requests_in_flight\x18\x04 \x01(\x05\x12\x15\n\renforced_rate\x18\x05 \x01(\x01\"\xf2\x01\n TaskQueueFetchQueueStatsResponse\x12Q\n\nqueuestats\x18\x01 \x03(\n2=.apphosting_bytes.TaskQueueFetchQueueStatsResponse.QueueStats\x1a{\n\nQueueStats\x12\x11\n\tnum_tasks\x18\x02 \x01(\x05\x12\x17\n\x0foldest_eta_usec\x18\x03 \x01(\x03\x12\x41\n\x0cscanner_info\x18\x04 \x01(\x0b\x32+.apphosting_bytes.TaskQueueScannerQueueInfo\"O\n\x1aTaskQueuePauseQueueRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\x12\r\n\x05pause\x18\x03 \x01(\x08\"\x1d\n\x1bTaskQueuePauseQueueResponse\"@\n\x1aTaskQueuePurgeQueueRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\"\x1d\n\x1bTaskQueuePurgeQueueResponse\"A\n\x1bTaskQueueDeleteQueueRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\"\x1e\n\x1cTaskQueueDeleteQueueResponse\"-\n\x1bTaskQueueDeleteGroupRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\"\x1e\n\x1cTaskQueueDeleteGroupResponse\"\x99\x01\n\x1aTaskQueueQueryTasksRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\x12\x17\n\x0fstart_task_name\x18\x03 \x01(\x0c\x12\x16\n\x0estart_eta_usec\x18\x04 \x01(\x03\x12\x11\n\tstart_tag\x18\x06 \x01(\x0c\x12\x13\n\x08max_rows\x18\x05 \x01(\x05:\x01\x31\"\xb0\x08\n\x1bTaskQueueQueryTasksResponse\x12@\n\x04task\x18\x01 \x03(\n22.apphosting_bytes.TaskQueueQueryTasksResponse.Task\x1a\xce\x07\n\x04Task\x12\x11\n\ttask_name\x18\x02 \x01(\x0c\x12\x10\n\x08\x65ta_usec\x18\x03 \x01(\x03\x12\x0b\n\x03url\x18\x04 \x01(\x0c\x12P\n\x06method\x18\x05 \x01(\x0e\x32@.apphosting_bytes.TaskQueueQueryTasksResponse.Task.RequestMethod\x12\x13\n\x0bretry_count\x18\x06 \x01(\x05\x12I\n\x06header\x18\x07 \x03(\n29.apphosting_bytes.TaskQueueQueryTasksResponse.Task.Header\x12\x11\n\tbody_size\x18\n \x01(\x05\x12\x10\n\x04\x62ody\x18\x0b \x01(\x0c\x42\x02\x08\x01\x12\x1a\n\x12\x63reation_time_usec\x18\x0c \x01(\x03\x12W\n\rcrontimetable\x18\r \x01(\n2@.apphosting_bytes.TaskQueueQueryTasksResponse.Task.CronTimetable\x12I\n\x06runlog\x18\x10 \x01(\n29.apphosting_bytes.TaskQueueQueryTasksResponse.Task.RunLog\x12\x13\n\x0b\x64\x65scription\x18\x15 \x01(\x0c\x12.\n\x07payload\x18\x16 \x01(\x0b\x32\x1d.apphosting_bytes.TaskPayload\x12\x44\n\x10retry_parameters\x18\x17 \x01(\x0b\x32*.apphosting_bytes.TaskQueueRetryParameters\x12\x16\n\x0e\x66irst_try_usec\x18\x18 \x01(\x03\x12\x0b\n\x03tag\x18\x19 \x01(\x0c\x12\x17\n\x0f\x65xecution_count\x18\x1a \x01(\x05\x12\x1e\n\x16\x64ispatch_deadline_usec\x18\x1c \x01(\x03\x1a$\n\x06Header\x12\x0b\n\x03key\x18\x08 \x01(\x0c\x12\r\n\x05value\x18\t \x01(\x0c\x1a\x33\n\rCronTimetable\x12\x10\n\x08schedule\x18\x0e \x01(\x0c\x12\x10\n\x08timezone\x18\x0f \x01(\x0c\x1av\n\x06RunLog\x12\x17\n\x0f\x64ispatched_usec\x18\x11 \x01(\x03\x12\x10\n\x08lag_usec\x18\x12 \x01(\x03\x12\x14\n\x0c\x65lapsed_usec\x18\x13 \x01(\x03\x12\x15\n\rresponse_code\x18\x14 \x01(\x03\x12\x14\n\x0cretry_reason\x18\x1b \x01(\t\"A\n\rRequestMethod\x12\x07\n\x03GET\x10\x01\x12\x08\n\x04POST\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\"R\n\x19TaskQueueFetchTaskRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\x12\n\nqueue_name\x18\x02 \x01(\x0c\x12\x11\n\ttask_name\x18\x03 \x01(\x0c\"Y\n\x1aTaskQueueFetchTaskResponse\x12;\n\x04task\x18\x01 \x01(\x0b\x32-.apphosting_bytes.TaskQueueQueryTasksResponse\"C\n\"TaskQueueUpdateStorageLimitRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x0c\x12\r\n\x05limit\x18\x02 \x01(\x03\"8\n#TaskQueueUpdateStorageLimitResponse\x12\x11\n\tnew_limit\x18\x01 \x01(\x03\"\x83\x01\n TaskQueueQueryAndOwnTasksRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\x0c\x12\x15\n\rlease_seconds\x18\x02 \x01(\x01\x12\x11\n\tmax_tasks\x18\x03 \x01(\x03\x12\x14\n\x0cgroup_by_tag\x18\x04 \x01(\x08\x12\x0b\n\x03tag\x18\x05 \x01(\x0c\"\xcc\x01\n!TaskQueueQueryAndOwnTasksResponse\x12\x46\n\x04task\x18\x01 \x03(\n28.apphosting_bytes.TaskQueueQueryAndOwnTasksResponse.Task\x1a_\n\x04Task\x12\x11\n\ttask_name\x18\x02 \x01(\x0c\x12\x10\n\x08\x65ta_usec\x18\x03 \x01(\x03\x12\x13\n\x0bretry_count\x18\x04 \x01(\x05\x12\x10\n\x04\x62ody\x18\x05 \x01(\x0c\x42\x02\x08\x01\x12\x0b\n\x03tag\x18\x06 \x01(\x0c\"q\n\x1fTaskQueueModifyTaskLeaseRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\x0c\x12\x11\n\ttask_name\x18\x02 \x01(\x0c\x12\x10\n\x08\x65ta_usec\x18\x03 \x01(\x03\x12\x15\n\rlease_seconds\x18\x04 \x01(\x01\"<\n TaskQueueModifyTaskLeaseResponse\x12\x18\n\x10updated_eta_usec\x18\x01 \x01(\x03\x42`\n,com.google.appengine.api.taskqueue.proto1apiB\x0bTaskQueuePb\x9a\x01\"com.google.appengine.api.taskqueue')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.api.taskqueue.taskqueue_service_bytes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.appengine.api.taskqueue.proto1apiB\013TaskQueuePb\232\001\"com.google.appengine.api.taskqueue'
  _globals['_TASKPAYLOAD']._loaded_options = None
  _globals['_TASKPAYLOAD']._serialized_options = b'\010\001'
  _globals['_TASKQUEUEADDREQUEST'].fields_by_name['body']._loaded_options = None
  _globals['_TASKQUEUEADDREQUEST'].fields_by_name['body']._serialized_options = b'\010\001'
  _globals['_TASKQUEUEFETCHQUEUESRESPONSE_QUEUE'].fields_by_name['creator_name']._loaded_options = None
  _globals['_TASKQUEUEFETCHQUEUESRESPONSE_QUEUE'].fields_by_name['creator_name']._serialized_options = b'\010\001'
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK'].fields_by_name['body']._loaded_options = None
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK'].fields_by_name['body']._serialized_options = b'\010\001'
  _globals['_TASKQUEUEQUERYANDOWNTASKSRESPONSE_TASK'].fields_by_name['body']._loaded_options = None
  _globals['_TASKQUEUEQUERYANDOWNTASKSRESPONSE_TASK'].fields_by_name['body']._serialized_options = b'\010\001'
  _globals['_TASKQUEUESERVICEERROR']._serialized_start=136
  _globals['_TASKQUEUESERVICEERROR']._serialized_end=1448
  _globals['_TASKQUEUESERVICEERROR_ERRORCODE']._serialized_start=162
  _globals['_TASKQUEUESERVICEERROR_ERRORCODE']._serialized_end=1448
  _globals['_TASKPAYLOAD']._serialized_start=1450
  _globals['_TASKPAYLOAD']._serialized_end=1477
  _globals['_TASKQUEUERETRYPARAMETERS']._serialized_start=1480
  _globals['_TASKQUEUERETRYPARAMETERS']._serialized_end=1638
  _globals['_TASKQUEUEACL']._serialized_start=1640
  _globals['_TASKQUEUEACL']._serialized_end=1696
  _globals['_TASKQUEUEHTTPHEADER']._serialized_start=1698
  _globals['_TASKQUEUEHTTPHEADER']._serialized_end=1747
  _globals['_TASKQUEUEMODE']._serialized_start=1749
  _globals['_TASKQUEUEMODE']._serialized_end=1792
  _globals['_TASKQUEUEMODE_MODE']._serialized_start=1766
  _globals['_TASKQUEUEMODE_MODE']._serialized_end=1792
  _globals['_TASKQUEUEADDREQUEST']._serialized_start=1795
  _globals['_TASKQUEUEADDREQUEST']._serialized_end=2698
  _globals['_TASKQUEUEADDREQUEST_HEADER']._serialized_start=2542
  _globals['_TASKQUEUEADDREQUEST_HEADER']._serialized_end=2578
  _globals['_TASKQUEUEADDREQUEST_CRONTIMETABLE']._serialized_start=2580
  _globals['_TASKQUEUEADDREQUEST_CRONTIMETABLE']._serialized_end=2631
  _globals['_TASKQUEUEADDREQUEST_REQUESTMETHOD']._serialized_start=2633
  _globals['_TASKQUEUEADDREQUEST_REQUESTMETHOD']._serialized_end=2698
  _globals['_TASKQUEUEADDRESPONSE']._serialized_start=2700
  _globals['_TASKQUEUEADDRESPONSE']._serialized_end=2748
  _globals['_TASKQUEUEBULKADDREQUEST']._serialized_start=2750
  _globals['_TASKQUEUEBULKADDREQUEST']._serialized_end=2835
  _globals['_TASKQUEUEBULKADDRESPONSE']._serialized_start=2838
  _globals['_TASKQUEUEBULKADDRESPONSE']._serialized_end=3046
  _globals['_TASKQUEUEBULKADDRESPONSE_TASKRESULT']._serialized_start=2941
  _globals['_TASKQUEUEBULKADDRESPONSE_TASKRESULT']._serialized_end=3046
  _globals['_TASKQUEUEDELETEREQUEST']._serialized_start=3048
  _globals['_TASKQUEUEDELETEREQUEST']._serialized_end=3127
  _globals['_TASKQUEUEDELETERESPONSE']._serialized_start=3129
  _globals['_TASKQUEUEDELETERESPONSE']._serialized_end=3221
  _globals['_TASKQUEUEFORCERUNREQUEST']._serialized_start=3223
  _globals['_TASKQUEUEFORCERUNREQUEST']._serialized_end=3304
  _globals['_TASKQUEUEFORCERUNRESPONSE']._serialized_start=3306
  _globals['_TASKQUEUEFORCERUNRESPONSE']._serialized_end=3400
  _globals['_TASKQUEUEUPDATEQUEUEREQUEST']._serialized_start=3403
  _globals['_TASKQUEUEUPDATEQUEUEREQUEST']._serialized_end=3820
  _globals['_TASKQUEUEUPDATEQUEUERESPONSE']._serialized_start=3822
  _globals['_TASKQUEUEUPDATEQUEUERESPONSE']._serialized_end=3852
  _globals['_TASKQUEUEFETCHQUEUESREQUEST']._serialized_start=3854
  _globals['_TASKQUEUEFETCHQUEUESREQUEST']._serialized_end=3917
  _globals['_TASKQUEUEFETCHQUEUESRESPONSE']._serialized_start=3920
  _globals['_TASKQUEUEFETCHQUEUESRESPONSE']._serialized_end=4455
  _globals['_TASKQUEUEFETCHQUEUESRESPONSE_QUEUE']._serialized_start=4022
  _globals['_TASKQUEUEFETCHQUEUESRESPONSE_QUEUE']._serialized_end=4455
  _globals['_TASKQUEUEFETCHQUEUESTATSREQUEST']._serialized_start=4457
  _globals['_TASKQUEUEFETCHQUEUESTATSREQUEST']._serialized_end=4549
  _globals['_TASKQUEUESCANNERQUEUEINFO']._serialized_start=4552
  _globals['_TASKQUEUESCANNERQUEUEINFO']._serialized_end=4723
  _globals['_TASKQUEUEFETCHQUEUESTATSRESPONSE']._serialized_start=4726
  _globals['_TASKQUEUEFETCHQUEUESTATSRESPONSE']._serialized_end=4968
  _globals['_TASKQUEUEFETCHQUEUESTATSRESPONSE_QUEUESTATS']._serialized_start=4845
  _globals['_TASKQUEUEFETCHQUEUESTATSRESPONSE_QUEUESTATS']._serialized_end=4968
  _globals['_TASKQUEUEPAUSEQUEUEREQUEST']._serialized_start=4970
  _globals['_TASKQUEUEPAUSEQUEUEREQUEST']._serialized_end=5049
  _globals['_TASKQUEUEPAUSEQUEUERESPONSE']._serialized_start=5051
  _globals['_TASKQUEUEPAUSEQUEUERESPONSE']._serialized_end=5080
  _globals['_TASKQUEUEPURGEQUEUEREQUEST']._serialized_start=5082
  _globals['_TASKQUEUEPURGEQUEUEREQUEST']._serialized_end=5146
  _globals['_TASKQUEUEPURGEQUEUERESPONSE']._serialized_start=5148
  _globals['_TASKQUEUEPURGEQUEUERESPONSE']._serialized_end=5177
  _globals['_TASKQUEUEDELETEQUEUEREQUEST']._serialized_start=5179
  _globals['_TASKQUEUEDELETEQUEUEREQUEST']._serialized_end=5244
  _globals['_TASKQUEUEDELETEQUEUERESPONSE']._serialized_start=5246
  _globals['_TASKQUEUEDELETEQUEUERESPONSE']._serialized_end=5276
  _globals['_TASKQUEUEDELETEGROUPREQUEST']._serialized_start=5278
  _globals['_TASKQUEUEDELETEGROUPREQUEST']._serialized_end=5323
  _globals['_TASKQUEUEDELETEGROUPRESPONSE']._serialized_start=5325
  _globals['_TASKQUEUEDELETEGROUPRESPONSE']._serialized_end=5355
  _globals['_TASKQUEUEQUERYTASKSREQUEST']._serialized_start=5358
  _globals['_TASKQUEUEQUERYTASKSREQUEST']._serialized_end=5511
  _globals['_TASKQUEUEQUERYTASKSRESPONSE']._serialized_start=5514
  _globals['_TASKQUEUEQUERYTASKSRESPONSE']._serialized_end=6586
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK']._serialized_start=5612
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK']._serialized_end=6586
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_HEADER']._serialized_start=6310
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_HEADER']._serialized_end=6346
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_CRONTIMETABLE']._serialized_start=6348
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_CRONTIMETABLE']._serialized_end=6399
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_RUNLOG']._serialized_start=6401
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_RUNLOG']._serialized_end=6519
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_REQUESTMETHOD']._serialized_start=2633
  _globals['_TASKQUEUEQUERYTASKSRESPONSE_TASK_REQUESTMETHOD']._serialized_end=2698
  _globals['_TASKQUEUEFETCHTASKREQUEST']._serialized_start=6588
  _globals['_TASKQUEUEFETCHTASKREQUEST']._serialized_end=6670
  _globals['_TASKQUEUEFETCHTASKRESPONSE']._serialized_start=6672
  _globals['_TASKQUEUEFETCHTASKRESPONSE']._serialized_end=6761
  _globals['_TASKQUEUEUPDATESTORAGELIMITREQUEST']._serialized_start=6763
  _globals['_TASKQUEUEUPDATESTORAGELIMITREQUEST']._serialized_end=6830
  _globals['_TASKQUEUEUPDATESTORAGELIMITRESPONSE']._serialized_start=6832
  _globals['_TASKQUEUEUPDATESTORAGELIMITRESPONSE']._serialized_end=6888
  _globals['_TASKQUEUEQUERYANDOWNTASKSREQUEST']._serialized_start=6891
  _globals['_TASKQUEUEQUERYANDOWNTASKSREQUEST']._serialized_end=7022
  _globals['_TASKQUEUEQUERYANDOWNTASKSRESPONSE']._serialized_start=7025
  _globals['_TASKQUEUEQUERYANDOWNTASKSRESPONSE']._serialized_end=7229
  _globals['_TASKQUEUEQUERYANDOWNTASKSRESPONSE_TASK']._serialized_start=7134
  _globals['_TASKQUEUEQUERYANDOWNTASKSRESPONSE_TASK']._serialized_end=7229
  _globals['_TASKQUEUEMODIFYTASKLEASEREQUEST']._serialized_start=7231
  _globals['_TASKQUEUEMODIFYTASKLEASEREQUEST']._serialized_end=7344
  _globals['_TASKQUEUEMODIFYTASKLEASERESPONSE']._serialized_start=7346
  _globals['_TASKQUEUEMODIFYTASKLEASERESPONSE']._serialized_end=7406

