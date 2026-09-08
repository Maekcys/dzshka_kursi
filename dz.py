def count_vowels(s):
    all_vowels = 'aeyuio'
    count = 0
    for letter in s:
        if letter in all_vowels:
            count += 1
    return f"стики гласних:{count}"

print(count_vowels("hello world yo sobaki ya naruto ozumaki"))


def flatten_list(nested_list):
    big_list = []
    for sublist in nested_list:
        for item in sublist:
            big_list.append(item)
    return big_list

print(flatten_list([[1, 2], [3, 4], [5, 6]]))


def fibonacci(n):
    # начало с 0 1 1 и тд
    a = 0
    b = 1
    temp = 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    for i in range(n - 1):
        b += a
        a = temp
        temp = b

    return b

print(fibonacci(6))


# def reverse_string(word):
#     drow = ''
#     for letter in word:
#         temp = drow
#         drow = letter
#         drow += temp


#     return drow


# print(reverse_string('hihihaha 123'))
