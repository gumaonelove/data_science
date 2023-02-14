from train import all_combinations

import random


random.seed(10)

words=input("Путь к файлу\t>")


def predict(prefix=random.choices(words),lenght=None):
    text=str(prefix)+" "
    data_count, data_head = all_combinations(prefix)

    for i in range(lenght):
        new_word=random.choices(data_head, weights=data_count)
        new_word=str(new_word[0])
        text=text+str(new_word)+" "
        data_count, data_head = all_combinations(new_word)
    return text

print(predict("я", 100))