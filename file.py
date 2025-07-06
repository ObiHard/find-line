def second_index(text: str, some_str: str) -> int | None:
    count: int = 0
    start: int = 0
    while True:
        pos: int = text.find(some_str, start)
        if pos == -1:
            return None
        count += 1
        if count == 2:
            return pos
        start = pos + len(some_str)
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
