"""Реализуем структуру бинарного дерева:
Вставка и удаление элемента, поиск, подсчет количества и вывод дерева"""

"""Класс Node используется для задания узла

Attributes
----------
value : int
    числовое значение узла
left : int
    числовое значение левого дочернего узла
right : int
    числовое значение правого дочернего узла
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res

"""Класс BinaryTree используется для задания бинарного дерева

Attributes
----------
root : int
    числовое значение корневого элемента
leng : int
    количество элементов в дереве

Methods
-------
add()
    Добавляет элемент в бинарное дерево
search()
    Поиск элемента в дереве, возвращает элемент и его родителя
delete()
    Удаляет элемент в бинарном дереве
show_tree()
    Вывод элементов дерева в одну строку
print_tree()
    Вывод дерева в след. структуре для всех узлов в дереве:
        Значение узла  - Значение левого дочернего узла - Значение правого дочернего узла
"""
class BinaryTree:

    def __init__(self, value):
        self.root = Node(value)
        self.leng = 1


    def add(self,value):
        """Метод добавляет элемент в бинарное дерево

        Parameters
        ----------
        value : int
            значение узла, которое необходимо добавить """
        res = self.search(self.root, value)
        if res[0] is None:
            new_node = Node(value)
            self.leng += 1
            if value < res[1].value:
                res[1].left = new_node
            else:
                res[1].right = new_node
        else:
            print('Не возможно вставить значение')

    def search(self, node, value, parent=None):
        """Метод поиска элемента в бинарном дереве

        Parameters
        ----------
        value : int
            значение узла, которое необходимо найти """
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def delete(self, value):
        """Метод удаляет элемент в бинарное дерево

        Parameters
        ----------
        value : int
            значение узла, которое необходимо удалить """
        if self.root is None:
            return None
        node,parent = self.search(self.root, value)
        if node is None:
            return None
        else:
            if node.left is None and node.right is None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            elif node.left is None and node.right is not None:
                node = node.right
                if node.value < parent.value:
                    parent.left = node
                else:
                    parent.right = node
            elif node.left is not None and node.right is None:
                node = node.left
                if node.value < parent.value:
                    parent.left = node
                else:
                    parent.right = node
            else:
                right = node.right
                left = node.left
                new_node = node.left
                while new_node.right is not None:
                    new_node = new_node.right
                node = new_node
                node.left = left
                node.right = right

    def show_tree(self,node, level):
        """Метод отображает бинарное дерево в следующей структуре:
        корень
        ___уровень 1
        ______уровень 2
        _________уровень 3
        ___уровень 1
        ______уровень 2
        Здесь уровень 1 - дочерние элементы корневого элемента
        Уровень 2 - дочерние элементы, элементов уровня 1
        Уровень 3 - дочерние элементы, элементов уровня 2
        и так далее...

        Parameters
        ----------
        node : Node
            узел, от которого необходимо нарисовать дерево вниз
        level : int
            уровень, который отображает уровень прохождения в глубину дерева"""
        if node is None:
            print(f"Дерево пустое")
            return
        print(level * 3 * '_' + str(node.value))
        if node.left:
            self.show_tree(node.left, level + 1)
        if node.right:
            self.show_tree(node.right, level + 1)

    def print_tree(self, node):
        """Метод отображает бинарное дерево в несколько строк, каждая строка отображает узел и его дочерние элементы
        узел - левый дочерний элемент - правый дочерний элемент

        Parameters
        ----------
        node : Node
            узел, от которого необходимо нарисовать дерево вниз"""
        print(node)
        if node.left:
            self.print_tree(node.left)
        if node.right:
            self.print_tree(node.right)

bt = BinaryTree(5)
bt.add(3)
bt.add(7)
bt.add(4)
bt.add(10)
bt.add(15)
bt.add(12)
print(bt.show_tree(bt.root,0))
bt.delete(10)
bt.delete(3)
print(bt.show_tree(bt.root,0))
bt.print_tree(bt.root)
