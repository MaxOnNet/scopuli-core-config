#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright [2018] Tatarnikov Viktor [viktor@tatarnikov.org]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" """

from unittest import TestCase
from Scopuli.Interfaces.Config import Config


class Interfaces_Config(TestCase):
    def test_config_primary(self):
        config = Config(use_web=False)
        
        #   Read
        self.assertEqual(config.get("SelfTest", "test1", "arg1", "3"), "1")
        self.assertEqual(config.get("SelfTest", "test2", "arg3", "2"), "2")

        #   Add Node
        self.assertEqual(config.set("SelfTest", "test3", "arg1", "1"), None)
        self.assertEqual(config.get("SelfTest", "test3", "arg1", "2"), "1")

        #   Save and reload
        config.save()
        config = Config(use_web=False)
        
        #   Check Now node
        self.assertEqual(config.get("SelfTest", "test3", "arg1", "2"), "1")
        
        #   Remove
        self.assertEqual(config.remove("SelfTest", "test3", "arg1"), None)
        self.assertEqual(config.remove("SelfTest", "test3", ""), None)
        self.assertEqual(config.get("SelfTest", "test3", "arg1", "2"), "2")

        config.save()
