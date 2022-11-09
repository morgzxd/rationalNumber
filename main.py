def gcf(x, y):
    if x > y:
      for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
          gcf = i
          return gcf
    if y > x:
      for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
          gcf = i
          return gcf
          
class Rational:
    def __init__(self, numer, denom):
      self.n = numer
      self.d = denom
      
      try:
        self.n = int(self.n)
        self.d = int(self.d)
      except ValueError:
        print("Your numerator/denominator input was invalid.")
        self.n = int(input("Please re-enter numerator: "))
        self.d = int(input("Please re-enter denominator: "))

    def simplify(self):
      x = gcf(self.n, self.d)
      newnom = self.n / x
      newdenom = self.d / x
      return Rational(newnom, newdenom)

    def __add__(self, other):
      fn = self.n
      fd = self.d
      sn = other.n
      sd = other.d
      fn *= sd
      sn *= fd
      fd *= sd
      sd *= fd
      newnom = fn + sn
      newdenom = sd
      ans = Rational(newnom, newdenom)
      return ans.simplify()

    def __sub__(self, other):
      fn = self.n
      fd = self.d
      sn = other.n
      sd = other.d
      fn *= sd
      sn *= fd
      fd *= sd
      sd *= fd
      newnom = fn - sn
      newdenom = sd
      ans = Rational(newnom, newdenom)
      return ans.simplify()

    def __mul__(self, other):
      fn = self.n
      fd = self.d
      sn = other.n
      sd = other.d
      newnom = fn * sn
      newdenom = fd * sd
      ans = Rational(newnom, newdenom)
      return ans.simplify()

    def __truediv__(self, other):
      fn = self.n
      fd = self.d
      sn = other.d
      sd = other.n
      newnom = fn * sn
      newdenom = fd * sd
      ans = Rational(newnom, newdenom)
      return ans.simplify()
      
    def __str__(self):
      return "%d/%d" %(self.n, self.d)

def main():
  third = Rational(1,3)
  half = Rational(1,2)
  print(third.__truediv__(half))


if __name__ == '__main__':
    main()
