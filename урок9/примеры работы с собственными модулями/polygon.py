# P
def valid_polygon(*sides):
    if len(sides) >= 3:
        if len(list(filter(lambda side: side > 0, sides))) == len(sides):
            return True
    return False

def perimeter(*sides):
    if valid_polygon(*sides):
        return sum(sides)
    return -1 # НЕвалидный полигон