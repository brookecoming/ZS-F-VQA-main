import os

def count_samples_in_files(directory, file_prefix):
    sample_counts = {}
    # 遍历目录下所有文件
    for filename in os.listdir(directory):
        # 检查文件名前缀以确定是训练样本还是测试样本
        if filename.startswith(file_prefix):
            # 构建完整的文件路径
            filepath = os.path.join(directory, filename)
            # 计算每个文件中的行数
            with open(filepath, 'r') as file:
                lines = file.readlines()
                sample_counts[filename] = len(lines)
    return sample_counts

# 设置文件夹路径（请根据实际情况修改）
directory = '.'

# 计算训练样本数量
train_prefix = 'train_list_'
train_sample_counts = count_samples_in_files(directory, train_prefix)

# 计算测试样本数量
test_prefix = 'test_list_'
test_sample_counts = count_samples_in_files(directory, test_prefix)

# 打印结果
print("Training samples count:")
for filename, count in train_sample_counts.items():
    print(f"{filename}: {count}")
    sum_train=sum(train_sample_counts.values())
print(f"Training sample totle:{sum_train}")

print("\nTesting samples count:")
for filename, count in test_sample_counts.items():
    print(f"{filename}: {count}")
    sum_test = sum(test_sample_counts.values())
print(f"Testing sample totle:{sum_test}")
print(f"training plus Testing samples count:{sum_train+sum_test}")