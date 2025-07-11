#!/usr/bin/env python3

class CashRegister:
  def __init__(self,  discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
      self._discount = 0



  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    self.items.extend([item] * quantity)
    self.previous_transactions.append({
      'item': item,
      'price': price,
      'quantity': quantity,
    })

      
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
      return 
    discount_amount = self.total * (self.discount / 100)
    self.total -= int(discount_amount) 
    print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      print("No transactions to void.")
      return 
    last = self.previous_transactions.pop()
    item = last["item"]
    price = last["price"]
    quantity = last["quantity"]
    self.total -= price * quantity 
    for _ in range(quantity):
      if item in self.items:
        self.items.remove(item)
        
