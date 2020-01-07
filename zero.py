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


# 1. 运行 ok
# 2. 错误检查
# 3. 无法查询后退 ok
# 4. 重复词处理
# 5. 最长备份
def auto_idiom(w: str):
    results, backup = OrderedDict(), None
    while True:
        try:
            words = get_match_idioms(w)
            if words:
                results[w] = words[:-1]  # in
            else:
                if tail_words := results[list(results.keys())[-1]]:  # 处理无法接龙，新词重来
                    w = tail_words.pop()
                    continue
                else:
                    results.popitem()
                    w = results[list(results.keys())[-1]].pop()
                    continue
            print(f"{w=}")
            print(f"{results.keys()=}")
            w = words[-1]  # new word
        except Exception as e:
            print(f"{type(e)=},{e=}")
            print(list(results.items())[-2:])
            raise ValueError(f"new word {w=}")


if __name__ == '__main__':
    auto_idiom('啊鬼')
