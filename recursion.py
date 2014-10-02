#-------------------------------------------------------------------------------
# Name:        recursion.py
# Purpose:    to get comfortable with recursion functions and their use.
#
# Author:      SABASTIAN MUGAZAMBI
#
# Created:     01/06/2014
# Copyright:   (c) Sabastian Mugazambi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import sys
import random

def min(numList):
    """Given a list of numbers this functions checks for the smallest number and returns the smallest number"""
    if len(numList) <= 1:
            return numList[0]
    m = min(numList[1:])
    return m if m < numList[0] else numList[0]

def palindrome(word):
    """Checks if a word is a palindrome and returns True or False"""
    word = word.lower()
    word = word.strip(" ?,!~`\';:.(){}\"\"[]-_")

    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return palindrome(word[1:-1])

def testMIn():
    """Creates a random list of numbers from 0-20 and test whether
    the min() functtion works using the random list."""
    numList = []
    while len(numList) < 5:
        x = random.randrange(0,20)
        numList.append(x)

    print "your random list is:", (numList)
    print"the smallest number is: %d\n" %min(numList)

    #giving the option to try again or quit.
    action = raw_input("enter 'a' to try again or 'q' to close")
    if action == "a":
        testMIn()
    else:
        exit()

def testPalindrome():
    """This function tests the palindrome function written to identify palindromes"""
    #making a list of all the words and phrases to be used in the test.
    listed_words = ["amma", "ana",'"Do nine men interpret?" "Nine men," I nod',"peep","poop","redder","repaper","Do geese see god?","May a moody baby doom a yam?","are some of","are",
                    "babe","radio",'"Do nine men interpret?" "Nine men," I nod' ]

    #randomly picking a phrase or word to check from the list
    x = random.randrange(0, len(listed_words)-1)

    #prints the word randomly chosen and makes the call to palindrome then checks if the out put is true or false
    #prints the relative output.
    if palindrome(listed_words[x]) == True:
        print "Your phrase is: %s" %listed_words[x]
        print "It is a palindrome\n"
        action = raw_input("enter 'a' to try again or 'q' to quit")
    else:
        print "Your phrase is: %s" %listed_words[x]
        print "It is NOT a palindrome\n"
        action = raw_input("enter 'a' to try again or 'q' to close")
    if action == "a":
        testPalindrome()
    else:
        exit()


def drawSection(window,x1,y1,x2,y2,levels):
    """This is the function which has all the recursion required to draw the squareFractal.
    it includes some math as I had to calculate the points to be used to draw the square"""

    if levels > 0:

        # Draw the three little sections.Doing the math that maps the right points which would be used to draw the squares
        w = x2-x1
        first = drawSection(window,x1-w/4,y1-w/4,x2-(w/4)*3,y2-(w/4)*3,levels-1)
        second = drawSection(window,x1-w/4,y1+(w/4)*3,x2-(w/4)*3,y2+w/4,levels-1)
        third = drawSection(window,x1+(w/4)*3,y1+(w/4)*3,x2+w/4,y2+w/4,levels-1)
        fourth = drawSection(window,x1+(w/4)*3,y1-w/4,x2+w/4,y2-(w/4)*3,levels-1)

         # Draw the big triangle last
        main_square = Rectangle(Point(x1,y1),Point(x2,y2))
        main_square.draw(window)
        main_square.setFill("white")
        main_square.setOutline("black")

def squareFractal(levels):
    """This function creates the graphical window and makes a call to the drawSection()
     function which then draws the squares on to the window"""

    window = GraphWin('Fractal Square Demo', 800, 800)
    window.setBackground(color_rgb(255, 255, 255))
    window.setCoords(0,0,800,800)

    #Assigning variables to the initial two points used to draw the big square.
    #Passing them into a function which I wrote separately to avoid drawing the graphical window everytime.
    x1 ,y1,x2,y2= 300, 300,500, 500
    drawSection(window,x1,y1,x2,y2,levels)

    #waiting for raw_input from user before closing the window.
    raw_input("Hit Enter to quit")
    window.close()


def main():
##    testMIn()
##    testPalindrome()
    levels = 5
    squareFractal(levels)




if __name__ == '__main__':
    main()
