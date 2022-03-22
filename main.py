from dataclasses import dataclass
from functools import reduce
from math import ceil


@dataclass(frozen=True)
class Possibilities:
    values: set

    def __add__(self, other):
        return self.operation(other, (lambda a, b: a+b))

    def __radd__(self, other):
        return self + other

    def __abs__(self):
        return Possibilities(set([abs(v) for v in self.values]))

    def __ceil__(self):
        return Possibilities(set([ceil(v) for v in self.values]))

    def __complex__(self):
        return Possibilities(set([complex(v) for v in self.values]))

    def __float__(self):
        return Possibilities(set([float(v) for v in self.values]))

    def __int__(self):
        return Possibilities(set([int(v) for v in self.values]))

    def __truediv__(self, other):
        return self.operation(other, (lambda a, b: a/b))

    def __rtruediv__(self, other):
        return self.operation(other, (lambda a, b: a/b), reversed=True)

    def __mul__(self, other):
        return self.operation(other, (lambda a, b: a*b))

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        return self.operation(other, (lambda a, b: a**b))

    def __sub__(self, other):
        return self.operation(other, (lambda a, b: a-b))

    def __divmod__(self, other):
        return self.operation(other, (lambda a, b: divmod(a, b)))

    def operation(self, value, fn, reversed=False):
        cfn = (lambda a, b: fn(b, a)) if reversed else fn
        m = [cfn(v, value) for v in self.values]
        if type(value) is Possibilities:
            return Possibilities(reduce(lambda a, b: a | b, m).values)
        else:
            return Possibilities(set(m))

    def __str__(self):
        return str(self.values)

    def __repr__(self) -> str:
        return f"Possibilities({repr(self.values)})"

    def __or__(self, other: "Possibilities"):
        return Possibilities(self.values.union(other.values))


P = Possibilities

print(P({-10, 10}) / 2)
