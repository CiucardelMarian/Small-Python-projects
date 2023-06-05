from collections import Counter


class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        return Counter(my_list).most_common(1)[0][0]

    @classmethod
    def doubles(cls, my_list: list):
        counts = Counter(my_list)
        out_list = [i for i in counts if counts[i] > 1]
        return len(out_list)


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
