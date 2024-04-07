# --*-- coding: utf-8 --*--
import os
import unittest
from config import cfg
from torch import nn, optim
from torch.utils.data import default_collate

from model import Vector
from torchlight import get_dump_path


# class Test_Runner(unittest.TestCase):
	'''
	TestRunner是一个测试用例，是unittest.TestCase的子类，unittest.TestCase
	提供了组织和运行特定测试的基础设施。
	'''

	def __init__(self):
		cfg2=cfg
	# 	print("\033[92m" +f"' 文件:C:\ZS-F-VQA-main\code\test_main_init.py||类：Test_Runner ||方法：__init__ ||变量：self.fusion_model_path ':{self.fusion_model_path}" + "\033[0m")
	# 	print("\033[92m" + f"' 文件:C:\ZS-F-VQA-main\code\test_main_init.py||类：TestRunner ||方法：__init__ || '" + "\033[0m")

	'''
	TestRunner有一个方法test_init，它似乎是一种初始化过程的测试，
	由get_dump_path(self.args)表示。然而，没有上下文显示通过self.args
	传递什么参数，以及get_dump_path(self.args)做什么。
	根据提供的额外信息，test_init执行了许多断言。它检查运行器实例的某些属性与
	预期值的相等性，或检查这些属性的实例类型。它还确认某些属性不为空。
	'''

	def test_init(self):
		'''
		get_dump_path函数似乎生成了用于存储某些数据或结果的目录路径。
		没有实际的实现，具体的操作就不清楚了
		'''


		'''
		Vector类似乎处理一些与向量相关的操作，名称像glove.840B，这让人推测它可能是与GloVe向量相关的一种
		词嵌入类型。但是没有更多的代码，这些都只是假设。__getitem__、_prepare、check、cache方法似乎是
		Vector类的一部分，并可能处理词向量上的各种操作。
		'''
		self.assertTrue(isinstance(self.runner.word2vec, Vector))
		# 进一步的测试将取决于 fvqa.get_loader 方法返回的内容
		# self.assertTrue(isinstance(self.runner.train_loader, SomeTrainLoaderType))
		# self.assertTrue(isinstance(self.runner.val_loader, SomeValLoaderType))
		self.assertEqual(self.runner.avocab, default_collate(list(range(0, self.args.FVQA.max_ans))))
		# Similarly, further tests for question_word2vec will depend on the actual instance it should be.
		# self.assertTrue(isinstance(self.runner.question_word2vec, SomeVectorType))
		self.assertIsNotNone(self.runner.fusion_model)
		self.assertIsNotNone(self.runner.answer_net)
		self.assertIsNotNone(self.runner.negtive_mux)
		self.assertTrue(isinstance(self.runner.optimizer, optim.Adam))
		self.assertTrue(isinstance(self.runner.log_softmax, nn.LogSoftmax))
		self.assertEqual(self.runner.max_acc, [0, 0, 0, 0])
		self.assertEqual(self.runner.max_zsl_acc, [0, 0, 0, 0])
		self.assertEqual(self.runner.best_epoch, 0)
		self.assertEqual(self.runner.correspond_loss, 1e20)
		self.assertEqual(self.runner.early_stop, 0)
		self.assertEqual(self.runner.args, self.args)  # If there are also methods like _load_model defined, the model loadings could be further tested.  # Here I am assuming that the model files are not available during test.


if __name__ == "__main__":
	unittest.main()
	# cfg=cfg()
	# print("\033[92m" +f"' 文件:C:\ZS-F-VQA-main\code\test_main_init.py||类： ||方法： ||变量：cfg.fusion_model_path ':{cfg.fusion_model_path}" + "\033[0m")
