import os
import subprocess
import shutil

# 需要从Git历史中删除的文件路径列表。这应该是相对于仓库顶部的路径，不是绝对路径。
file_paths = ['C:\\ZS-F-VQA-main\\.git\\objects\\3b\\4f381a9dc608aaee6b6ad9d7d951f8ec7bdbf9',
              'C:\\ZS-F-VQA-main\\.git\\objects\\68\\4a276dddce58fe192607f1d3856ff10374788f',
              'C:\\ZS-F-VQA-main\\.git\\objects\\6e\\c5cc917825c7314a80323068d4d172873bc765',
              'C:\\ZS-F-VQA-main\\.git\\objects\\7f\\96e1796fe1d6b4b7bcfa047e0467086c4fc2b0',
              'C:\\ZS-F-VQA-main\\.git\\objects\\d3\\27d0fd8553fc733bb12ce11d494851e45a622f',
              'C:\\ZS-F-VQA-main\\.git\\objects\\d9\\695817b244c4e751faacff5f9410b1150eb202']


def remove_large_files(file_paths):
    shutil.rmtree(r'C:\ZS-F-VQA-main\other_tools\temp')
    # 替换为你的仓库 URL
    repo_url = 'https://github.com/brookecoming/ZS-F-VQA-main.git'
    # 克隆仓库
    subprocess.run(['git', 'clone', repo_url, 'temp'], check=True)

    # 验证目录存在
    if os.path.isdir('temp'):
        os.chdir('temp')

    # 遍历每个要删除的文件
    for file_path in file_paths:
        # 使用 git filter-branch 来删除文件的所有历史记录
        subprocess.run([
            'git', 'filter-branch', '--force', '--index-filter',
            f'git rm --cached --ignore-unmatch {file_path}',
            '--prune-empty', '--tag-name-filter', 'cat', '--', '--all'
        ], check=True)

    # 强制推送更新到远程仓库
    subprocess.run(['git', 'push', 'origin', '--force', '--all'], check=True)

    # 返回到上一个目录
    os.chdir('..')

    # 删除临时目录和克隆的仓库。在删除之前，请确保现在不在那个目录中
    if os.path.isdir('temp'):
        # For Windows
        subprocess.run(['rmdir', '/S', '/Q', 'temp'], shell=True)
        # For Unix-like system
        # subprocess.run(['rm', '-rf', 'temp'], check=False)


# 使用函数
remove_large_files(file_paths)
