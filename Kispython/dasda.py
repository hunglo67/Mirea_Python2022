class main:
    def __init__(self):
        self.condition = 'A'

    def speed(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'C':
            self.condition = 'D'
            return 2
        elif self.condition == 'D':
            self.condition = 'B'
            return 5
        elif self.condition == 'E':
            self.condition = 'F'
            return 6
        elif self.condition == 'F':
            self.condition = 'A'
            return 7
        else:
            raise KeyError

    def spawn(self):
        if self.condition == 'B':
            self.condition = 'C'
            return 1
        elif self.condition == 'C':
            self.condition = 'F'
            return 3
        elif self.condition == 'F':
            self.condition = 'D'
            return 8
        elif self.condition == 'D':
            self.condition = 'E'
            return 4
        else:
            raise KeyError

o = main()
print(o.speed())
print(o.spawn())
print(o.spawn())
print(o.speed())
print(o.speed())
print(o.speed())
print(o.spawn())
print(o.speed())
print(o.spawn())
print(o.speed())
print(o.spawn())
print(o.speed())


