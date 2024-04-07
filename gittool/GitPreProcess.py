import json
import os

import shutil

class GitPreProcess:
    def __init__(self):
        print("\033[91m----------start:   GitPreProcess--->__init__   ---------\033[0m")

        self.origin_folder = "C:\\ZS-F-VQA-main"  # Replace with your project path
        self.max_size_mb = 100  # Set max file size limit
        self.ignored_folder = ['venv', '.venv', '.git', '.idea']  # Folders to ignore during the search
        self.target_folder = 'C:\\DATA'  # Replace with your target path
        self.bigfile_list = "C:\\ZS-F-VQA-main\gittool\\bigfile_list.txt"
        self.bigfile_origin_new_list = "C:\\ZS-F-VQA-main\gittool\\bigfile_origin_new_list.txt"
        print("\033[91m============end:   GitPreProcess--->__init__   ========\033[0m")

    def check_large_files(self):
        print("\033[91m----------start:   GitPreProcess--->check_large_files   ---------\033[0m")

        if self.ignored_folder is None:
            self.ignored_folder = []
        large_files = []
        for root, dirs, files in os.walk(self.origin_folder):
            dirs[:] = [d for d in dirs if d not in self.ignored_folder]
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                if file_size > self.max_size_mb:
                    large_files.append(file_path)
        with open(self.bigfile_list, 'w') as f:
            for file in large_files:
                f.write("%s\n" % file)
        print(
            f"C:\ZS-F-VQA-main\gittool\GitPreProcess.py -> GitPreProcess -> \033[91mcheck_large_files -> large_files\033[0m-> : {large_files}")
        print("\033[91m============end:   GitPreProcess--->check_large_files   ========\033[0m")

        return large_files

    # def move_files_to(self, large_files):
    #     print("\033[91m----------start:   GitPreProcess--->move_files_to   ---------\033[0m")
    #
    #     moved_files = []
    #     for file_path in large_files:
    #         new_path = os.path.join(self.target_folder, os.path.basename(file_path))
    #         shutil.move(file_path, new_path)
    #         moved_files.append((file_path, new_path))
    #
    #     with open(self.bigfile_origin_new_list, "w") as f:
    #         for original, new in moved_files:
    #             #     f.write(original + "," + new + "\n")
    #             paths = [original, new]
    #             # 使用 json.dumps 将数组转换为字符串，并写入文件
    #             f.write(json.dumps(paths) + "\n")
    #
    #             # 现在，你可以使用 `original` 和 `new`
    #     print(
    #         f"C:\ZS-F-VQA-main\gittool\GitPreProcess.py -> GitPreProcess -> \033[91mmove_files_to -> moved_files\033[0m-> : {moved_files}")
    #     print("\033[91m============end:   GitPreProcess--->move_files_to   ========\033[0m")
    def move_files_to(self, large_files):
        print("\033[91m----------start:   GitPreProcess--->move_files_to   ---------\033[0m")
        sum = 0
        from typing import List
        moved_files = []  # [(origin, new), ...]

        # Move files to target folder
        for file_path in large_files:
            new_path = os.path.join(self.target_folder, os.path.basename(file_path))
            shutil.move(file_path, new_path)  # Move the file to target folder
            moved_files.append((file_path, new_path))  # Keep track of file move
            sum += 1
        print(f"移走的文件个数 : {sum}")

        # Write all moves to file
        with open(self.bigfile_origin_new_list, "w") as f:
            for original, new in moved_files:
                paths = [original, new]
                f.write(json.dumps(paths) + "\n")

        # Remove moved files from the bigfile_list
        moved_origins = [original for original, new in moved_files]  # List of original file locations

        # Read all files from bigfile_list file
        file_list = []
        with open(self.bigfile_list, "r") as f:
            for line in f:
                file_path = line.strip()
                if file_path not in moved_origins:
                    file_list.append(file_path)
        # Rewrite bigfile_list with remaining files
        with open(self.bigfile_list, "w") as f:
            for file_path in file_list:
                f.write(file_path + "\n")
        print("\033[91m============end:   GitPreProcess--->move_files_to   ========\033[0m")

    # def move_files_back(self):
    #     print("\033[91m----------start:   GitPreProcess--->move_files_back   ---------\033[0m")
    #
    #     with open(self.bigfile_origin_new_list, "r") as f:
    #         for line in f:
    #             original, new = line.strip().split(",")
    #             if os.path.exists(new):
    #                 os.makedirs(os.path.dirname(original), exist_ok=True)
    #                 print(
    #                     f"C:\ZS-F-VQA-main\gittool\GitPreProcess.py -> GitPreProcess -> \033[91mmove_files_back -> new\033[0m-> : {new}")
    #                 shutil.move(new, original)
    #     print("\033[91m============end:   GitPreProcess--->move_files_back   ========\033[0m")
    def move_files_back(self):
        import json
        import shutil
        import os
        print("\033[91m----------start:   GitPreProcess--->move_files_back   ---------\033[0m")

        with open(self.bigfile_origin_new_list, "r") as f:
            for line in f:
                original, new = json.loads(line.strip())  # Load paths from JSON
                if os.path.exists(new):
                    os.makedirs(os.path.dirname(original), exist_ok=True)
                    print(f"\033[91mmove_files_back -> new\033[0m-> : {new} to {original}")
                    shutil.move(new, original)

        print("\033[91m----------end:   GitPreProcess--->move_files_back   ---------\033[0m")
if __name__ == "__main__":
    obj = GitPreProcess()
    large_files = obj.check_large_files()
    # Move large files to target_folder
    # obj.move_files_to(large_files)
    #
    # # Later, when you want to move files back:
    # obj.move_files_back()
    large_files = obj.check_large_files()
