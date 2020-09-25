class Parent(type):
  def __new__(cls, name, bases, body):
    if 'name' not in body.keys() or body['name'].__class__.__name__ != 'property':
      raise TypeError(f"Can't instantiate class {name} without property name")
    return super().__new__(cls, name, bases, body)


class GoodChild(metaclass=Parent):
  @property # If I forget this, raise TypeError
  def name(self) -> str: # also, name must be implemented
    return 'good child'

print(GoodChild().name)

class BadChild1(metaclass=Parent):
  def name(self) -> str:
    return 'bad 1'

class BadChild2(metaclass=Parent):
  @property
  def name2(self) -> str:
    return 'bad 2'

if __name__ == '__main__':
  # print(GoodChild().name)
  print(BadChild1().name)
  print(BadChild2().name2)
