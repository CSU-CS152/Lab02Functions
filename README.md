# Lab 02 - Functions
## Introduction
This lab introduces the idea of functions. Functions are self-contained parts of code meant for you to use over and over again instead of writing the same code multiple times. In this lab you will be asked to write a total of five functions. The first four functions will calculate the area of circle, rectangle, triangle, and trapezoid, respectively. The last function will print a statement about the shape given the type of shape and it's area passed in as arguments. We assume that the units are in centimeters. 

## Pre-Step: Application Flow

### Testing
An important aspect of programming includes testing your code to check for errors. A great way to test your program for this lab is to create function calls from your main method, print the returned value, and verify that the returned value is what you would expect it to be. 

## Step 1: Area of a Circle
The area of a circle is $\Pi$ * $radius^2$. $\Pi$ is declared as the variable PI and is initialized to 3.14 on the first line of code in this program. The circleArea function takes in only one parameter--the radius of that specific circle. It returns the area of that circle. 

## Step 2: Area of a Rectangle
A rectangle's area is length * width. Both length and width are passed into the function rectangleArea as parameters. The function returns the result of multiplying those two parameters. 

## Step 3: Area of a Triangle
The area of a triangle is (base*height) / 2. Base and height will be passed as parameters into triangleArea.

## Step 4: Area of a Trapezoid
Feel free to view following [link](https://www.cuemath.com/measurement/area-of-trapezoid/) to visualize the area of a trapezoid. 

The area is the 1/2 * (base1 + base2) * height. Three parameters are passed into this function--base1, base2, and height. 

## Step 5: Print Shape Information
After creating functions that will find the area of four shapes, we want to print out information about the shapes. Namely, we will print out a statment declaring the type of shape and it's area, both passed as parameters. If I passed in 'circle' as the type of the shape and 78.5 as the area, I want the function to print out:

The area of this circle is $78.5cm^2$

To be able to print out your area variable, cast the variable to a String type. 

Also note, the squared symbol is a special unicode symbol. It can be written into a String using the following sequence of characters: \u00b2. The following example shows the code and output that uses this special character.

Code:
``` python
'The rug covered 25ft\u00b2'
``` 
Output:

The rug covered 25ft²