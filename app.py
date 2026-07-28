import streamlit as st

# 设置页面标题
st.set_page_config(page_title="Python 工具搜索引擎", page_icon="🔍")

# ========== 按功能分组 ==========
group_string = {
    "把字符串的第一个字符改为大写，后面的小写": "capitalize()",
    "把整个字符串都小写": "casefold()",
    "编码str--bytes（二进制字符串）": "encode()",
    "解码": "decode()",
    "返回字符（sub）出现的次数，star：开始下标，stop：结束下标": "count(sub,start,stop)",
    "返回sub第一次出现的下标，查不到返回-1": "find(sub,start,stop)",
    "返回sub第一次出现的下标": "index(sub,start,stop)",
    "将字符串转为大写": "upper()",
    "将字符串转为小写": "lower()",
    "用指定字符串连接序列中的元素（常用于拼接）": "join(iterable)",
    "按指定分隔符拆分字符串，返回列表": "split(sep=None, maxsplit=-1)",
    "移除字符串首尾指定的字符（默认为空白）": "strip([chars])",
    "替换字符串中的旧子串为新子串": "replace(old, new, [count])",
    "格式化字符串（传入参数替换占位符）": "format(*args, **kwargs)",
    "检查字符串是否以指定前缀开头": "startswith(prefix, [start, end])",
    "检查字符串是否以指定后缀结尾": "endswith(suffix, [start, end])",
    "检查字符串是否全为字母": "isalpha()",
    "检查字符串是否全为数字": "isdigit()",
    "检查字符串是否全为字母或数字": "isalnum()",
    "检查字符串是否全为小写": "islower()",
    "检查字符串是否全为大写": "isupper()",
    "将字符串中的大写转换为小写，小写转大写（大小写互换）": "swapcase()",
    "将字符串按行拆分为列表（多行文本）": "splitlines([keepends])",
    "左对齐字符串（填充指定字符）": "ljust(width, [fillchar])",
    "右对齐字符串（填充指定字符）": "rjust(width, [fillchar])",
    "居中对齐字符串（填充指定字符）": "center(width, [fillchar])",
}

group_list_tuple_set = {
    "向列表中添加对象，并添加到末尾": "append()",
    "将可选代对象中数据分别添加到列表中，并添加到末尾": "extend(可选代对象)",
    "向指定下标位置添加对象": "insert(下标, 对象)",
    "清空列表": "clear()",
    "删除下标指定的元素，如果不加下标则删除最后一个元素": "pop()",
    "删除指定的对象": "remove(对象)",
    "删除变量或指定下表的值": "del",
    "浅拷贝": "copy()",
    "返回对象在列表中出现的次数": "count(对象)",
    "元素出现的第一次下标位置，也可自定义范围": "index(value, 开始下标, 结束下标)",
    "原地翻转": "reverse()",
    "快速排序，默认从小到大排序，key:算法": "sort(key=None, reverse=False)",
    "获取列表的长度（元素）": "len()",
    "返回元素在元组中出现的次数": "count(value)",
    "返回元素第一次出现的下标，查不到抛出异常": "index(value, [start, stop])",
    "向集合中添加元素（如果已存在则无变化）": "add(elem)",
    "清空集合": "clear()",
    "浅拷贝集合": "copy()",
    "返回两个集合的差集（在A但不在B）": "difference(other)",
    "从集合中移除指定元素，若不存在则忽略": "discard(elem)",
    "返回两个集合的交集": "intersection(other)",
    "从集合中随机移除并返回一个元素，若空则报错": "pop()",
    "移除指定元素，若不存在则报错": "remove(elem)",
    "返回两个集合的并集": "union(other)",
    "更新集合，添加另一个集合中的所有元素": "update(other)",
}

group_type_conversion = {
    "将整数转换为二进制字符串": "bin(x)",
    "将整数转换为八进制字符串": "oct(x)",
    "将整数转换为十六进制字符串": "hex(x)",
    "将对象转换为整数字符串（十进制）": "int(x, base=10)",
    "将对象转换为浮点数": "float(x)",
    "将对象转换为字符串": "str(object)",
    "将对象转换为布尔值": "bool(x)",
    "将对象转换为列表": "list(iterable)",
    "将对象转换为元组": "tuple(iterable)",
    "将对象转换为字典": "dict(iterable)",
    "将对象转换为集合": "set(iterable)",
    "创建固定集合（不可变集合）": "frozenset(iterable)",
    "将对象转换为字节数组": "bytearray(source)",
    "将对象转换为字节串": "bytes(source)",
}

