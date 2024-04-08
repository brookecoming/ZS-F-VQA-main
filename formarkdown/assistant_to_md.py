class Assistant_to_md:
    def __init__(self):
        self.file_path = 'chat_records.txt'

    def read_chat_records(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.chat_records = file.readlines()

    def write_chat_records_to_md(self):
        # Create or open output.md in write mode
        with open('output.md', 'w', encoding='utf-8') as file:
            for record in self.chat_records:
                # Write each chat record to the file, add a newline character for formatting
                file.write(record.strip() + '\n')
class Main:
    def __init__(self):
        self.assistant = Assistant_to_md()

    def execute(self):
        self.assistant.read_chat_records(self.assistant.file_path)
        self.assistant.write_chat_records_to_md()
if __name__ == '__main__':
    main = Main()
    main.execute()
