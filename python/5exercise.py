sentence = 'This is a common interview question'
unpack = [*sentence.lower()]


# 递归：减而治之
# def find_max_count(unpack):
#     if len(unpack) == 1:
#         return unpack[0], 1
#     son_unpack = unpack[:-1]
#     last_character = unpack[-1]
#     count_last = 1
#     son_max_character, son_max_count = find_max_count(son_unpack)
#     for character in son_unpack:
#         if character == last_character:
#             count_last += 1
#     if count_last >= son_max_count:
#         max_character = last_character
#         max_count = count_last
#     else:
#         max_character = son_max_character
#         max_count = son_max_count
#     return max_character, max_count


# print(find_max_count(unpack))


# 字典
def find_max_count2(unpack):
    dic = {}
    for character in unpack:
        if character in dic:
            dic[character] += 1
        else:
            dic[character] = 1
    dic_list = dic.items()
    dic_lsit_sort = sorted(
        dic_list,
        key=lambda kv: kv[1],
        reverse=True
    )
    return dic_lsit_sort[0]


print(find_max_count2(unpack))
