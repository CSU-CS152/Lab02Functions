PI = 3.14

def circleArea(radius):
    return PI*radius**2

def rectangleArea(length, width):
    return length * width

def triangleArea(base, height):
    return (height * base) / 2

def trapezoidArea(base1, base2, height):
    return ((base1+base2)/2)*height

def printShapeInfo(type, area):
    print('The area of this '+ type + ' is '+ str(area) +'cm\u00b2')


def main():
    #assume units are in cm
    #make diagram for each area
    circle = circleArea(5)
    printShapeInfo('circle', circle)

    rectangle = rectangleArea(6,7)
    printShapeInfo('rectangle', rectangle)

    triangle = triangleArea(6,7)
    printShapeInfo('triangle', triangle)

    trapezoid = trapezoidArea(1,3,4)
    printShapeInfo('trapezoid', trapezoid)


if __name__ == "__main__":
    main()
