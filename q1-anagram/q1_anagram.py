from collections import Counter

def anagram(a, b):

    count_a = Counter(a)
    count_b = Counter(b)

    result_a = 0
    result_b = 0

    for key in count_a:
        if key in count_b.keys():
            difference = count_a[key] - count_b[key]
            if difference > 0:
                result_a += difference
            else:
                result_b += -difference
        else:
            result_a += count_a[key]

    for key in count_b:
        if not key in count_a.keys():
            result_b += count_b[key]

    return result_a, result_b


if __name__ == "__main__":
    a = input("Please enter string one:")
    b = input("Please enter string two:")

    if not (a.isalpha() and b.isalpha()):
        print("At least one of the strings is not valid")
    else:
        res1, res2 = anagram(a,b)

        if res1 + res2 == 0:
            print("they are anagrams")
        else:
            print("remove {} character(s) from \'{}\' and {} character(s) from \'{}\'".format(res1, a, res2, b))
