"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2010-2022 Google LLC
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import ortools.sat.cp_model_pb2
import ortools.sat.sat_parameters_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CpSolverRequest(google.protobuf.message.Message):
    """The request sent to the remote solve service."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    @property
    def model(self) -> ortools.sat.cp_model_pb2.CpModelProto:
        """The model to solve."""
    @property
    def parameters(self) -> ortools.sat.sat_parameters_pb2.SatParameters:
        """Solver parameters."""
    def __init__(
        self,
        *,
        model: ortools.sat.cp_model_pb2.CpModelProto | None = ...,
        parameters: ortools.sat.sat_parameters_pb2.SatParameters | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["model", b"model", "parameters", b"parameters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["model", b"model", "parameters", b"parameters"]) -> None: ...

global___CpSolverRequest = CpSolverRequest