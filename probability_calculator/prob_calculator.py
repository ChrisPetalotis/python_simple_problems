import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, number in kwargs.items():
      for i in range(number):
        self.contents.append(color)

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    
    return random.sample(self.contents, number)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  totalMatches = 0
  for i in range(num_experiments):
    balls_drawn = hat.draw(num_balls_drawn)
    drawn = {}
    for ball in balls_drawn:
      drawn[ball] = drawn.get(ball, 0) + 1
    
    missed = False
    for color, number in expected_balls.items():
      if not color in drawn or drawn[color] < number:
        missed = True
        break
    if not missed: totalMatches += 1
    
  return totalMatches/num_experiments
