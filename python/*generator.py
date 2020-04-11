def game(guess, answer):
    result = (guess[i] == answer[i] for i in range(len(guess)))
    print(type(result))
    print(list(result))
    print(sum(guess[i] == answer[i] for i in range(len(guess))))


guess = [1, 2, 3]
answer = [1, 2, 3]
game(guess, answer)


# <class 'generator'>
# [True, True, True]
# 3
