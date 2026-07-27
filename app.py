import streamlit as st

# 设置页面标题
st.set_page_config(page_title="Python 工具搜索引擎", page_icon="🔍")

# ========== 你的工具词典 ==========
tool_guide = {
    "把字符串的第一个字符改为大写，后面的小写": "capitalize()",
    "把整个字符串都小写": "casefold()",
    "编码str--bytes（二进制字符串）": "encode()",
    "解码": "decode()",
    "返回字符（sub）出现的次数，star：开始下标，stop：结束下标": "count(sub,start,stop)",
    "返回sub第一次出现的下标，查不到返回-1": "find(sub,start,stop)",
    "返回sub第一次出现的下标": "index(sub,start,stop)",
    "将字符串转为大写": "upper()",
    "将字符串转为小写": "lower()",
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
    "居中对齐字符串（填充指定字符）": "center(width, [fillchar])"
}

# ========== 搜索函数（修正了缩进逻辑） ==========
def search_tools(keyword):
    """根据输入的关键词（字符串），按字符匹配权重排序返回结果"""
    # 将关键词拆分成字符列表（保留顺序，但不影响权重）
    search_chars = list(keyword.strip())
    result = []
    for desc, func in tool_guide.items():
        weight = 0
        for ch in search_chars:
            if ch in desc:
                weight += 1
        # 只保留权重>0的匹配项
        if weight > 0:
            result.append((desc, func, weight))
    # 按权重从高到低排序
    result.sort(key=lambda x: x[2], reverse=True)
    return result

# ========== 网页界面 ==========
st.title("🔍 Python 工具搜索引擎")
st.write("根据输入的关键词（逐字符匹配），返回最相关的 Python 内置方法。")

# 用户输入
keyword = st.text_input("请输入你想搜索的关键词：", placeholder="例如：大写、文件、排序...")

# 搜索按钮
if st.button("🚀 搜索"):
    if keyword.strip():
        with st.spinner("正在匹配中..."):
            results = search_tools(keyword)
        
        # 显示匹配数量
        st.success(f"✅ 共匹配到 **{len(results)}** 个相关工具")
        st.write(f"关键词拆分为 {len(list(keyword.strip()))} 个字符：`{list(keyword.strip())}`")
        st.divider()
        
        if results:
            # 按顺序显示结果（带权重）
            for idx, (desc, func, weight) in enumerate(results, start=1):
                # 用表情、颜色区分权重高低（可选）
                if weight >= 3:
                    emoji = "⭐"
                elif weight >= 2:
                    emoji = "🔹"
                else:
                    emoji = "▫️"
                st.write(f"{emoji} **{idx}. 权重 {weight}**")
                st.write(f"   - 描述：{desc}")
                st.write(f"   - 方法：`{func}`")
                st.divider()
        else:
            st.warning("❌ 没有找到任何匹配的工具，请尝试其他关键词。")
    else:
        st.warning("⚠️ 请输入关键词后再搜索！")