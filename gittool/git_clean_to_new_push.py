import subprocess


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error executing {command}: {error}")
    return output


def main():
    commands = [
        "git rm --cached C:\ZS-F-VQA-main\data\KG_VQA\fvqa\exp_data\images\images\fvqa-resnet-14x14.h5",

        "git checkout --orphan newBranch",
        # 创建一个名为 "newBranch" 的新分支，这个分支是一个孤立分支
        # ，即它不会继承来自master分支的历史记录。
        "git add .",
        # 添加当前目录下所有的新文件或已修改的文件到git的暂存区，
        # 准备进行下一次提交。'.' 代表当前目录。
        "git commit -m 'Initial commit'",
        # 提交暂存区中的所有文件并创建新的 commit，
        # commit 信息为 'Initial commit'。
        "git branch -D master",
        # 删除本地的 "master" 分支。'-D' 选项会强制删除，即使该分支没有被合并。
        "git branch -m master"
        # 将当前分支重命名为 "master"。
        # '-m' 是 '--move' 的缩写，表示移动或重命名分支。
        "git lfs ls -files"
        # 列出所有已追踪的 LFS 文件。你需要找出那个超过 2 GB 的文件，然后确定是否还需要它。如果文件不再需要，你可以直接从你的仓库中删除它。
    ]

    for cmd in commands:
        print(run_command(cmd).decode())
    print("You will need to manually force push the changes: git push -f origin master")


if __name__ == '__main__':
    main()
