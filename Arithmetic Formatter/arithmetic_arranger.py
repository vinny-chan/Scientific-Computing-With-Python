import helpers as h
import constants as c

def get_arithmetic_arrangment(problems, showAnswer):
    firstLine = ""
    secondLine = ""
    thirdLine = ""
    fourthLine = ""

    for i in range(len(problems)):
      space = "" if i == 0 else " " * c.SPACE_BETWEEN_QUESTIONS

      p = problems[i].split()
      firstOperand = p[c.FIRST_OPERAND_POSITION]
      operator = p[c.OPERATOR_POSITION]
      secondOperand = p[c.SECOND_OPERAND_POSITION]

      questionWidth = h.getQuestionWidth(firstOperand, secondOperand)

      firstLine += space + h.getFirstLine(questionWidth, firstOperand)
      secondLine += space + h.getSecondLine(questionWidth, operator, secondOperand)
      thirdLine += space + h.getThirdLine(questionWidth)

      answer = h.getAnswer(firstOperand, operator, secondOperand)
      
      fourthLine += space + h.getFourthLine(questionWidth, answer)

    return firstLine + "\n" + secondLine + "\n" + thirdLine + ("\n" + fourthLine if showAnswer else "")

def arithmetic_arranger(problems, showAnswer = False):
    if not h.isValidNumberOfProblems(problems):
      return c.TOO_MANY_PROBLEMS

    if not h.isOperatorValid(problems):
      return c.INVALID_OPERATOR

    if not h.isOnlyDigits(problems):
      return c.INVALID_OPERAND

    if h.isNumberTooBig(problems):
      return c.TOO_MANY_DIGITS

    return get_arithmetic_arrangment(problems, showAnswer)