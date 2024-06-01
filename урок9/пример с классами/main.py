# #import figures.polygon as polygon
# # from figures import polygon
# square = polygon.Polygon(3,3,3,3)
# print(square.perimeter())

from figures.polygon import Polygon

square = Polygon(3,3,3,3)
print(square.perimeter())
square.show_figure()