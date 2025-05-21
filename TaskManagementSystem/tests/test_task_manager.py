import unittest
import sys
import os

# Add src directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()

    def test_add_task(self):
        self.tm.add_task("Test Task", "2025-06-01")
        self.assertEqual(len(self.tm.tasks), 1)

    def test_toggle_complete(self):
        self.tm.add_task("Sample", "2025-06-01")
        self.tm.toggle_complete(1)
        self.assertTrue(self.tm.tasks[0].complete)

if __name__ == '__main__':
    unittest.main()
