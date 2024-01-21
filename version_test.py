#!/usr/bin/env python3
# Copyright 2010-2022 Google LLC
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
"""Simple unit tests to check version."""

import unittest
import ortools
from ortools.init.python import init


class VersionApi(unittest.TestCase):

    def test_version_api(self):
        print("test_version_api")
        self.assertEqual(9, init.OrToolsVersion.major_number())
        self.assertEqual(8, init.OrToolsVersion.minor_number())
        self.assertEqual(3309, init.OrToolsVersion.patch_number())

    def test_version(self):
        print("test_version")
        self.assertEqual("9.8.3309", ortools.__version__)


if __name__ == "__main__":
    unittest.main()
