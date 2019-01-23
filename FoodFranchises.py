# CodeAcademy Project on Python Objects and Classes by Adam Stebbing 1/22/2019
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return self.name
  def calculate_bill(self, purchased_items):
    cost = [v for k, v in self.items.items() if k in purchased_items]
    return sum(cost)
  
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available = []
    for x in self.menus:
      if x.start_time <= time and x.end_time >= time:
        available.append(x)
    return available
  
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return self.name
  
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1500)
early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 1500, 1800)
dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 1700, 2300)
kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)

arepas_menu = Menu("Take a' Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 1000, 2000)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])

fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas = Business("Take A' Arepa", [arepas_place])

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))
print(arepas)
