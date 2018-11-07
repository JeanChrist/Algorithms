def is_sorted(li):
    before = float('-inf')
    for i in li:
        if i < before:
            return False
        before = i

    return True


# def div(a, b):
#     _l = a % b
#     if _l == 0:
#         return b
#     return div(b, _l)


def quick_sort(li) -> list:
    left_li, right_li = [], []

    if len(li) < 2:
        return li

    pivot, rest_li = li[0], li[1:]
    for i in rest_li:
        if i < pivot:
            left_li.append(i)
        else:
            right_li.append(i)
    # print(left_li, right_li)
    return quick_sort(left_li) + [pivot] + quick_sort(right_li)


def main():
    import random
    li = [random.randint(1, 100) for _ in range(10)]

    print(li)

    sorted_li = quick_sort(li)
    print(sorted_li)
    print(is_sorted(sorted_li))


if __name__ == '__main__':
    main()
