import helpers as h
import constants as c

class Category:
  name = None
  ledger = None
  balance = None

  def __init__(self, name):
    self.name = name
    self.ledger = list()
    self.balance = 0

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": "Transfer to " + category.name})
      self.balance -= amount
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False
  
  def check_funds(self, amount):
    return amount <= self.balance

  def __str__(self):
    return h.get_header(self.name) + h.get_lines(self.ledger) + h.get_total(self.balance)

def create_spend_chart(categories):
  spend_chart = c.SPEND_CHART_TITLE
  spendingSummary = h.get_spending_summary(categories)
  for i in range(c.Y_LABEL_MAX, c.Y_LABEL_MIN-1, -c.Y_LABEL_INCREMENT):
    spend_chart += h.get_bar_data(i, spendingSummary) + ' '
  spend_chart += h.get_x_axis(spendingSummary)
  spend_chart += h.get_x_labels(spendingSummary)
  return spend_chart