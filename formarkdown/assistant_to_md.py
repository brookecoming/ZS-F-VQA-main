class Assistant_to_md:
    def read_chat_records(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()

    file_path = 'chat_records.txt'
    chat_records = read_chat_records(file_path)

    # 输出读取的对话记录
    for record in chat_records:
        print(record.strip())  # .strip()用于去除每行末尾的换行符

Class Main:
if __name__ == '__main__':
    file_path = 'chat_records.txt'
    obj=  Assistant_to_md()
    obj.read_chat_records(file_path)

