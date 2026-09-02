from typing import List


def sort_words(words: List[str]) -> List[str]:
        n_words = []
        for i in words:
            n = len(i)
            n_words.append(n)

        for i in range(len(n_words)-1):
            for j in range(len(n_words)-1):
                if n_words[j] < n_words[j+1]:
                    temp = words[j]
                    words[j] = words[j+1]
                    words[j+1] = temp

                    n_temp = n_words[j]
                    n_words[j] = n_words[j+1]
                    n_words[j+1] = n_temp 


        return words


def sort_numbers(numbers: List[int]) -> List[int]:

    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1):
            if abs(numbers[j]) > abs(numbers[j+1]):
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp


    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
