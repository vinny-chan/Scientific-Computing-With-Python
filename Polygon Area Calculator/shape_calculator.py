class Rectangle:
  width = None
  height = None

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width <= 50 and self.height <= 50:
      shape = ''
      for i in range(self.height):
        for j in range(self.width):
          shape += '*'
        shape += '\n'
      return shape
    else:
      return "Too big for picture."

  def get_amount_inside(self, shape):
    if shape.height <= self.height and shape.width <= self.width:
      fitVertically = self.height // shape.height
      fitHorizontally = self.width // shape.width
      return fitVertically * fitHorizontally
    else:
      return 0

  def __str__(self):
    return 'Rectangle(width={width}, height={height})'.format(width=self.width, height=self.height)

class Square(Rectangle):
  side = None

  def __init__(self, side):
    self.side = side
    Rectangle.__init__(self, side, side)

  def set_side(self, side):
    self.side = side
    Rectangle.set_height(self, side)
    Rectangle.set_width(self, side)

  def set_height(self, side):
    self.side = side
    Rectangle.set_height(self, side)

  def set_width(self, side):
    self.side = side
    Rectangle.set_width(self, side)

  def __str__(self):
      return 'Square(side={side})'.format(side=self.side)