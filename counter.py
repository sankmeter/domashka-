from collections import Counter

def find_unique_value(numbers):
    count = Counter(numbers)
    for num, freq in count.items():
        if freq == 1:
            return num
print(find_unique_value([1, 1, 2, 2, 3]))