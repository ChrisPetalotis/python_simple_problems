class Category:
  def __init__(self, type):
    self.type = type
    self.balance = 0
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})
    self.balance += amount

  def withdraw(self, amount, description=''):
    if not self.check_funds(amount):
      return False

    self.ledger.append({'amount': -float(amount), 'description': description})
    self.balance -= amount

    return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if not self.check_funds(amount):
      return False

    descriptionTo = 'Transfer to ' + category.type
    self.withdraw(amount, descriptionTo)
    descriptionFrom = 'Transfer from ' + self.type
    category.deposit(amount, descriptionFrom)

    return True

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    return True

  def __str__(self, length=30):
    headerSideLength = (length - len(self.type))//2
    toPrint = '*'*headerSideLength + self.type + '*'*headerSideLength + '\n'

    for item in self.ledger:
      amount = str(item['amount'])
      if not '.' in amount:
        amount += '.00'
      elif len(amount.split('.')[1]) < 2:
        amount += '0'
      
      amountLength = len(amount)
      descLength = len(item['description'])

      toPrint += item['description'][:23]
      if descLength > 23:
        toPrint += ' '
      else:
        toPrint +=  ' '*(length - amountLength - descLength)
      toPrint += amount + '\n'
    
    toPrint += 'Total: ' + str(self.balance)

    return toPrint

def create_spend_chart(categories):
  percentages = [' '*(3-len(str(per))) + str(per) +'|' for per in range(100, -1, -10)]
  names = []
  spentAmounts = []
  totalSpent = 0
  for c in categories:
    spent = 0
    for entry in c.ledger:
      if entry['amount'] < 0:
        spent -= entry['amount']
        spentAmounts.append(spent)
        totalSpent += spent
    names.append(c.type)
  
  for amount in spentAmounts:
    percentage = (amount/totalSpent) *100
    percentage -= percentage % 10
    percentages = [p + ' o ' if percentage >= int(p.split('|')[0]) else p + '   ' for p in percentages]
    
  
  initialSpaces = ' '*4
  joinedPercs = ' \n'.join(percentages) + ' \n'
  dashes = initialSpaces + '-'*(len(percentages[0]) - 3) + '\n'
  joinedNames = ''

  maxLength = len(max(names, key=len))
  for i in range(maxLength):
    joinedNames += initialSpaces + ' '
    for name in names:
      try:
        joinedNames += name[i]
      except:
        joinedNames += ' '
      joinedNames += '  '
    
    if i < maxLength - 1:
      joinedNames += '\n'

  return 'Percentage spent by category\n' + joinedPercs + dashes + joinedNames
