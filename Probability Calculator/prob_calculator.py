import copy
import random
# Consider using the modules imported above.

class Hat:
  contents = None
  
  def __init__(self, **kwargs):
    self.contents = list()
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_of_balls):
    if num_of_balls <= len(self.contents):
      drawn_balls = list()
      for i in range(num_of_balls):
        rand = random.randint(0, len(self.contents)-1)
        drawn_balls.append(self.contents[rand])
        del self.contents[rand]
      return drawn_balls
    else:
      return self.contents



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_failed_experiments = 0
  for i in range(num_experiments):
    experiment_hat = copy.deepcopy(hat)
    drawn_balls = experiment_hat.draw(num_balls_drawn)
    actual_balls = dict()
    for ball in drawn_balls:
      actual_balls[ball] = actual_balls.get(ball, 0) + 1
    for key, value in expected_balls.items():
      if not key in actual_balls or actual_balls[key] < value:
        num_failed_experiments += 1
        break
  return (num_experiments - num_failed_experiments) / num_experiments  

