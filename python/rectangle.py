class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0

    def set_dimensions (self, h, w):
        self.width = w
        self.height = h
    
    def get_area (self):
        return self.width * self.height