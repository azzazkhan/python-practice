# Example type casting for each data type
y = str("Hello world")
y = int(20)
y = float(20.5)
# Complex numbers cannot be converted into other numeric data types!
y = complex(1j)
y = list(("apple", "banana", "cherry"))
y = tuple(("apple", "banana", "cherry"))
y = dict(name="John", age=36)
y = set(("apple", "banana", "cherry"))
y = frozenset(("apple", "banana", "cherry"))
y = bool(5)
y = bytes(5)
t = bytearray(5)
y = memoryview(bytes(5))

z = int(5e2) # 5 into 10 raise to power 2 (5x10^2) exponential form