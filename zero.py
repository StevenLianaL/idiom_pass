import json
from collections import deque


def load_idioms():
    with open('idiom.json', encoding='utf8') as f:
        data = json.load(f)
    return data


idioms = load_idioms()


def get_match_idioms(word: str):
    last_char = word[-1]
    words = [i for i in idioms if i['word'][0] == last_char]
    if words:
        res = list({i['word'] for i in words})
        return res


def help_word(total_stack: deque, res_stack: list, word: str, reason: str):
    """辅助处理重复词、无词"""
    print(f"{word=} {reason=}")
    if not total_stack[-1]:  # 尾栈无词
        print('尾栈无词')
        total_stack.pop()
        res_stack.pop()
    res_stack.pop()  # 弹出旧词
    new_word = total_stack[-1].pop()
    return new_word


def run(w: str = ''):
    if not w:
        w = input('成语：')
    stack = deque()
    results = []
    while True:
        if len(results) >= 2:
            if not results[-1][0] == results[-2][-1]:
                raise ValueError('接龙错误')
        words = get_match_idioms(w)
        if words:  # 可接龙
            stack.append(words[:-1])  # 入栈
            results.append(w)  # 收集结果
        else:  # 不可接龙
            w = help_word(stack, results, w, '不可接龙')
            continue
        print(f"{w=}")
        print(f"{results=}")
        print(f"{words=}")
        with open('a.json', encoding='utf8', mode='w') as w:
            json.dump(list(stack), w, ensure_ascii=False)
        w = words[-1]  # 设置新词


if __name__ == '__main__':
    run('啊行')