group_math = {
    "返回一个数的绝对值": "abs(x)",
    "返回数字的幂（x 的 y 次方）": "pow(x, y, z=None)",
    "返回商和余数": "divmod(a, b)",
    "返回最大值（可传入多个参数或可迭代对象）": "max(iterable, *args)",
    "返回最小值（可传入多个参数或可迭代对象）": "min(iterable, *args)",
    "四舍五入到指定小数位数": "round(number, ndigits=None)",
    "求多个数的和（从 start 开始累加）": "sum(iterable, start=0)",
}

group_iteration = {
    "返回一个枚举对象，生成包含索引和值的元组": "enumerate(iterable, start=0)",
    "生成一个整数序列（用于循环）": "range(stop, start=0, step=1)",
    "返回可迭代对象的长度（元素个数）": "len(s)",
    "返回可迭代对象中元素是否全部为真": "all(iterable)",
    "返回可迭代对象中是否有任一元素为真": "any(iterable)",
    "对可迭代对象进行排序，返回新列表": "sorted(iterable, key=None, reverse=False)",
    "反转序列，返回迭代器": "reversed(seq)",
    "将多个可迭代对象打包成元组迭代器": "zip(*iterables)",
    "创建迭代器（不断重复整个可迭代对象）": "cycle(iterable)",
}

group_io = {
    "从标准输入读取一行字符串": "input(prompt='')",
    "打印对象到文本流": "print(*objects, sep=' ', end='\\n')",
    "打开文件并返回文件对象": "open(file, mode='r', encoding=None)",
}

group_object_reflection = {
    "返回对象的类型": "type(object)",
    "返回对象的内存地址": "id(object)",
    "检查对象是否是指定类的实例": "isinstance(object, classinfo)",
    "检查类是否是另一个类的子类": "issubclass(class, classinfo)",
    "返回对象的可打印字符串（供开发者调试）": "repr(object)",
    "返回对象的字符串表示（供用户阅读）": "str(object)",
    "返回对象的哈希值": "hash(object)",
    "设置对象的属性值": "setattr(object, name, value)",
    "获取对象的属性值": "getattr(object, name, default=None)",
    "检查对象是否有指定属性": "hasattr(object, name)",
    "删除对象的属性": "delattr(object, name)",
    "调用对象（当对象是可调用时）": "callable(object)",
}

group_other_builtins = {
    "返回字符的 Unicode 码点（ASCII 码）": "ord(c)",
    "返回 Unicode 码点对应的字符": "chr(i)",
    "计算表达式的值（动态执行代码）": "eval(expression, globals=None, locals=None)",
    "执行代码块（可执行多行代码）": "exec(object, globals=None, locals=None)",
    "创建帮助页面（交互式查看文档）": "help([object])",
    "返回对象的属性列表和内置方法": "dir([object])",
    "全局变量字典": "globals()",
    "局部变量字典": "locals()",
    "格式化值（按指定格式）": "format(value, format_spec='')",
    "返回对象的可打印表示（ASCII 转义非 ASCII）": "ascii(object)",
    "获取异步可迭代对象的迭代器": "aiter(iterable)",
    "获取异步迭代器的下一项": "anext(iterator, default)",
}
importable_modules = {
    # ===== 数学与随机 =====
    "数学运算模块（三角函数、对数、阶乘等）": "import math",
    "生成随机数的模块": "import random",
    "日期和时间处理模块": "import datetime",
    "日历相关功能模块": "import calendar",
    "统计函数模块（均值、中位数、方差等）": "import statistics",

    # ===== 数据结构与算法 =====
    "高效容器数据类型（deque、Counter、defaultdict等）": "import collections",
    "高效循环和组合生成器（排列、组合、笛卡尔积等）": "import itertools",
    "高阶函数工具（partial、lru_cache等）": "import functools",
    "操作符函数模块（替代 lambda）": "import operator",

    # ===== 文件与系统 =====
    "操作系统接口（文件和目录操作）": "import os",
    "高级文件操作（复制、移动、删除）": "import shutil",
    "面向对象的文件路径操作": "import pathlib",
    "系统相关参数和函数（命令行参数、退出等）": "import sys",

    # ===== 文件格式 =====
    "读写 CSV 文件": "import csv",
    "JSON 编码与解码": "import json",
    "配置文件解析器（.ini 文件）": "import configparser",
    "解析 XML 文件": "import xml.etree.ElementTree as ET",

    # ===== 数据持久化 =====
    "Python 对象序列化（保存到文件）": "import pickle",
    "轻量级数据库（SQLite）": "import sqlite3",

    # ===== 网络与互联网 =====
    "URL 处理模块（请求、解析）": "import urllib.request",
    "HTTP 请求模块（更高级的客户端）": "import requests",        # 需单独安装
    "发送电子邮件的模块（SMTP）": "import smtplib",

    # ===== 文本处理 =====
    "正则表达式匹配操作": "import re",
    "字符串通用操作（常量、模板）": "import string",
    "计算文本差异（对比文件）": "import difflib",
    "自动换行和文本填充": "import textwrap",

    # ===== 加密与安全 =====
    "安全散列函数（MD5、SHA 等）": "import hashlib",
    "消息认证码（HMAC）": "import hmac",

    # ===== 压缩与归档 =====
    "读写 ZIP 存档文件": "import zipfile",
    "读写 tar 存档文件": "import tarfile",
    "gzip 文件压缩和解压": "import gzip",

    # ===== 二进制数据处理 =====
    "将字节解析为打包的二进制数据": "import struct",
    "高效的数值数组（类似 C 的数组）": "import array",

    # ===== 并发与异步 =====
    "线程操作模块": "import threading",
    "多进程操作模块": "import multiprocessing",
    "异步 I/O 模块": "import asyncio",

    # ===== 图形界面 =====
    "Tkinter 图形界面库": "import tkinter",
}

