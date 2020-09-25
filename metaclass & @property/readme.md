### [Ensure child class adds the property decorator](https://stackoverflow.com/questions/63550842/how-to-override-an-abstract-property-method-without-forgetting-to-add-the-proper/63552878#63552878)

So, `Child` must have `@property` by `name` here:
```
class Parent(metaclass=ABCMeta):
  @property
  @abstractmethod
  def name(self) -> str:
    pass

class Child(Parent):
  @property ## If I forget this, I want Python to yell at me.
  def name(self) -> str:
    return 'The Name'

if __name__ == '__main__':
  print(Child().name)
```

**Solution : `metaclass`**

```
class Parent(type):
  def __new__(cls, name, bases, body):
    if 'name' not in body.keys() or body['name'].__class__.__name__ != 'property':
      raise TypeError(f"Can't instantiate class {name} without property name")
    return super().__new__(cls, name, bases, body)
```
