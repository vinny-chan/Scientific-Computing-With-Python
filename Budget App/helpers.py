import constants as c

def get_header(name):
  numberOfStars = c.HEADER_LENGTH - len(name)
  halfNumberOfStars = numberOfStars // 2
  header = "*" * halfNumberOfStars + name + "*" * halfNumberOfStars + "*"
  return header[:c.HEADER_LENGTH]

def get_lines(ledger):
  lines = ""
  for item in ledger:
    amount = str(c.TWO_DECIMAL_FORMAT % item["amount"])[:c.MAX_AMOUNT_LENGTH]
    description = item["description"][:c.MAX_DESCRIPTION_LENGTH]
    space = " " * (c.HEADER_LENGTH - len(description) - len(amount))
    lineItem = "\n" + description + space + amount
    lines += lineItem
  return lines

def get_total(balance):
  return "\nTotal: " + str(c.TWO_DECIMAL_FORMAT % balance)

def get_spending_summary(categories):
  summary = list()
  for category in categories:
    categorySpending = 0
    for item in category.ledger:
      amount = item['amount']
      if amount < 0:
        categorySpending += -amount
    summary.append({
      'category': category.name,
      'spending': categorySpending
    })
  totalSpending = sum(s['spending'] for s in summary)
  for s in summary:
    s['percentage'] = s['spending'] / totalSpending
  return summary
  
def get_bar_data(percentage, spendingSummary):
  bar_data = '\n' + ' ' * (c.Y_LABEL_SPACE - len(str(percentage))) + str(percentage) + '|'
  for ss in spendingSummary:
    if ss['percentage'] >= percentage / 100:
      bar_data += ' o '
    else:
      bar_data += ' ' * c.BAR_WIDTH
  return bar_data
    
def get_x_labels(spendingSummary):
  x_labels = ''
  longestCategoryName = max(len(ss['category']) for ss in spendingSummary)
  for i in range(longestCategoryName):
    x_labels += '\n' + ' ' * c.Y_LABEL_PLUS_AXIS_SPACE
    for ss in spendingSummary:
      if len(ss['category']) > i:
        x_labels += ' {letter} '.format(letter=ss['category'][i])
      else:
        x_labels += ' ' * c.BAR_WIDTH
    x_labels += ' '
  return x_labels

def get_x_axis(spendingSummary):
  return '\n' + ' ' * c.Y_LABEL_PLUS_AXIS_SPACE + '-' * (c.BAR_WIDTH * (len(spendingSummary)) + 1)