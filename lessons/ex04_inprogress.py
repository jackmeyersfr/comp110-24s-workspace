def extend(a: list[int], b: list[int]) -> None:
    indx_counter: int = 0
    while indx_counter < len(b):
        a = a.append(b[indx_counter])
        indx_counter += 1

a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
extend(a, b)