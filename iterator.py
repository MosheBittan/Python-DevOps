class countTo():
  max:int
  """this is iterable object
  Args:
    max:int - value for maximum number to iterate
  """
  def __init__(self,max):
    self.max = max

  def __iter__(self):
    return countToInt(self.max)

class countToInt():
  """this is iterator object
  Args:
    max:int - value for maximum number to iterate
    current:int - current number it is on 
  """
  max:int
  current:int

  def __init__(self, max:int):
    self.max = max
    self.current = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.current <= self.max:
      val_current = self.current
      self.current += 1
      return val_current
    raise StopIteration


test1 = countTo(5)
for i in test1:
  for j in test1:
    print(i,j)

