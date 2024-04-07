import json
'''
1.在这个脚本中，我们首先导入了json模块来处理JSON数据。
2.count_knowledge_graph_relations函数接收一个JSON文件的路径作为输入，然后尝试打开和读取该文件。
3.使用json.load(file)将文件内容加载成一个Python对象（在这个案例中，应该是一个字典），然后通过计算字典的长度来得到知识图谱信息的总数，
因为每个键值对代表一个实体关系。

请确保替换json_file_path变量的值为你的JSON文件的实际路径。运行这个脚本后，它会打印出文件中包含的知识图谱实体关系的总数。
这个脚本简单明了，适用于统计具有上述结构的JSON文件中的实体关系数量。如果你的文件结构更复杂，可能需要做相应的调整来正确统计信息的数量。
'''
def count_knowledge_graph_relations(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # 假设每个键值对代表一个知识图谱信息
            num_relations = len(data)
            print(f"Total number of knowledge graph relations: {num_relations}")
    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")

# 替换成你的JSON文件路径
json_file_path = 'all_fact_triples_release.json'
count_knowledge_graph_relations(json_file_path)
