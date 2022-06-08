# Lab 02 - Functions
## Introduction
This lab introduces the idea of functions. Functions are self-contained parts of code meant for you to use over and over again instead of writing the same code multiple times. In this lab, you will be asked to write a total of five functions. The first four functions will calculate the area of a circle, a rectangle, a triangle, and a trapezoid, respectively. The last function will print a statement about the shape. We assume that the units are in centimeters. 

### Testing
An important aspect of programming includes testing your code to check for errors. A great way to test your program for this lab is to create function calls from your main method, print the returned value, and verify that the returned value is what you would expect it to be. Your program currenlty contains eight lines of code in main that are specified for testing. Feel free to uncomment and use them as you develop your program. 

PLEASE NOTE: You need to delete (or comment out) each print('TESTING', ...) statement before turning in your completed program. Failure to do so may negatively impact your grade. 

## Pre-Step: Application Flow

## Step 1: Area of a Circle
The area of a circle is $\Pi$ * $radius^2$. $\Pi$ is declared as the variable PI and is initialized to 3.14 on the first line of code in this program. The circleArea function takes in only one parameter--the radius of that specific circle. It returns the area of that circle. If you are stuck, please see the Review section below on how a function that returns the area of a square is implemented and called. 


Example function calls and return value:

| Function call | Return value   |
|---|---|
| circleArea(1)  | 3.14   | 
| circleArea(2)  | 12.56  | 
| circleArea(8)  | 200.96 |
|   |   | 

## Step 2: Area of a Rectangle
A rectangle's area is length * width. Both length and width are passed into the function rectangleArea as parameters. The function returns the result of multiplying those two parameters. 

Example function calls and return value:

| Function call | Return value   |
|---|---|
| retangleArea(1,3)    | 3  | 
| rectangleArea(2,4)   | 8  | 
| rectangleArea(8,10)  | 80 |
|   |   | 

## Step 3: Area of a Triangle
The area of a triangle is (base*height) / 2. Base and height will be passed as parameters into triangleArea.


Example function calls and return value:

| Function call | Return value   |
|---|---|
| triangleArea(1,2)  | 1.0  | 
| triangleArea(3,6)  | 9.0  | 
| triangleArea(3,7)  | 10.5 |
|   |   | 

## Step 4: Area of a Trapezoid
Feel free to view following [link](https://www.cuemath.com/measurement/area-of-trapezoid/) to visualize the area of a trapezoid. 

The area is the 1/2 * (base1 + base2) * height. Three parameters are passed into this function--base1, base2, and height. 


Example function calls and return value:

| Function call | Return value   |
|---|---|
| trapezoidArea(1,2,2)  | 3.0   | 
| trapezoidArea(2,4,7)  | 21.0  | 
| trapezoidArea(9,5,13) | 91.0  |
|   |   | 

## Step 5: Shape Information
After creating functions that will find the area of four shapes, we want to create a function that will return a string containing information about the shapes. Namely, we will return a statment declaring the type of shape and it's area, both passed as parameters. If I passed in 'circle' as the type of the shape and 78.5 as the area, I want the function to print out:

The area of this circle is $78.5cm^2$

Please see the Review section at the bottom of this document on how to utilize string formatting. Also note, the squared symbol is a special unicode symbol. It can be written into a String using the following sequence of characters: \u00b2. The following example shows the code and output that uses this special character. See the review for more examples.

Code:
``` python
'The rug covered 25ft\u00b2'
``` 
Output:

The rug covered 25ft²


Example function calls and return value:

| Function call | Return value   |
|---|---|
| shapeInfo('circle',10.0)        | The area of this circle is 10.00cm²     | 
| shapeInfo('rectangle', 14)      | The area of this rectangle is 14.00cm²  | 
| shapeInfo('trapezoid', 12.555)  | The area of this trapezoid is 12.555cm² |
|   |   | 

We can also pass in variable as parameters. 

```python
shape = 'circle'
area = 100.00
```
| Function call | Return value   |
|---|---|
| shapeInfo(shape,area)        | The area of this circle is 100.00cm²      | 


## Submitting Your Code
To receive credit for this lab you need to submit the lab for grading in Zybooks after clicking through the canvas link again!


## Review 
### Functions

The following function will calculate the area of a square. I start the function by using the keyword def. I then create the function's name, squareArea. Finally, I write in the parameters. In this case, I am using one parameter named sideLength. 

Inside of the function, I am creating a variable called area and assigning it to sideLength squared--the area of any square. I then return the area variable. 

``` python
def squareArea(sideLength):
    area = sideLength*sideLength
    return area
```
### Function Calls
The line of code shown below is a function call. It is used to tell my program that I want to execute a certain function. I am using 3 as my sideLength. 

``` python
squareArea(3)
```

I can also assign a function call to a variable. As shown below, I am assigning the variable square to my function call where 4 is the parameter. My square variable will be assigned to whatever my function call returns. In this case, square will be assigned to 16. 

```python
square = squareArea(4)

print(square) #this will print 16
```

### String Formatting
String formatting allows you to input variables and different characters into a string. This can be useful when you want to print statements where certain inputs may change. The following examples shows how to input a float into your string. Note: using .2f will output to 2 decimal places while .1f will output a single decimal place. 

```python
    milesRanToday = 4.56
    marathon = 26.2188

    statement = 'Today I ran %.2f miles.' %milesRanToday
    affirmation = 'I am going to run %.1f miles one day' %marathon

    print(statement)
    print(affirmation)
```
Output: 
Today I ran 4.56 miles. 
I am going to run 26.2 miles one day.


### Unicode
While not talked about in lecture, we want you to write one unicode character for this lecture. Unicode characters are special characters interpreted by the compiler using a hexidecimal number for encoding. 

Below are some examples of unicode characters. 

```python
#example unicode for dollar sign
print('I have \u002420 in my pockets')
#\u0024 is the unicode and the last 20 will be interpreted as normal
```
Output: I have $20 in my pockets. 

``` python
#example unicode for smiley face
print("Hi there! \U0001F600")
```
Output: Hi there! 😀
