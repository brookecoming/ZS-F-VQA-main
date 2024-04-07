import pyperclip
import time
import re

import re


def simple_markdown_converter(text):
    # 处理标题：假设"==="下一行文本为一级标题，"---"下一行文本为二级标题
    lines = text.split('\n')
    for i in range(len(lines)):
        if i > 0 and lines[i - 1].strip() == '===':
            lines[i] = f'# {lines[i]}'
        elif i > 0 and lines[i - 1].strip() == '---':
            lines[i] = f'## {lines[i]}'

    # 处理无序列表：假设以"- "开头的行为无序列表项
    lines = [f"- {line[2:]}" if line.startswith("- ") else line for line in lines]

    # 处理链接：简单识别URL并转换为Markdown链接格式
    processed_text = '\n'.join(lines)
    processed_text = re.sub(r'https?://[^\s]+', lambda x: f"[Link]({x.group(0)})", processed_text)

    return processed_text


def main():
    previous_text = ""
    while True:
        # 检查剪贴板内容是否有变化
        current_text = pyperclip.paste()
        if current_text != previous_text:
            print("检测到新的剪贴板内容。正在转换...")
            processed_text = simple_markdown_converter(current_text)
            # 将转换后的文本写回剪贴板
            pyperclip.copy(processed_text)
            previous_text = processed_text
            print("剪贴板内容已更新。")
        # 每隔一秒检查一次剪贴板
        time.sleep(1)


if __name__ == "__main__":
    main()
