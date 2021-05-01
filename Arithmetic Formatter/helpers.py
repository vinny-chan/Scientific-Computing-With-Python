def isValidNumberOfProblems(problems):
  return len(problems) <= 5

def isOperatorValid(problems):
  for problem in problems:
    p = problem.split()
    if p[1] == '+' or p[1] == '-':
      continue
    else:
      return False
  return True

def isOnlyDigits(problems):
  for problem in problems:
    p = problem.split()
    if p[0].isdigit() and p[2].isdigit():
      continue
    else:
      return False
  return True

def isNumberTooBig(problems):
  for problem in problems:
    p = problem.split()
    if len(p[0]) > 4 or len(p[2]) > 4:
      return True
    else:
      continue
  return False

def getQuestionWidth(firstOperand, secondOperand):
  return max(len(firstOperand), len(secondOperand)) + 2

def getFirstLine(questionWidth, firstOperand):
  return " " * (questionWidth - len(firstOperand)) + firstOperand

def getSecondLine(questionWidth, operator, secondOperand):
  return operator + " " * (questionWidth - len(operator) - len(secondOperand)) + secondOperand

def getThirdLine(questionWidth):
  return "-" * questionWidth

def getAnswer(firstOperand, operator, secondOperand):
  additionAnswer = int(firstOperand) + int(secondOperand)
  subtractionAnswer = int(firstOperand) - int(secondOperand)
  return additionAnswer if operator == '+' else subtractionAnswer

def getFourthLine(questionWidth, answer):
  return " " * (questionWidth - len(str(answer))) + str(answer)