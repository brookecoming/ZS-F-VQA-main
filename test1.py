import traceback
import inspect
import os


def print_context():
    stack = inspect.stack()
    frame = stack[1][0]
    info = inspect.getframeinfo(frame)
    _, filename = os.path.split(info.filename)
    module_name = os.path.splitext(filename)[0]  # remove extension

    print("引用信息：")
    print(f"文件名: {filename}")
    print(f"模块名: {module_name}")
    print(f"函数名: {info.function}")
    print(f"行号: {info.lineno}")


class Sample:
    def test(self):
        x = 10
        print_context()


Sample().test()
