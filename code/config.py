import os

import numpy as np
import random
import torch
from easydict import EasyDict as edict
import argparse
import pdb


class cfg():
	def __init__(self):
		print("=================config.py init start======================")
		self.fusion_model_path = ""
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.fusion_model_path ':{self.fusion_model_path}" + "\033[0m")
		self.answer_net_path = ""
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.answer_net_path ':{self.answer_net_path}" + "\033[0m")
		self.joint_test_way = 0
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.joint_test_way ':{self.joint_test_way}" + "\033[0m")
		self.this_dir = os.path.dirname(__file__)
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.this_dir ':{self.this_dir}" + "\033[0m")
		self.answer_net_path = ""
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.answer_net_path ':{self.answer_net_path}" + "\033[0m")
		self.joint_test_way = 0
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.joint_test_way ':{self.joint_test_way}" + "\033[0m")
		self.this_dir = os.path.dirname(__file__)
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.this_dir ':{self.this_dir}" + "\033[0m")
		self.answer_net_path = ""
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.answer_net_path ':{self.answer_net_path}" + "\033[0m")
		self.joint_test_way = 0
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.joint_test_way ':{self.joint_test_way}" + "\033[0m")
		self.this_dir = os.path.dirname(__file__)
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.this_dir ':{self.this_dir}" + "\033[0m")
		# self.data_root = os.path.abspath(os.path.join(self.this_dir, '..', '..', 'data', 'KG_VQA'))
		parent_dir = os.path.join(self.this_dir, '..')
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量parent_dir ':{parent_dir}" + "\033[0m")

		self.data_root = os.path.abspath(os.path.join(parent_dir, 'data'))
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.data_root ':{self.data_root}" + "\033[0m")

		self.this_dir = os.path.dirname(__file__)
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.this_dir ':{self.this_dir}" + "\033[0m")
		self.project_root = os.path.abspath(os.path.join(self.this_dir, '..'))
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.project_root ':{self.project_root}" + "\033[0m")
		self.method_choice = "KG"
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.method_choice ':{self.method_choice}" + "\033[0m")
		self.ans_fusion = 'RNN_concate'
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.ans_fusion ':{self.ans_fusion}" + "\033[0m")
		self.fusion_model = ''
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.fusion_model ':{self.fusion_model}" + "\033[0m")
		self.requires_grad = 1
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.requires_grad ':{self.requires_grad}" + "\033[0m")
		self.bert_dim = 1024
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.bert_dim ':{self.bert_dim}" + "\033[0m")
		self.KGE = "TransE"
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.KGE ':{self.KGE}" + "\033[0m")
		self.KGE_init = None  # none or w2v
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.KGE_init ':{self.KGE_init}" + "\033[0m")
		self.glimpse = 4
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.glimpse ':{self.glimpse}" + "\033[0m")
		self.ans_feature_len = 0
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.ans_feature_len ':{self.ans_feature_len}" + "\033[0m")
		self.patience = 30
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.patience ':{self.patience}" + "\033[0m")
		self.v_dim = 2048
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.v_dim ':{self.v_dim}" + "\033[0m")

		self.FVQA = edict()
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA ':{self.FVQA}" + "\033[0m")

		print("-----------------FVQA params--------------------------")
		# FVQA params
		self.FVQA.max_ans = 500
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.max_ans ':{self.FVQA.max_ans}" + "\033[0m")
		self.FVQA.data_choice = "0"
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.data_choice ':{self.FVQA.data_choice}" + "\033[0m")

		self.FVQA.entity_num = "all"
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.entity_num ':{self.FVQA.entity_num}" + "\033[0m")
		self.FVQA.data_path = os.path.join(self.data_root, "fvqa")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.data_path ':{self.FVQA.data_path}" + "\033[0m")

		self.FVQA.exp_data_path = os.path.join(self.FVQA.data_path, "exp_data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.exp_data_path ':{self.FVQA.exp_data_path}" + "\033[0m")
		self.FVQA.common_data_path = os.path.join(self.FVQA.exp_data_path, "common_data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.common_data_path ':{self.FVQA.common_data_path}" + "\033[0m")
		self.FVQA.test_data_path = os.path.join(self.FVQA.exp_data_path, "test_data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.test_data_path ':{self.FVQA.test_data_path}" + "\033[0m")
		self.FVQA.train_data_path = os.path.join(self.FVQA.exp_data_path, "train_data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.train_data_path ':{self.FVQA.train_data_path}" + "\033[0m")
		self.FVQA.seen_train_data_path = os.path.join(self.FVQA.exp_data_path, "train_seen_data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.seen_train_data_path ':{self.FVQA.seen_train_data_path}" + "\033[0m")
		self.FVQA.unseen_test_data_path = os.path.join(self.FVQA.exp_data_path, "test_unseen_data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.unseen_test_data_path ':{self.FVQA.unseen_test_data_path}" + "\033[0m")
		self.FVQA.seen_test_data_path = os.path.join(self.FVQA.exp_data_path, "test_seen_data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.seen_test_data_path ':{self.FVQA.seen_test_data_path}" + "\033[0m")
		self.FVQA.model_save_path = os.path.join(self.FVQA.data_path, "model_save")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.model_save_path ':{self.FVQA.model_save_path}" + "\033[0m")
		self.FVQA.runs_path = os.path.join(self.FVQA.data_path, "model_save")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.runs_path ':{self.FVQA.runs_path}" + "\033[0m")
		self.FVQA.qa_path = self.FVQA.exp_data_path
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.qa_path ':{self.FVQA.qa_path}" + "\033[0m")
		self.FVQA.feature_path = os.path.join(self.FVQA.common_data_path, 'fvqa-resnet-14x14.h5')
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.feature_path ':{self.FVQA.feature_path}" + "\033[0m")
		self.FVQA.answer_vocab_path = os.path.join(self.FVQA.common_data_path, 'answer.vocab.fvqa.' + str(self.FVQA.max_ans) + '.json')
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.answer_vocab_path ':{self.FVQA.answer_vocab_path}" + "\033[0m")
		self.FVQA.fact_vocab_path = os.path.join(self.FVQA.common_data_path, 'answer.vocab.fvqa.fact.500.json')
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.fact_vocab_path ':{self.FVQA.fact_vocab_path}" + "\033[0m")
		self.FVQA.relation_vocab_path = os.path.join(self.FVQA.common_data_path, 'answer.vocab.fvqa.relation.500.json')
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.relation_vocab_path ':{self.FVQA.relation_vocab_path}" + "\033[0m")
		self.FVQA.fact_relation_to_ans_path = os.path.join(self.FVQA.common_data_path, "fact_relation_dict.data")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.fact_relation_to_ans_path ':{self.FVQA.fact_relation_to_ans_path}" + "\033[0m")
		self.FVQA.img_path = os.path.join(self.FVQA.qa_path, 'images')
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.img_path ':{self.FVQA.img_path}" + "\033[0m")
		self.FVQA.kg_path = os.path.join(self.FVQA.common_data_path, "KG_embedding")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.kg_path ':{self.FVQA.kg_path}" + "\033[0m")
		self.FVQA.gae_path = os.path.join(self.FVQA.common_data_path, "GAE_embedding")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.gae_path ':{self.FVQA.gae_path}" + "\033[0m")
		self.FVQA.bert_path = os.path.join(self.FVQA.common_data_path, "BERT_embedding")
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.bert_path ':{self.FVQA.bert_path}" + "\033[0m")
		self.FVQA.gae_node_num = 3463
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.gae_node_num ':{self.FVQA.gae_node_num}" + "\033[0m")
		self.FVQA.gae_init = "w2v"  # or w2v
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.FVQA.gae_init ':{self.FVQA.gae_init}" + "\033[0m")
		# 有问题
		# self.FVQA.qa = 'train2014'
		# self.FVQA.task = 'OpenEnded'
		# self.FVQA.dataset = 'mscoco'
		# self.dataset = self.FVQA
		self.cache_path = os.path.join(self.data_root, '.cache')
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.cache_path ':{self.cache_path}" + "\033[0m")
		self.output_path = self.FVQA.model_save_path
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.output_path ':{self.output_path}" + "\033[0m")
		self.embedding_size = 1024  # embedding dimensionality
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.embedding_size ':{self.embedding_size}" + "\033[0m")
		self.hidden_size = 2 * self.embedding_size  # hidden embedding
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.hidden_size ':{self.hidden_size}" + "\033[0m")

		print("------------一个跨所有数据集的联合问题词汇表----------------------------")
		# a joint question vocab across all dataset
		self.question_vocab_path = os.path.join(self.FVQA.common_data_path, 'question.vocab.json')  # 修改这里之后所有的预存文件（pt）都要删除
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.question_vocab_path ':{self.question_vocab_path}" + "\033[0m")
		
		print("---------------preprocess config----------------------")
		# preprocess config
		self.image_size = 448
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.image_size ':{self.image_size}" + "\033[0m")
		self.output_size = self.image_size // 32
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.output_size ':{self.output_size}" + "\033[0m")
		self.preprocess_batch_size = 100  # 64
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.preprocess_batch_size ':{self.preprocess_batch_size}" + "\033[0m")
		self.output_features = 2048
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.output_features ':{self.output_features}" + "\033[0m")
		self.central_fraction = 0.875
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.central_fraction ':{self.central_fraction}" + "\033[0m")
		
		print("--------------------Train params---------------------------")
		# Train params
		self.TRAIN = edict()
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN ':{self.TRAIN}" + "\033[0m")
		self.TRAIN.epochs = 600
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.epochs ':{self.TRAIN.epochs}" + "\033[0m")
		self.TRAIN.batch_size = 128  # 128
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.batch_size ':{self.TRAIN.batch_size}" + "\033[0m")
		self.TRAIN.lr = 5e-4  # default Adam lr 1e-3
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.lr ':{self.TRAIN.lr}" + "\033[0m")
		self.TRAIN.lr_decay_step = 3
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.lr_decay_step ':{self.TRAIN.lr_decay_step}" + "\033[0m")
		self.TRAIN.lr_decay_rate = .70
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.lr_decay_rate ':{self.TRAIN.lr_decay_rate}" + "\033[0m")

		# self.TRAIN.data_workers = 20
		self.TRAIN.data_workers = 8  # 10
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.data_workers ':{self.TRAIN.data_workers}" + "\033[0m")
		self.TRAIN.answer_batch_size = self.FVQA.max_ans  # batch size for answer network
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.answer_batch_size ':{self.TRAIN.answer_batch_size}" + "\033[0m")
		self.TRAIN.max_negative_answer = self.FVQA.max_ans  # max negative answers to sample
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TRAIN.max_negative_answer ':{self.TRAIN.max_negative_answer}" + "\033[0m")

		print("-----------Test params-------------------")
		# Test params
		self.TEST = edict()
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TEST ':{self.TEST}" + "\033[0m")
		self.TEST.batch_size = 128
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TEST.batch_size ':{self.TEST.batch_size}" + "\033[0m")
		self.TEST.max_answer_index = self.FVQA.max_ans  # max answer index for computing acc   853
		print("\033[92m" +f"'文件C:\ZS-F-VQA-main\code\config.py|类cfg|方法__init__|变量self.TEST.max_answer_index ':{self.TEST.max_answer_index}" + "\033[0m")

	'''
	argparse模块在Python中用于处理命令行参数。在你的代码中，argparse.ArgumentParser()创建了一个新的命令行
	参数解析对象，然后add_argument方法给它添加了参数。parse_args方法将命令行参数解析为结果对象，这个对象附带
	有参数及其值，可以像访问对象的属性一样访问这些值。这个结果对象并不是一个字典，而是一个"命名空间"。
	它的行为与字典有些不同。你可以使用.来访问对象的属性，就像访问对象的属性一样，而不需要用[]操作符。
	例如，args.top_fact。然而，如果你需要将这个对象转换为字典以便于某些操作（例如迭代），
	你可以使用vars()函数，如dict_args = vars(args)。
	
	'''
	def get_args(self):
		print("=================config.py get_args start:====================")
		parser = argparse.ArgumentParser()
		parser.add_argument('--gpu_id', default=1, type=int)
		parser.add_argument('--finetune', action='store_true')
		parser.add_argument('--batch_size', default=128, type=int)
		parser.add_argument('--max_ans', default=500, type=int)  # 3000 300##
		parser.add_argument('--loss_temperature', default=0.01, type=float)
		# parser.add_argument('--pretrained_model', default=None, type=str)
		parser.add_argument('--answer_embedding', default='MLP', choices=['RNN', 'MLP'])  # 答案编码：MLP or RNN##
		# parser.add_argument('--context_embedding', default='BoW', choices=['SAN', 'BoW'])  # Q I 内容编码：SAN or MLP
		parser.add_argument('--embedding_size', default=1024, choices=[1024, 300, 512], type=int)  # 答案编码：MLP or RNN##
		parser.add_argument('--epoch', default=800, type=int)  # 答案编码：MLP or RNN ##
		# choice model
		parser.add_argument('--fusion_model', default='SAN', choices=['MLP', 'SAN', 'UD', 'MUTAN', 'BAN', 'ViLBERT'])
		parser.add_argument('--requires_grad', default=0, type=int, choices=[0, 1])
		# choice class
		parser.add_argument('--method_choice', default='W2V', choices=['CLS', 'W2V', 'KG', 'GAE', 'KG_W2V', 'KG_GAE', 'GAE_W2V', 'KG_GAE_W2V'])
		parser.add_argument('--ans_fusion', default='Simple_concate', choices=['RNN_concate', 'GATE_attention', 'GATE', 'RNN_GATE_attention', 'Simple_concate'])
		# KG situation
		parser.add_argument('--KGE', default='TransE', choices=['TransE', 'ComplEx', "TransR", "DistMult"])  # 答案编码：MLP or RNN ##
		parser.add_argument('--KGE_init', default="w2v")  # None  # none or w2v ##
		parser.add_argument('--GAE_init', default="random")  # None  # random or w2v ##
		parser.add_argument('--ZSL', type=int, default=0)  # None  # random or w2v ##
		parser.add_argument('--entity_num', default="all", choices=['all', '4302'])  # todo: 完成不同子图情况的... ##

		parser.add_argument('--data_choice', default='0', choices=['0', '1', '2', '3', '4'])
		parser.add_argument('--name', default=None, type=str)  # 定义名字后缀

		parser.add_argument("--no-tensorboard", default=False, action="store_true")
		parser.add_argument("--exp_name", default="", type=str, required=True, help="Experiment name")
		parser.add_argument("--dump_path", default="dump/", type=str, help="Experiment dump path")
		parser.add_argument("--exp_id", default="", type=str, help="Experiment ID")
		parser.add_argument("--random_seed", default=4567, type=int)
		parser.add_argument("--freeze_w2v", default=1, type=int, choices=[0, 1])
		parser.add_argument("--ans_net_lay", default=0, type=int, choices=[0, 1, 2])
		parser.add_argument("--fact_map", default=0, type=int, choices=[0, 1])
		parser.add_argument("--relation_map", default=0, type=int, choices=[0, 1])

		parser.add_argument("--now_test", default=0, type=int, choices=[0, 1])
		parser.add_argument("--save_model", default=0, type=int, choices=[0, 1])

		parser.add_argument("--joint_test_way", default=0, type=int, choices=[0, 1])
		parser.add_argument("--top_rel", default=10, type=int)
		parser.add_argument("--top_fact", default=100, type=int)
		parser.add_argument("--soft_score", default=10, type=int)  # 10 or 10000
		parser.add_argument("--mrr", default=0, type=int)
		args = parser.parse_args()
		# print each argument and its properties
		for action in parser._actions:
			print('-----------------')
			print('Argument Name:', action.dest)
			print('Default Value:', action.default)
			print('Type:', action.type)
		return args

	def update_train_configs(self, args):
		self.gpu_id = args.gpu_id
		self.finetune = args.finetune
		self.answer_embedding = args.answer_embedding
		self.name = args.name
		self.no_tensorboard = args.no_tensorboard
		self.exp_name = args.exp_name
		self.dump_path = args.dump_path
		self.exp_id = args.exp_id
		self.random_seed = args.random_seed
		self.freeze_w2v = args.freeze_w2v
		self.loss_temperature = args.loss_temperature
		self.ZSL = args.ZSL
		self.ans_net_lay = args.ans_net_lay
		self.fact_map = args.fact_map
		self.relation_map = args.relation_map
		self.now_test = args.now_test
		self.save_model = args.save_model
		self.joint_test_way = args.joint_test_way
		self.top_rel = args.top_rel
		self.top_fact = args.top_fact
		self.soft_score = args.soft_score
		self.mrr = args.mrr

		if args.ZSL == 1:
			print("ZSL setting...")
			self.FVQA.test_data_path = self.FVQA.unseen_test_data_path
			self.FVQA.train_data_path = self.FVQA.seen_train_data_path

		if args.fusion_model == 'UD' or args.fusion_model == 'BAN':
			self.FVQA.feature_path = os.path.join(self.FVQA.common_data_path, 'fvqa_36.hdf5')
			self.FVQA.img_id2idx = os.path.join(self.FVQA.common_data_path, 'fvqa36_imgid2idx.pkl')
		self.requires_grad = True if args.requires_grad == 1 else False
		self.fusion_model = args.fusion_model
		self.TRAIN.batch_size = args.batch_size
		# self.TRAIN.answer_batch_size = args.answer_batch_size
		self.method_choice = args.method_choice
		self.ans_fusion = args.ans_fusion
		self.embedding_size = args.embedding_size
		self.FVQA.data_choice = args.data_choice
		self.FVQA.max_ans = args.max_ans
		self.TRAIN.epochs = args.epoch
		self.FVQA.KGE = args.KGE
		self.FVQA.KGE_init = args.KGE_init
		self.FVQA.gae_init = args.GAE_init
		self.FVQA.entity_num = args.entity_num

		if self.fact_map:
			self.FVQA.max_ans = 2791
		if self.relation_map:
			self.FVQA.max_ans = 103

		self.TEST.max_answer_index = self.FVQA.max_ans
		self.TRAIN.answer_batch_size = self.FVQA.max_ans  # batch size for answer network
		self.TRAIN.max_negative_answer = self.FVQA.max_ans

		self.FVQA.answer_vocab_path = os.path.join(self.FVQA.common_data_path, 'answer.vocab.fvqa.' + str(self.FVQA.max_ans) + '.json')

		if "KG" in self.method_choice:
			self.FVQA.relation2id_path = os.path.join(self.FVQA.kg_path, "relations_" + self.FVQA.entity_num + ".tsv")
			self.FVQA.entity2id_path = os.path.join(self.FVQA.kg_path, "entities_" + self.FVQA.entity_num + ".tsv")
			if self.KGE_init != "w2v":
				self.FVQA.entity_path = os.path.join(self.FVQA.kg_path, "fvqa_" + self.FVQA.entity_num + "_" + self.KGE + "_entity.npy")
				self.FVQA.relation_path = os.path.join(self.FVQA.kg_path, "fvqa_" + self.FVQA.entity_num + "_" + self.KGE + "_relation.npy")
			else:
				self.FVQA.entity_path = os.path.join(self.FVQA.kg_path, "fvqa_" + self.FVQA.entity_num + "_w2v_" + self.KGE + "_entity.npy")
				self.FVQA.relation_path = os.path.join(self.FVQA.kg_path, "fvqa_" + self.FVQA.entity_num + "_w2v_" + self.KGE + "_relation.npy")
