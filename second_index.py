def second_index(text, substring):
    first_index = text.find(substring)
    if first_index == -1:
        return None
    second_index = text.find(substring, first_index + 1)
    return second_index if second_index != -1 else None
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
