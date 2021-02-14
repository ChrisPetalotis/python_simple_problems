import re

def arithmetic_arranger(problems, showResult=False):
  print(problems)
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  operator = ''
  arranged_problems = []

  for problem in problems:
    if '+' in problem:
      operator = '+'
    elif '-' in problem:
      operator = '-'
    else:
      return "Error: Operator must be '+' or '-'."

    numbers = re.findall('[0-9\w]+', problem)
    maxLength = 0
    result = None
    for number in numbers:
      if re.search('[^0-9]', number):
        return 'Error: Numbers must only contain digits.'
      
      numLength = len(number)
      if numLength > 4:
        return 'Error: Numbers cannot be more than four digits.'
      
      if numLength > maxLength:
        maxLength = numLength

      if not result:
        result = int(number)
      else:
        if operator == '+':
          result += int(number)
        else:
          result -= int(number)

    lineLength = maxLength + 2
    
    topLine = ' '*(lineLength - len(numbers[0])) + numbers[0].strip()
    bottomLine = operator + ' '*(lineLength - 1 - len(numbers[1])) + numbers[1].strip()
    dashes = '-'*lineLength
    result = ' '*(lineLength-len(str(result))) + str(result)

    arranged_problems.append({
      'topLine': topLine, 
      'bottomLine': bottomLine, 
      'dashes': dashes, 
      'result': result
    })

  toPrint = (' '*4).join([r['topLine'] for r in arranged_problems]) + '\n'
  toPrint += (' '*4).join([r['bottomLine'] for r in arranged_problems]) + '\n'
  toPrint += (' '*4).join([r['dashes'] for r in arranged_problems])
  if showResult:
    toPrint += '\n' + (' '*4).join([r['result'] for r in arranged_problems])

  return toPrint