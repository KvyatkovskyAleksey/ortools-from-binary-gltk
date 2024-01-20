# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/bop/bop_parameters.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ortools/bop/bop_parameters.proto\x12\x17operations_research.bop\"\x84\x04\n\x12\x42opOptimizerMethod\x12G\n\x04type\x18\x01 \x01(\x0e\x32\x39.operations_research.bop.BopOptimizerMethod.OptimizerType\"\xa4\x03\n\rOptimizerType\x12\x12\n\x0eSAT_CORE_BASED\x10\x00\x12\x15\n\x11SAT_LINEAR_SEARCH\x10\x0f\x12\x15\n\x11LINEAR_RELAXATION\x10\x01\x12\x10\n\x0cLOCAL_SEARCH\x10\x02\x12\x19\n\x15RANDOM_FIRST_SOLUTION\x10\x03\x12\x19\n\x15RANDOM_CONSTRAINT_LNS\x10\x04\x12\x17\n\x13RANDOM_VARIABLE_LNS\x10\x05\x12\x10\n\x0c\x43OMPLETE_LNS\x10\x07\x12\x15\n\x11LP_FIRST_SOLUTION\x10\x08\x12\x1c\n\x18OBJECTIVE_FIRST_SOLUTION\x10\t\x12\x1e\n\x1aUSER_GUIDED_FIRST_SOLUTION\x10\x0e\x12&\n\"RANDOM_CONSTRAINT_LNS_GUIDED_BY_LP\x10\x0b\x12$\n RANDOM_VARIABLE_LNS_GUIDED_BY_LP\x10\x0c\x12\x16\n\x12RELATION_GRAPH_LNS\x10\x10\x12#\n\x1fRELATION_GRAPH_LNS_GUIDED_BY_LP\x10\x11\"U\n\x15\x42opSolverOptimizerSet\x12<\n\x07methods\x18\x01 \x03(\x0b\x32+.operations_research.bop.BopOptimizerMethod\"\xee\x13\n\rBopParameters\x12 \n\x13max_time_in_seconds\x18\x01 \x01(\x01:\x03inf\x12#\n\x16max_deterministic_time\x18\x1b \x01(\x01:\x03inf\x12$\n\x19lp_max_deterministic_time\x18% \x01(\x01:\x01\x31\x12\x39\n1max_number_of_consecutive_failing_optimizer_calls\x18# \x01(\x05\x12\"\n\x12relative_gap_limit\x18\x1c \x01(\x01:\x06\x30.0001\x12\"\n\x17max_num_decisions_in_ls\x18\x02 \x01(\x05:\x01\x34\x12\x34\n max_num_broken_constraints_in_ls\x18& \x01(\x05:\n2147483647\x12\"\n\x13log_search_progress\x18\x0e \x01(\x08:\x05\x66\x61lse\x12&\n\x18\x63ompute_estimated_impact\x18\x03 \x01(\x08:\x04true\x12 \n\x11prune_search_tree\x18\x04 \x01(\x08:\x05\x66\x61lse\x12,\n\x1dsort_constraints_by_num_terms\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x0euse_random_lns\x18\x06 \x01(\x08:\x04true\x12\x16\n\x0brandom_seed\x18\x07 \x01(\x05:\x01\x38\x12\x1c\n\x10num_relaxed_vars\x18\x08 \x01(\x05:\x02\x31\x30\x12\x33\n%max_number_of_conflicts_in_random_lns\x18\t \x01(\x05:\x04\x32\x35\x30\x30\x12\x1f\n\x14num_random_lns_tries\x18\n \x01(\x05:\x01\x31\x12\x31\n\x1emax_number_of_backtracks_in_ls\x18\x0b \x01(\x03:\t100000000\x12\x18\n\nuse_lp_lns\x18\x0c \x01(\x08:\x04true\x12\x31\n#use_sat_to_choose_lns_neighbourhood\x18\x0f \x01(\x08:\x04true\x12\x33\n\'max_number_of_conflicts_for_quick_check\x18\x10 \x01(\x05:\x02\x31\x30\x12\x1b\n\x0cuse_symmetry\x18\x11 \x01(\x08:\x05\x66\x61lse\x12\x35\n&exploit_symmetry_in_sat_first_solution\x18( \x01(\x08:\x05\x66\x61lse\x12\x42\n5max_number_of_conflicts_in_random_solution_generation\x18\x14 \x01(\x05:\x03\x35\x30\x30\x12?\n0max_number_of_explored_assignments_per_try_in_ls\x18\x15 \x01(\x03:\x05\x31\x30\x30\x30\x30\x12+\n\x1duse_transposition_table_in_ls\x18\x16 \x01(\x08:\x04true\x12\x33\n$use_potential_one_flip_repairs_in_ls\x18\' \x01(\x08:\x05\x66\x61lse\x12.\n use_learned_binary_clauses_in_lp\x18\x17 \x01(\x08:\x04true\x12\x1c\n\x11number_of_solvers\x18\x18 \x01(\x05:\x01\x31\x12r\n\x14synchronization_type\x18\x19 \x01(\x0e\x32@.operations_research.bop.BopParameters.ThreadSynchronizationType:\x12NO_SYNCHRONIZATION\x12M\n\x15solver_optimizer_sets\x18\x1a \x03(\x0b\x32..operations_research.bop.BopSolverOptimizerSet\x12\xf2\x05\n\x1d\x64\x65\x66\x61ult_solver_optimizer_sets\x18! \x01(\t:\xca\x05methods:{type:LOCAL_SEARCH }                       methods:{type:RANDOM_FIRST_SOLUTION }              methods:{type:LINEAR_RELAXATION }                  methods:{type:LP_FIRST_SOLUTION }                  methods:{type:OBJECTIVE_FIRST_SOLUTION }           methods:{type:USER_GUIDED_FIRST_SOLUTION }         methods:{type:RANDOM_CONSTRAINT_LNS_GUIDED_BY_LP } methods:{type:RANDOM_VARIABLE_LNS_GUIDED_BY_LP }   methods:{type:RELATION_GRAPH_LNS }                 methods:{type:RELATION_GRAPH_LNS_GUIDED_BY_LP }    methods:{type:RANDOM_CONSTRAINT_LNS }              methods:{type:RANDOM_VARIABLE_LNS }                methods:{type:SAT_CORE_BASED }                     methods:{type:COMPLETE_LNS }                       \x12&\n\x17use_lp_strong_branching\x18\x1d \x01(\x08:\x05\x66\x61lse\x12.\n\"decomposer_num_variables_threshold\x18\x1e \x01(\x05:\x02\x35\x30\x12\x30\n%num_bop_solvers_used_by_decomposition\x18\x1f \x01(\x05:\x01\x31\x12\x31\n&decomposed_problem_min_time_in_seconds\x18$ \x01(\x01:\x01\x30\x12(\n\x1aguided_sat_conflicts_chunk\x18\" \x01(\x05:\x04\x31\x30\x30\x30\x12\x30\n%max_lp_solve_for_feasibility_problems\x18) \x01(\x05:\x01\x30\"b\n\x19ThreadSynchronizationType\x12\x16\n\x12NO_SYNCHRONIZATION\x10\x00\x12\x13\n\x0fSYNCHRONIZE_ALL\x10\x01\x12\x18\n\x14SYNCHRONIZE_ON_RIGHT\x10\x02\x42/\n\x16\x63om.google.ortools.bopP\x01\xaa\x02\x12Google.OrTools.Bop')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.bop.bop_parameters_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.google.ortools.bopP\001\252\002\022Google.OrTools.Bop'
  _globals['_BOPOPTIMIZERMETHOD']._serialized_start=62
  _globals['_BOPOPTIMIZERMETHOD']._serialized_end=578
  _globals['_BOPOPTIMIZERMETHOD_OPTIMIZERTYPE']._serialized_start=158
  _globals['_BOPOPTIMIZERMETHOD_OPTIMIZERTYPE']._serialized_end=578
  _globals['_BOPSOLVEROPTIMIZERSET']._serialized_start=580
  _globals['_BOPSOLVEROPTIMIZERSET']._serialized_end=665
  _globals['_BOPPARAMETERS']._serialized_start=668
  _globals['_BOPPARAMETERS']._serialized_end=3210
  _globals['_BOPPARAMETERS_THREADSYNCHRONIZATIONTYPE']._serialized_start=3112
  _globals['_BOPPARAMETERS_THREADSYNCHRONIZATIONTYPE']._serialized_end=3210
# @@protoc_insertion_point(module_scope)