# 将 importable_modules 也作为一个组
group_modules = importable_modules   # 直接使用你已定义的字典

# 将所有分组放入一个列表，每个元素为 (组名, 字典)
all_groups = [
    ("字符串方法", group_string),
    ("列表/元组/集合", group_list_tuple_set),
    ("类型转换", group_type_conversion),
    ("数学运算", group_math),
    ("迭代与序列", group_iteration),
    ("输入输出与文件", group_io),
    ("对象与反射", group_object_reflection),
    ("其他内置函数", group_other_builtins),
    ("模块导入", group_modules),
]
# 所有分组名称列表（用于下拉选择框）
group_names = ["全部"] + [name for name, _ in all_groups]


def search_tools(keyword, group_filter="全部"):
    """
    根据关键词和组别过滤进行搜索
    - keyword: 搜索关键词
    - group_filter: 组名，如果为"全部"则搜索所有组
    """
    search_chars = list(keyword.strip())
    results = []

    # 如果选择的是"全部"，遍历所有组；否则只遍历选中的组
    groups_to_search = all_groups if group_filter == "全部" else [(group_filter, dict(all_groups))]  # 注意这里需要找到对应的字典

    # 更稳健的做法：遍历 all_groups，根据名称判断
    for group_name, group_dict in all_groups:
        if group_filter != "全部" and group_name != group_filter:
            continue
        for desc, func in group_dict.items():
            weight = 0
            for ch in search_chars:
                if ch in desc:
                    weight += 1
            if weight > 0:
                results.append((desc, func, weight, group_name))

    results.sort(key=lambda x: x[2], reverse=True)
    return results


# ========== 网页界面 ==========
# 使用两列布局，增加第一列宽度占比，确保不会换行
col1, col2 = st.columns([4, 1], gap="small")

with col1:
    # 隐藏 label，只保留占位符
    keyword = st.text_input(
        "搜索关键词",  # 这个 label 会被隐藏，但为了可访问性保留
        placeholder="例如：大写、文件、排序...",
        label_visibility="collapsed"
    )

with col2:
    # 同样隐藏下拉框的 label
    selected_group = st.selectbox(
        "选择类别",
        group_names,
        index=0,
        label_visibility="collapsed"
    )


# 搜索按钮
if st.button("🚀 搜索"):
    if keyword.strip():
        with st.spinner("正在匹配中..."):
            results = search_tools(keyword, selected_group)

        # 显示匹配数量
        st.success(f"✅ 共匹配到 **{len(results)}** 个相关工具")
        st.write(f"关键词拆分为 {len(list(keyword.strip()))} 个字符：`{list(keyword.strip())}`")
        if selected_group != "全部":
            st.write(f"🔍 当前筛选组别：`{selected_group}`")
        st.divider()

        if results:
            for idx, (desc, func, weight, group) in enumerate(results, start=1):
                if weight >= 3:
                    emoji = "⭐"
                elif weight >= 2:
                    emoji = "🔹"
                else:
                    emoji = "▫️"
                st.write(f"{emoji} **{idx}. 权重 {weight}**  [组别：`{group}`]")
                st.write(f"   - 描述：{desc}")
                st.write(f"   - 方法：`{func}`")
                st.divider()
        else:
            st.warning("❌ 没有找到任何匹配的工具，请尝试其他关键词。")
    else:
        st.warning("⚠️ 请输入关键词后再搜索！")
