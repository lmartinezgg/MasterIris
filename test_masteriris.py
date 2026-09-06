# test_masteriris.py
"""
Tests for MasterIris module.
"""

import unittest
from masteriris import MasterIris

class TestMasterIris(unittest.TestCase):
    """Test cases for MasterIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MasterIris()
        self.assertIsInstance(instance, MasterIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MasterIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
