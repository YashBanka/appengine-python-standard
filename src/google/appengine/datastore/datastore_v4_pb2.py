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
    'google/appengine/datastore/datastore_v4.proto'
)


_sym_db = _symbol_database.Default()


from google.appengine.datastore import entity_v4_pb2 as google_dot_appengine_dot_datastore_dot_entity__v4__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/appengine/datastore/datastore_v4.proto\x12\x1dgoogle.appengine.datastore.v4\x1a*google/appengine/datastore/entity_v4.proto\"\x9f\x03\n\x05\x45rror\"\x95\x03\n\tErrorCode\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x01\x12\x1a\n\x16\x43ONCURRENT_TRANSACTION\x10\x02\x12\x12\n\x0eINTERNAL_ERROR\x10\x03\x12\x0e\n\nNEED_INDEX\x10\x04\x12\x0b\n\x07TIMEOUT\x10\x05\x12\x15\n\x11PERMISSION_DENIED\x10\x06\x12\x12\n\x0e\x42IGTABLE_ERROR\x10\x07\x12 \n\x1c\x43OMMITTED_BUT_STILL_APPLYING\x10\x08\x12\x17\n\x13\x43\x41PABILITY_DISABLED\x10\t\x12\x19\n\x15TRY_ALTERNATE_BACKEND\x10\n\x12\x15\n\x11SAFE_TIME_TOO_OLD\x10\x0b\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x0c\x12\x1c\n\x18SNAPSHOT_VERSION_TOO_OLD\x10\x12\x12\r\n\tNOT_FOUND\x10\r\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x0e\x12\x17\n\x13\x46\x41ILED_PRECONDITION\x10\x0f\x12\x13\n\x0fUNAUTHENTICATED\x10\x10\x12\x0b\n\x07\x41\x42ORTED\x10\x11\"\x9c\x01\n\x0c\x45ntityResult\x12\x35\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.google.appengine.datastore.v4.Entity\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0e\n\x06\x63ursor\x18\x03 \x01(\x0c\"4\n\nResultType\x12\x08\n\x04\x46ULL\x10\x01\x12\x0e\n\nPROJECTION\x10\x02\x12\x0c\n\x08KEY_ONLY\x10\x03\"\x8f\x03\n\x05Query\x12\x45\n\nprojection\x18\x02 \x03(\x0b\x32\x31.google.appengine.datastore.v4.PropertyExpression\x12;\n\x04kind\x18\x03 \x03(\x0b\x32-.google.appengine.datastore.v4.KindExpression\x12\x35\n\x06\x66ilter\x18\x04 \x01(\x0b\x32%.google.appengine.datastore.v4.Filter\x12;\n\x05order\x18\x05 \x03(\x0b\x32,.google.appengine.datastore.v4.PropertyOrder\x12\x42\n\x08group_by\x18\x06 \x03(\x0b\x32\x30.google.appengine.datastore.v4.PropertyReference\x12\x14\n\x0cstart_cursor\x18\x07 \x01(\x0c\x12\x12\n\nend_cursor\x18\x08 \x01(\x0c\x12\x11\n\x06offset\x18\n \x01(\x05:\x01\x30\x12\r\n\x05limit\x18\x0b \x01(\x05\"\x1e\n\x0eKindExpression\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x11PropertyReference\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xdf\x01\n\x12PropertyExpression\x12\x42\n\x08property\x18\x01 \x01(\x0b\x32\x30.google.appengine.datastore.v4.PropertyReference\x12\x63\n\x14\x61ggregation_function\x18\x02 \x01(\x0e\x32\x45.google.appengine.datastore.v4.PropertyExpression.AggregationFunction\" \n\x13\x41ggregationFunction\x12\t\n\x05\x46IRST\x10\x01\"\xd5\x01\n\rPropertyOrder\x12\x42\n\x08property\x18\x01 \x01(\x0b\x32\x30.google.appengine.datastore.v4.PropertyReference\x12T\n\tdirection\x18\x02 \x01(\x0e\x32\x36.google.appengine.datastore.v4.PropertyOrder.Direction:\tASCENDING\"*\n\tDirection\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\"\x9a\x01\n\x06\x46ilter\x12H\n\x10\x63omposite_filter\x18\x01 \x01(\x0b\x32..google.appengine.datastore.v4.CompositeFilter\x12\x46\n\x0fproperty_filter\x18\x02 \x01(\x0b\x32-.google.appengine.datastore.v4.PropertyFilter\"\xa8\x01\n\x0f\x43ompositeFilter\x12I\n\x08operator\x18\x01 \x01(\x0e\x32\x37.google.appengine.datastore.v4.CompositeFilter.Operator\x12\x35\n\x06\x66ilter\x18\x02 \x03(\x0b\x32%.google.appengine.datastore.v4.Filter\"\x13\n\x08Operator\x12\x07\n\x03\x41ND\x10\x01\"\xd0\x02\n\x0ePropertyFilter\x12\x42\n\x08property\x18\x01 \x01(\x0b\x32\x30.google.appengine.datastore.v4.PropertyReference\x12H\n\x08operator\x18\x02 \x01(\x0e\x32\x36.google.appengine.datastore.v4.PropertyFilter.Operator\x12\x33\n\x05value\x18\x03 \x01(\x0b\x32$.google.appengine.datastore.v4.Value\"{\n\x08Operator\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05\x45QUAL\x10\x05\x12\x10\n\x0cHAS_ANCESTOR\x10\x0b\"\xbc\x01\n\x08GqlQuery\x12\x14\n\x0cquery_string\x18\x01 \x01(\t\x12\x1c\n\rallow_literal\x18\x02 \x01(\x08:\x05\x66\x61lse\x12<\n\x08name_arg\x18\x03 \x03(\x0b\x32*.google.appengine.datastore.v4.GqlQueryArg\x12>\n\nnumber_arg\x18\x04 \x03(\x0b\x32*.google.appengine.datastore.v4.GqlQueryArg\"`\n\x0bGqlQueryArg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.google.appengine.datastore.v4.Value\x12\x0e\n\x06\x63ursor\x18\x03 \x01(\x0c\"\xbb\x03\n\x10QueryResultBatch\x12R\n\x12\x65ntity_result_type\x18\x01 \x01(\x0e\x32\x36.google.appengine.datastore.v4.EntityResult.ResultType\x12\x42\n\rentity_result\x18\x02 \x03(\x0b\x32+.google.appengine.datastore.v4.EntityResult\x12\x16\n\x0eskipped_cursor\x18\x03 \x01(\x0c\x12\x12\n\nend_cursor\x18\x04 \x01(\x0c\x12U\n\x0cmore_results\x18\x05 \x01(\x0e\x32?.google.appengine.datastore.v4.QueryResultBatch.MoreResultsType\x12\x1a\n\x0fskipped_results\x18\x06 \x01(\x05:\x01\x30\x12\x18\n\x10snapshot_version\x18\x07 \x01(\x03\"V\n\x0fMoreResultsType\x12\x10\n\x0cNOT_FINISHED\x10\x01\x12\x1c\n\x18MORE_RESULTS_AFTER_LIMIT\x10\x02\x12\x13\n\x0fNO_MORE_RESULTS\x10\x03\"\x84\x02\n\x08Mutation\x12\x46\n\x02op\x18\x01 \x01(\x0e\x32\x31.google.appengine.datastore.v4.Mutation.Operation:\x07UNKNOWN\x12/\n\x03key\x18\x02 \x01(\x0b\x32\".google.appengine.datastore.v4.Key\x12\x35\n\x06\x65ntity\x18\x03 \x01(\x0b\x32%.google.appengine.datastore.v4.Entity\"H\n\tOperation\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06UPSERT\x10\x03\x12\n\n\x06\x44\x45LETE\x10\x04\"Y\n\x0eMutationResult\x12/\n\x03key\x18\x03 \x01(\x0b\x32\".google.appengine.datastore.v4.Key\x12\x16\n\x0bnew_version\x18\x04 \x01(\x03:\x01\x30\"\xbb\x02\n\x12\x44\x65precatedMutation\x12\x35\n\x06upsert\x18\x01 \x03(\x0b\x32%.google.appengine.datastore.v4.Entity\x12\x35\n\x06update\x18\x02 \x03(\x0b\x32%.google.appengine.datastore.v4.Entity\x12\x35\n\x06insert\x18\x03 \x03(\x0b\x32%.google.appengine.datastore.v4.Entity\x12=\n\x0einsert_auto_id\x18\x04 \x03(\x0b\x32%.google.appengine.datastore.v4.Entity\x12\x32\n\x06\x64\x65lete\x18\x05 \x03(\x0b\x32\".google.appengine.datastore.v4.Key\x12\r\n\x05\x66orce\x18\x06 \x01(\x08\"\xf1\x01\n\x18\x44\x65precatedMutationResult\x12\x15\n\rindex_updates\x18\x01 \x01(\x05\x12>\n\x12insert_auto_id_key\x18\x02 \x03(\x0b\x32\".google.appengine.datastore.v4.Key\x12\x16\n\x0eupsert_version\x18\x03 \x03(\x03\x12\x16\n\x0eupdate_version\x18\x04 \x03(\x03\x12\x16\n\x0einsert_version\x18\x05 \x03(\x03\x12\x1e\n\x16insert_auto_id_version\x18\x06 \x03(\x03\x12\x16\n\x0e\x64\x65lete_version\x18\x07 \x03(\x03\"\xbb\x01\n\x0bReadOptions\x12]\n\x10read_consistency\x18\x01 \x01(\x0e\x32:.google.appengine.datastore.v4.ReadOptions.ReadConsistency:\x07\x44\x45\x46\x41ULT\x12\x13\n\x0btransaction\x18\x02 \x01(\x0c\"8\n\x0fReadConsistency\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06STRONG\x10\x01\x12\x0c\n\x08\x45VENTUAL\x10\x02\"\x82\x01\n\rLookupRequest\x12@\n\x0cread_options\x18\x01 \x01(\x0b\x32*.google.appengine.datastore.v4.ReadOptions\x12/\n\x03key\x18\x03 \x03(\x0b\x32\".google.appengine.datastore.v4.Key\"\xc0\x01\n\x0eLookupResponse\x12:\n\x05\x66ound\x18\x01 \x03(\x0b\x32+.google.appengine.datastore.v4.EntityResult\x12<\n\x07missing\x18\x02 \x03(\x0b\x32+.google.appengine.datastore.v4.EntityResult\x12\x34\n\x08\x64\x65\x66\x65rred\x18\x03 \x03(\x0b\x32\".google.appengine.datastore.v4.Key\"\xc3\x02\n\x0fRunQueryRequest\x12@\n\x0cread_options\x18\x01 \x01(\x0b\x32*.google.appengine.datastore.v4.ReadOptions\x12@\n\x0cpartition_id\x18\x02 \x01(\x0b\x32*.google.appengine.datastore.v4.PartitionId\x12\x33\n\x05query\x18\x03 \x01(\x0b\x32$.google.appengine.datastore.v4.Query\x12:\n\tgql_query\x18\x07 \x01(\x0b\x32\'.google.appengine.datastore.v4.GqlQuery\x12\x1d\n\x15min_safe_time_seconds\x18\x04 \x01(\x03\x12\x1c\n\x14suggested_batch_size\x18\x05 \x01(\x05\"h\n\x10RunQueryResponse\x12>\n\x05\x62\x61tch\x18\x01 \x01(\x0b\x32/.google.appengine.datastore.v4.QueryResultBatch\x12\x14\n\x0cquery_handle\x18\x02 \x01(\x0c\",\n\x14\x43ontinueQueryRequest\x12\x14\n\x0cquery_handle\x18\x01 \x01(\x0c\"W\n\x15\x43ontinueQueryResponse\x12>\n\x05\x62\x61tch\x18\x01 \x01(\x0b\x32/.google.appengine.datastore.v4.QueryResultBatch\"S\n\x17\x42\x65ginTransactionRequest\x12\x1a\n\x0b\x63ross_group\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rcross_request\x18\x02 \x01(\x08:\x05\x66\x61lse\"/\n\x18\x42\x65ginTransactionResponse\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c\"&\n\x0fRollbackRequest\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c\"\x12\n\x10RollbackResponse\"\xd2\x02\n\rCommitRequest\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c\x12\x39\n\x08mutation\x18\x05 \x03(\x0b\x32\'.google.appengine.datastore.v4.Mutation\x12N\n\x13\x64\x65precated_mutation\x18\x02 \x01(\x0b\x32\x31.google.appengine.datastore.v4.DeprecatedMutation\x12N\n\x04mode\x18\x04 \x01(\x0e\x32\x31.google.appengine.datastore.v4.CommitRequest.Mode:\rTRANSACTIONAL\x12\x1f\n\x10ignore_read_only\x18\x06 \x01(\x08:\x05\x66\x61lse\"0\n\x04Mode\x12\x11\n\rTRANSACTIONAL\x10\x01\x12\x15\n\x11NON_TRANSACTIONAL\x10\x02\"\xcc\x01\n\x0e\x43ommitResponse\x12\x46\n\x0fmutation_result\x18\x03 \x03(\x0b\x32-.google.appengine.datastore.v4.MutationResult\x12[\n\x1a\x64\x65precated_mutation_result\x18\x01 \x01(\x0b\x32\x37.google.appengine.datastore.v4.DeprecatedMutationResult\x12\x15\n\rindex_updates\x18\x04 \x01(\x05\"\x7f\n\x12\x41llocateIdsRequest\x12\x34\n\x08\x61llocate\x18\x01 \x03(\x0b\x32\".google.appengine.datastore.v4.Key\x12\x33\n\x07reserve\x18\x02 \x03(\x0b\x32\".google.appengine.datastore.v4.Key\"L\n\x13\x41llocateIdsResponse\x12\x35\n\tallocated\x18\x01 \x03(\x0b\x32\".google.appengine.datastore.v4.KeyB\'\n%com.google.google.appengine.datastore')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.datastore.datastore_v4_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.google.appengine.datastore'
  _globals['_ERROR']._serialized_start=125
  _globals['_ERROR']._serialized_end=540
  _globals['_ERROR_ERRORCODE']._serialized_start=135
  _globals['_ERROR_ERRORCODE']._serialized_end=540
  _globals['_ENTITYRESULT']._serialized_start=543
  _globals['_ENTITYRESULT']._serialized_end=699
  _globals['_ENTITYRESULT_RESULTTYPE']._serialized_start=647
  _globals['_ENTITYRESULT_RESULTTYPE']._serialized_end=699
  _globals['_QUERY']._serialized_start=702
  _globals['_QUERY']._serialized_end=1101
  _globals['_KINDEXPRESSION']._serialized_start=1103
  _globals['_KINDEXPRESSION']._serialized_end=1133
  _globals['_PROPERTYREFERENCE']._serialized_start=1135
  _globals['_PROPERTYREFERENCE']._serialized_end=1168
  _globals['_PROPERTYEXPRESSION']._serialized_start=1171
  _globals['_PROPERTYEXPRESSION']._serialized_end=1394
  _globals['_PROPERTYEXPRESSION_AGGREGATIONFUNCTION']._serialized_start=1362
  _globals['_PROPERTYEXPRESSION_AGGREGATIONFUNCTION']._serialized_end=1394
  _globals['_PROPERTYORDER']._serialized_start=1397
  _globals['_PROPERTYORDER']._serialized_end=1610
  _globals['_PROPERTYORDER_DIRECTION']._serialized_start=1568
  _globals['_PROPERTYORDER_DIRECTION']._serialized_end=1610
  _globals['_FILTER']._serialized_start=1613
  _globals['_FILTER']._serialized_end=1767
  _globals['_COMPOSITEFILTER']._serialized_start=1770
  _globals['_COMPOSITEFILTER']._serialized_end=1938
  _globals['_COMPOSITEFILTER_OPERATOR']._serialized_start=1919
  _globals['_COMPOSITEFILTER_OPERATOR']._serialized_end=1938
  _globals['_PROPERTYFILTER']._serialized_start=1941
  _globals['_PROPERTYFILTER']._serialized_end=2277
  _globals['_PROPERTYFILTER_OPERATOR']._serialized_start=2154
  _globals['_PROPERTYFILTER_OPERATOR']._serialized_end=2277
  _globals['_GQLQUERY']._serialized_start=2280
  _globals['_GQLQUERY']._serialized_end=2468
  _globals['_GQLQUERYARG']._serialized_start=2470
  _globals['_GQLQUERYARG']._serialized_end=2566
  _globals['_QUERYRESULTBATCH']._serialized_start=2569
  _globals['_QUERYRESULTBATCH']._serialized_end=3012
  _globals['_QUERYRESULTBATCH_MORERESULTSTYPE']._serialized_start=2926
  _globals['_QUERYRESULTBATCH_MORERESULTSTYPE']._serialized_end=3012
  _globals['_MUTATION']._serialized_start=3015
  _globals['_MUTATION']._serialized_end=3275
  _globals['_MUTATION_OPERATION']._serialized_start=3203
  _globals['_MUTATION_OPERATION']._serialized_end=3275
  _globals['_MUTATIONRESULT']._serialized_start=3277
  _globals['_MUTATIONRESULT']._serialized_end=3366
  _globals['_DEPRECATEDMUTATION']._serialized_start=3369
  _globals['_DEPRECATEDMUTATION']._serialized_end=3684
  _globals['_DEPRECATEDMUTATIONRESULT']._serialized_start=3687
  _globals['_DEPRECATEDMUTATIONRESULT']._serialized_end=3928
  _globals['_READOPTIONS']._serialized_start=3931
  _globals['_READOPTIONS']._serialized_end=4118
  _globals['_READOPTIONS_READCONSISTENCY']._serialized_start=4062
  _globals['_READOPTIONS_READCONSISTENCY']._serialized_end=4118
  _globals['_LOOKUPREQUEST']._serialized_start=4121
  _globals['_LOOKUPREQUEST']._serialized_end=4251
  _globals['_LOOKUPRESPONSE']._serialized_start=4254
  _globals['_LOOKUPRESPONSE']._serialized_end=4446
  _globals['_RUNQUERYREQUEST']._serialized_start=4449
  _globals['_RUNQUERYREQUEST']._serialized_end=4772
  _globals['_RUNQUERYRESPONSE']._serialized_start=4774
  _globals['_RUNQUERYRESPONSE']._serialized_end=4878
  _globals['_CONTINUEQUERYREQUEST']._serialized_start=4880
  _globals['_CONTINUEQUERYREQUEST']._serialized_end=4924
  _globals['_CONTINUEQUERYRESPONSE']._serialized_start=4926
  _globals['_CONTINUEQUERYRESPONSE']._serialized_end=5013
  _globals['_BEGINTRANSACTIONREQUEST']._serialized_start=5015
  _globals['_BEGINTRANSACTIONREQUEST']._serialized_end=5098
  _globals['_BEGINTRANSACTIONRESPONSE']._serialized_start=5100
  _globals['_BEGINTRANSACTIONRESPONSE']._serialized_end=5147
  _globals['_ROLLBACKREQUEST']._serialized_start=5149
  _globals['_ROLLBACKREQUEST']._serialized_end=5187
  _globals['_ROLLBACKRESPONSE']._serialized_start=5189
  _globals['_ROLLBACKRESPONSE']._serialized_end=5207
  _globals['_COMMITREQUEST']._serialized_start=5210
  _globals['_COMMITREQUEST']._serialized_end=5548
  _globals['_COMMITREQUEST_MODE']._serialized_start=5500
  _globals['_COMMITREQUEST_MODE']._serialized_end=5548
  _globals['_COMMITRESPONSE']._serialized_start=5551
  _globals['_COMMITRESPONSE']._serialized_end=5755
  _globals['_ALLOCATEIDSREQUEST']._serialized_start=5757
  _globals['_ALLOCATEIDSREQUEST']._serialized_end=5884
  _globals['_ALLOCATEIDSRESPONSE']._serialized_start=5886
  _globals['_ALLOCATEIDSRESPONSE']._serialized_end=5962

