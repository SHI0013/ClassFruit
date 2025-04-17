class fruits:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def introduction(self):
        print("Hello, I am - ", self.name)


ob = fruits('Apple', 'Red')
ob.introduction()
