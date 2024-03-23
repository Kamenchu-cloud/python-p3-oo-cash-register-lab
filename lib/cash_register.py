#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.last_transaction_amount = 0

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([title] * quantity)
    self.last_transaction_amount = price * quantity

  def apply_discount(self):
    if self.discount > 0:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    self.total -= self.last_transaction_amount
    self.items = self.items[:-1]  
    self.last_transaction_amount = 0
