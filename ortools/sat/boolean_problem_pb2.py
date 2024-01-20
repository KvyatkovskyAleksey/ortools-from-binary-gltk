# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/sat/boolean_problem.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ortools/sat/boolean_problem.proto\x12\x17operations_research.sat\"{\n\x17LinearBooleanConstraint\x12\x10\n\x08literals\x18\x01 \x03(\x05\x12\x14\n\x0c\x63oefficients\x18\x02 \x03(\x03\x12\x13\n\x0blower_bound\x18\x03 \x01(\x03\x12\x13\n\x0bupper_bound\x18\x04 \x01(\x03\x12\x0e\n\x04name\x18\x05 \x01(\t:\x00\"g\n\x0fLinearObjective\x12\x10\n\x08literals\x18\x01 \x03(\x05\x12\x14\n\x0c\x63oefficients\x18\x02 \x03(\x03\x12\x11\n\x06offset\x18\x03 \x01(\x01:\x01\x30\x12\x19\n\x0escaling_factor\x18\x04 \x01(\x01:\x01\x31\"%\n\x11\x42ooleanAssignment\x12\x10\n\x08literals\x18\x01 \x03(\x05\"\xb4\x02\n\x14LinearBooleanProblem\x12\x0e\n\x04name\x18\x01 \x01(\t:\x00\x12\x15\n\rnum_variables\x18\x03 \x01(\x05\x12\x45\n\x0b\x63onstraints\x18\x04 \x03(\x0b\x32\x30.operations_research.sat.LinearBooleanConstraint\x12;\n\tobjective\x18\x05 \x01(\x0b\x32(.operations_research.sat.LinearObjective\x12\x11\n\tvar_names\x18\x06 \x03(\t\x12>\n\nassignment\x18\x07 \x01(\x0b\x32*.operations_research.sat.BooleanAssignment\x12\x1e\n\x16original_num_variables\x18\x08 \x01(\x05\x42/\n\x16\x63om.google.ortools.satP\x01\xaa\x02\x12Google.OrTools.Sat')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.sat.boolean_problem_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.google.ortools.satP\001\252\002\022Google.OrTools.Sat'
  _globals['_LINEARBOOLEANCONSTRAINT']._serialized_start=62
  _globals['_LINEARBOOLEANCONSTRAINT']._serialized_end=185
  _globals['_LINEAROBJECTIVE']._serialized_start=187
  _globals['_LINEAROBJECTIVE']._serialized_end=290
  _globals['_BOOLEANASSIGNMENT']._serialized_start=292
  _globals['_BOOLEANASSIGNMENT']._serialized_end=329
  _globals['_LINEARBOOLEANPROBLEM']._serialized_start=332
  _globals['_LINEARBOOLEANPROBLEM']._serialized_end=640
# @@protoc_insertion_point(module_scope)
