import unittest
import os
from config import cfg


class TestConfig(unittest.TestCase):
	def setUp(self):
		self.config = cfg()

	def test_initial_values(self):
		self.assertEqual(self.config.this_dir, os.path.dirname(os.path.realpath(__file__)))
		print("\033[92m" + f"' 文件:C:\ZS-F-VQA-main\code\test_config.py||类：TestConfig ||方法：test_initial_values ||变量：self.config.this_dir ':{self.config.this_dir}" + "\033[0m")
		self.assertEqual(self.config.method_choice, "KG")
		print("\033[92m" + f"' 文件:C:\ZS-F-VQA-main\code\test_config.py||类：TestConfig ||方法：test_initial_values ||变量：self.config.method_choice ':{self.config.method_choice}" + "\033[0m")
		self.assertEqual(self.config.ans_fusion, 'RNN_concate')
		print("\033[92m" + f"' 文件:C:\ZS-F-VQA-main\code\test_config.py||类：TestConfig ||方法：test_initial_values ||变量：self.config.ans_fusion ':{self.config.ans_fusion}" + "\033[0m")
		self.assertEqual(self.config.requires_grad, 1)
		print("\033[92m" + f"' 文件:C:\ZS-F-VQA-main\code\test_config.py||类：TestConfig ||方法：test_initial_values ||变量：self.config.requires_grad ':{self.config.requires_grad}" + "\033[0m")
		self.assertEqual(self.config.bert_dim, 1024)  # add more assertions here...
		print("\033[92m" + f"' 文件:C:\ZS-F-VQA-main\code\test_config.py||类：TestConfig ||方法：test_initial_values ||变量：self.config.bert_dim ':{self.config.bert_dim}" + "\033[0m")

	def test_get_args(self):
		# Mock args here or use a library like 'mock'
		pass

	def test_update_train_configs(self):
		# Mock args here or use a library like 'mock'
		pass


if __name__ == "__main__":
	unittest.main()
