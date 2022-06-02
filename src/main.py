PI = 3.14

def circleArea(radius):
    return 0

def rectangleArea(length, width):
    return 0

def triangleArea(base, height):
    return 0

def trapezoidArea(base1, base2, height):
    return 0

def shapeInfo(type, area):
    return ''


def main():
    #feel free to uncomment any of the following code in main
    #it is included here to help you test your program

    circle = circleArea(5)
    # print('TESTING', circleArea(5))
    # print('TESTING', shapeInfo('circle', circle))

    rectangle = rectangleArea(6,7)
    # print('TESTING', rectangleArea(6,7))
    # print('TESTING', shapeInfo('rectangle', rectangle))

    triangle = triangleArea(6,7)
    # print('TESTING', triangleArea(6,7))
    # print('TESTING', shapeInfo('triangle', triangle))

    strapezoid = trapezoidArea(1,3,4)
    # print('TESTING', trapezoidArea(1,3,4))
    # print('TESTING', shapeInfo('trapezoid', trapezoid))

if __name__ == "__main__":
    main()