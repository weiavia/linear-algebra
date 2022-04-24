
class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    # 向量的加法，返回一个新向量
    def __add__(self, another):
        assert len(self) == len(another),\
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, another)])
    
    # 向量的减法，返回一个新向量
    def __sub__(self, another):
        assert len(self) == len(another),\
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    # 向量数乘，返回一个新向量
    def __mul__(self, k):
        return Vector([k * e for e in self])

    # 向量数乘、右乘，返回一个新向量
    def __rmul__(self, k):
        return self * k

    # 返回向量取正的结果向量
    def __pos__(self):
        return 1 * self

    # 返回向量取负的结果向量
    def __neg__(self):
        return -1 * self

    # 代理list的迭代器
    def __iter__(self):
        return self._values.__iter__()

    # 取向量的第index个元素
    def __getitem__(self, index):
        return self._values[index]
        
    # 向量的维度
    def __len__(self):
        return len(self._values)

    # 系统打印所调用
    def __repr__(self) -> str:
        return "Vector({})".format(self._values)

    # 用户打印所调用
    def __str__(self) -> str:
        return "({})".format(", ".join(str (e) for e in self._values))