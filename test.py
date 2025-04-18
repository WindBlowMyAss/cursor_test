import os
import sys



if __name__ == "__main__":
    print("Hello, World!")

    # 获取当前目录
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")

    # 获取当前文件的绝对路径

    # 获取当前文件的相对路径
    relative_path = os.path.relpath(__file__)
    print(f"当前文件的相对路径: {relative_path}")

    # 获取当前文件的目录
    current_dir = os.path.dirname(__file__)
    print(f"当前文件的目录: {current_dir}")

    # 获取当前文件的文件名
    file_name = os.path.basename(__file__)
    print(f"当前文件的文件名: {file_name}")

    # 获取当前文件的文件名（不包含扩展名）


