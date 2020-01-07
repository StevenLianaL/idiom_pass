import json
from collections import OrderedDict
from random import choice


def load_idioms():
    with open('idiom.json', encoding='utf8') as f:
        data = json.load(f)
    return data


idioms = load_idioms()
idiom_words = {i['word'] for i in idioms}


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
# 2. 错误检查 not
# 3. 无法查询后退 ok
# 4. 重复词处理 ok
# 5. 最长备份 not

def query_idiom():
    w = input('请输入成语：')
    return get_match_idioms(w)


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


def interact_user(is_start=True):
    pc_idiom, count = '', -1
    while True:
        user_idiom = input('请输入成语：')
        if not is_start:
            if user_idiom[0] != pc_idiom[-1] or user_idiom not in idiom_words:
                print(f'你答错了,当前分数：{count}')
                continue
        if match_words := get_match_idioms(user_idiom):
            count += 1
            pc_idiom = choice(match_words)
            print(f"我的接龙：--{pc_idiom}--")
            print("轮到你了：")
        else:
            print(f'恭喜你，你赢了! 当前分数：{count}')
            break
        is_start = False


if __name__ == '__main__':
    choices = ['1 成语接龙', '2 查询成语', '3 自动接龙']
    user_choice = int(input(rf"{' '.join(choices)} (1/2/3):"))
    if user_choice == 1:
        interact_user()
    elif user_choice == 2:
        print(query_idiom())
    elif user_choice == 3:
        print(auto_idiom())
    else:
        print('无此选项，请输入 1/2/3')
