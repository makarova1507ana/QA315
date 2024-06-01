class Figure:
    def show_figure(self ):
        print("figure: ")
class Polygon(Figure):
    def __init__(self, *sides):
        self.sides = sides

    def valid_polygon(self):
        if len(self.sides) >= 3:
            if len(list(filter(lambda side: side > 0, self.sides))) == len(self.sides):
                return True
        return False

    def perimeter(self):
        if self.valid_polygon():
            return sum(self.sides)
        return -1  # НЕвалидный полигон