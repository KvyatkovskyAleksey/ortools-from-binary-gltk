# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/scheduling/jobshop_scheduling.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+ortools/scheduling/jobshop_scheduling.proto\x12#operations_research.scheduling.jssp\x1a\x1egoogle/protobuf/wrappers.proto\"7\n\x04Task\x12\x0f\n\x07machine\x18\x01 \x03(\x05\x12\x10\n\x08\x64uration\x18\x02 \x03(\x03\x12\x0c\n\x04\x63ost\x18\x03 \x03(\x03\"\xad\x02\n\x03Job\x12\x38\n\x05tasks\x18\x01 \x03(\x0b\x32).operations_research.scheduling.jssp.Task\x12\x33\n\x0e\x65\x61rliest_start\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x16\n\x0e\x65\x61rly_due_date\x18\x03 \x01(\x03\x12\x15\n\rlate_due_date\x18\x04 \x01(\x03\x12$\n\x1c\x65\x61rliness_cost_per_time_unit\x18\x05 \x01(\x03\x12#\n\x1blateness_cost_per_time_unit\x18\x06 \x01(\x03\x12/\n\nlatest_end\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x0c\n\x04name\x18\x10 \x01(\t\"/\n\x14TransitionTimeMatrix\x12\x17\n\x0ftransition_time\x18\x01 \x03(\x03\"r\n\x07Machine\x12Y\n\x16transition_time_matrix\x18\x01 \x01(\x0b\x32\x39.operations_research.scheduling.jssp.TransitionTimeMatrix\x12\x0c\n\x04name\x18\x10 \x01(\t\"U\n\rJobPrecedence\x12\x17\n\x0f\x66irst_job_index\x18\x01 \x01(\x05\x12\x18\n\x10second_job_index\x18\x02 \x01(\x05\x12\x11\n\tmin_delay\x18\x03 \x01(\x03\"\xca\x02\n\x10JsspInputProblem\x12\x36\n\x04jobs\x18\x01 \x03(\x0b\x32(.operations_research.scheduling.jssp.Job\x12>\n\x08machines\x18\x02 \x03(\x0b\x32,.operations_research.scheduling.jssp.Machine\x12G\n\x0bprecedences\x18\x03 \x03(\x0b\x32\x32.operations_research.scheduling.jssp.JobPrecedence\x12#\n\x1bmakespan_cost_per_time_unit\x18\x04 \x01(\x03\x12\x34\n\x0escaling_factor\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x0c\n\x04seed\x18\x18 \x01(\x05\x12\x0c\n\x04name\x18\x10 \x01(\t\"=\n\x0c\x41ssignedTask\x12\x19\n\x11\x61lternative_index\x18\x01 \x01(\x05\x12\x12\n\nstart_time\x18\x02 \x01(\x03\"\x81\x01\n\x0b\x41ssignedJob\x12@\n\x05tasks\x18\x01 \x03(\x0b\x32\x31.operations_research.scheduling.jssp.AssignedTask\x12\x15\n\rdue_date_cost\x18\x02 \x01(\x03\x12\x19\n\x11sum_of_task_costs\x18\x03 \x01(\x03\"\x7f\n\x12JsspOutputSolution\x12>\n\x04jobs\x18\x01 \x03(\x0b\x32\x30.operations_research.scheduling.jssp.AssignedJob\x12\x15\n\rmakespan_cost\x18\x02 \x01(\x03\x12\x12\n\ntotal_cost\x18\x03 \x01(\x03\x42G\n\"com.google.ortools.scheduling.jsspP\x01\xaa\x02\x1eGoogle.OrTools.scheduling.Jsspb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.scheduling.jobshop_scheduling_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.google.ortools.scheduling.jsspP\001\252\002\036Google.OrTools.scheduling.Jssp'
  _globals['_TASK']._serialized_start=116
  _globals['_TASK']._serialized_end=171
  _globals['_JOB']._serialized_start=174
  _globals['_JOB']._serialized_end=475
  _globals['_TRANSITIONTIMEMATRIX']._serialized_start=477
  _globals['_TRANSITIONTIMEMATRIX']._serialized_end=524
  _globals['_MACHINE']._serialized_start=526
  _globals['_MACHINE']._serialized_end=640
  _globals['_JOBPRECEDENCE']._serialized_start=642
  _globals['_JOBPRECEDENCE']._serialized_end=727
  _globals['_JSSPINPUTPROBLEM']._serialized_start=730
  _globals['_JSSPINPUTPROBLEM']._serialized_end=1060
  _globals['_ASSIGNEDTASK']._serialized_start=1062
  _globals['_ASSIGNEDTASK']._serialized_end=1123
  _globals['_ASSIGNEDJOB']._serialized_start=1126
  _globals['_ASSIGNEDJOB']._serialized_end=1255
  _globals['_JSSPOUTPUTSOLUTION']._serialized_start=1257
  _globals['_JSSPOUTPUTSOLUTION']._serialized_end=1384
# @@protoc_insertion_point(module_scope)
