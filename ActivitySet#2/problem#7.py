class Menu:
  """fill in class definition here"""
  def __init__(self,food,qty):
    self.food = food
    self.qty = str(qty)
  def __add__(self, o):
    q1 = self.food +' '+ self.qty
    q2 = o.food +' '+ o.qty
    return q1 + '\n' + q2
    
m1 = Menu("idly",10)
m2 = Menu("vada",20)
m = m1 + m2  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly