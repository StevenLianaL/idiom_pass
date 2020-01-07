import json
from collections import OrderedDict


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


def get_word(res: OrderedDict):
    tail_words = res[list(res.keys())[-1]]
    while True:
        if not tail_words:
            res.popitem()
            tail_words = res[list(res.keys())[-1]]
        else:
            break
    return tail_words.pop()


# 1. 运行 ok
# 2. 错误检查
# 3. 无法查询后退 ok
# 4. 重复词处理 ok
# 5. 最长备份
def auto_idiom(w: str = '啊一', limit: int = 1000):
    results = OrderedDict()
    for i in range(limit):
        if w in results.keys():
            w = get_word(results)
            continue
        words = get_match_idioms(w)
        if words:
            results[w] = words[:-1]  # in
        else:
            w = get_word(results)
            continue
        w = words[-1]  # new word
    return results.keys()


if __name__ == '__main__':
    for i in auto_idiom():
        print(i)
