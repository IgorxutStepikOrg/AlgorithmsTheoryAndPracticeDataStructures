def tree(tpl):
    dct = {}  # словарь, где ключ - родитель, значение - множество детей
    for index, apex in enumerate(tpl):
        if apex not in dct:
            dct.update({
                apex: {index},
            })
        else:
            dct[apex].add(index)

    return dct


def height_tree(dct):
    height = 0  # высота дерева

    # проверяем, что на вход поступило не пустое дерево
    try:
        stack = dct.get(-1).copy()  # корень дерева не имеет родителя

        # обходим дерево по уровням от родителей к детям
        while stack:
            height += 1

            # собираем детей со следующего уровня
            new_stack = set()
            for num in stack:
                apex = dct.get(num)
                if apex:
                    new_stack.update(apex)

            stack = new_stack.copy()

    finally:
        return height


n = int(input())
parents = tuple(map(int, input().split()))

print(height_tree(tree(parents)))
