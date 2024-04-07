
import os
import pytest
import json

from config import cfg
from deal_data import Runner  # 替换为包含Runner类的模块

class TestRunner:
    '''
    在此测试中，我们使用 mocker.patch.object 对 deal_fact 进行了替换，
    这样 deal_fact 的调用就会返回我们预设的值 'mocked_fact'。
    然后我们可以检查生成的 JSON 文件是否包含这个预设的值，
    以此来测试 get_new_all_json 是否正确调用了 deal_fact 函数。
    因此 pytest-mock 被用于该测试用例，对于没有安装 pytest-mock
    可以通过 pip install pytest-mock 来进行安装。

    '''

    def test_get_new_all_json(self,mocker):
        cfg1 = cfg()
        args = cfg1.get_args()
        cfg1.update_train_configs(args)
        runner_instance = Runner(cfg1)# 创建一个 Runner 类实例,替换为初始化参数


        # 定义数据路径和文件
        # runner_instance.data_path = "/path/to/data/dir"  # 更换为实际的数据目录
        print(f"runner_instance.data_path: {runner_instance.data_path}")
        # json_file_name = os.path.join(runner_instance.data_path, "all_qs_dict_release_combine_all.json") # 这是待处理的json文件，也更换为实际的文件命名
        json_file_name = os.path.join(runner_instance.data_path, "all_qs_dict_release_combine.json") # 这是待处理的json文件，也更换为实际的文件命名

        # 使用 mocker 对 deal_fact 进行简单模拟
        mocker.patch.object(Runner, 'deal_fact', return_value='mocked_fact')

        # 在测试开始前，确认文件不存在
        if os.path.exists(json_file_name):
            os.remove(json_file_name)

        # 调用我们需要测试的函数
        runner_instance.get_new_all_json()

        # 测试文件是否成功创建
        assert os.path.exists(json_file_name) is True

        # 另外，我们还可以进行一些额外的测试，比如检查文件内容是否满足预期，或者其他某种形式的输出检查
        with open(json_file_name, 'r') as file:
            data = json.load(file)
            # 在这里添加你的断言来检查具体的数据内容
            # 例如检查 deal_fact 是否正确被调用
            mocked_fact = 'mocked_fact'
            for _, value in data.items():
                assert mocked_fact in value['fact']

        # 测试完成后，删除文件
        if os.path.exists(json_file_name):
            os.remove(json_file_name)

    def test_get_new_json(self):
        self.fail()

    def test_get_entity_filter(self):
        self.fail()

    def test_get_all_entity(self):
        self.fail()

    def test_fusion_answer_and_entity(self):
        self.fail()

    def test_statistics_of_ans_and_entity(self):
        self.fail()

    def test_filter_top500_iqa_pair(self):
        self.fail()

    def test_deal_relation(self):
        self.fail()

    def test_split_data(self):
        self.fail()

    def test_preprocess_answer(self):
        self.fail()

    def test_preprocess_fact(self):
        self.fail()

    def test_preprocess_relation(self):
        self.fail()

    def test_split_unseen_data(self):
        self.fail()

    def test_get_fact_relation_matrix(self):
        self.fail()

    def test_preprocess_json_in_order(self):
        self.fail()

    def test_disjoint_judge(self):
        self.fail()

    def test_data_analysis(self):
        self.fail()

    def test_data_analysis_zsl_and_general(self):
        self.fail()
