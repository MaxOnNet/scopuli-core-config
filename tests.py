from unittest import TestCase
from Interfaces.Config import Config


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
