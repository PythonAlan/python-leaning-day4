#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan

from tkinter.constants import *
import tkinter

class Calculator():
    """A calculator program."""

    def __init__(self):
        """Sets up the calculator GUI. """


        # Memory
        self.register = [None, None]
        self.pointer = 0

        # Flags for telling calculator which operation to do
        self.flag = {'add': False,
                      'subtract': False,
                      'multiply': False,
                      'divide': False}

        # Main/Root container
        self.root = tkinter.Tk()
        self.root.title("Calculator")

        # Text variable to be displayed inside the "LCD"
        self.text_value = tkinter.StringVar()

        self.frame = tkinter.Frame(self.root, bg = 'red')
        self.frame.pack(fill = BOTH, expand = 1)

        self.create_widgets()

        # Main loop to listen for events
        self.root.mainloop()


    def create_widgets(self):
        """
        Method for the creation/placement of buttons/labels.
        """

        # "LCD" screen
        self.display = tkinter.Label(self.frame, textvariable = self.text_value, bg = 'gray')
        self.display.grid(row = 0, column = 0, columnspan = 5, sticky = NSEW)

        # One button
        self.one = tkinter.Button(self.frame, text='1', command = self.one)
        self.one.grid(row = 1, column = 0, sticky = NSEW)

        # Two button
        self.two = tkinter.Button(self.frame, text='2', command = self.two)
        self.two.grid(row = 1, column = 1, sticky = NSEW)

        # Three button
        self.three = tkinter.Button(self.frame, text='3', command = self.three)
        self.three.grid(row = 1, column = 2, sticky = NSEW)

        # Four button
        self.four = tkinter.Button(self.frame, text='4', command = self.four)
        self.four.grid(row = 2, column = 0, sticky = NSEW)

        # Five button
        self.five = tkinter.Button(self.frame, text='5', command = self.five)
        self.five.grid(row = 2, column = 1, sticky = NSEW)

        # Six button
        self.six = tkinter.Button(self.frame, text='6', command = self.six)
        self.six.grid(row = 2, column = 2, sticky = NSEW)

        # Seven button
        self.seven = tkinter.Button(self.frame, text='7', command = self.seven)
        self.seven.grid(row = 3, column = 0, sticky = NSEW)

        # Eight button
        self.eight = tkinter.Button(self.frame, text='8', command = self.eight)
        self.eight.grid(row = 3, column = 1, sticky = NSEW)

        # Nine button
        self.nine = tkinter.Button(self.frame, text='9', command = self.nine)
        self.nine.grid(row = 3, column = 2, sticky = NSEW)

        # Zero button
        self.zero = tkinter.Button(self.frame, text='0', command = self.zero)
        self.zero.grid(row = 4, column = 1, sticky = NSEW)

        # Clear button
        self.clear = tkinter.Button(self.frame, text = 'Clear', command = self.clear)
        self.clear.grid(row = 4, column = 0, sticky = NSEW)

        # Plus button
        self.add = tkinter.Button(self.frame, text = '+', command = self.add)
        self.add.grid(row = 1, column = 3, sticky = NSEW)

        # Minus button
        self.subtract = tkinter.Button(self.frame, text = '-', command = self.subtract)
        self.subtract.grid(row = 2, column = 3, sticky = NSEW)

        # Multiply button
        self.multiply = tkinter.Button(self.frame, text = '*', command = self.multiply)
        self.multiply.grid(row = 3, column = 3, sticky = NSEW)

        # Divide button
        self.divide = tkinter.Button(self.frame, text = '/', command = self.divide)
        self.divide.grid(row = 4, column = 3, sticky = NSEW)

        # Equals button
        self.equals = tkinter.Button(self.frame, text = '=', command = self.equals)
        self.equals.grid(row = 4, column = 2, sticky = NSEW)

        # Make widgets spread out to fill screen when window is resized.
        # This is accomplished by configuring the rows and columns of a widget's
        # parent.
        self.root.rowconfigure(0, weight = 1)

        self.root.columnconfigure(0, weight = 1)

        self.frame.columnconfigure(0, weight = 1)
        self.frame.columnconfigure(1, weight = 1)
        self.frame.columnconfigure(2, weight = 1)
        self.frame.columnconfigure(3, weight = 1)


        self.frame.rowconfigure(0, weight = 1)
        self.frame.rowconfigure(1, weight = 1)
        self.frame.rowconfigure(2, weight = 1)
        self.frame.rowconfigure(3, weight = 1)
        self.frame.rowconfigure(4, weight = 1)


    """
    Set of functions to display the number pressed.
    Number is also saved into calculator's memory (register).
    """
    def zero(self):
        # Display number '0'
        self.text_value.set('0')
        self.register[ self.pointer ] = 0

    def one(self):
        # Display number '1'
        self.text_value.set('1')
        self.register[ self.pointer ] = 1

    def two(self):
        # Display number '2'
        self.text_value.set('2')
        self.register[ self.pointer ] = 2

    def three(self):
        # Display number '3'
        self.text_value.set('3')
        self.register[ self.pointer ] = 3

    def four(self):
        # Display number '4'
        self.text_value.set('4')
        self.register[ self.pointer ] = 4

    def five(self):
        # Display number '5'
        self.text_value.set('5')
        self.register[ self.pointer ] = 5

    def six(self):
        # Display number '6'
        self.text_value.set('6')
        self.register[ self.pointer ] = 6

    def seven(self):
        # Display number '7'
        self.text_value.set('7')
        self.register[ self.pointer ] = 7

    def eight(self):
        # Display number '8'
        self.text_value.set('8')
        self.register[ self.pointer ] = 8

    def nine(self):
        # Display number '9'
        self.text_value.set('9')
        self.register[ self.pointer ] = 9

    def clear(self):
        """
        Clears The "LCD" screen by setting it to zero.
        Also resets calculator's memory.
        """
        self.text_value.set('0')
        self.register[0] = None
        self.register[1] = None
        self.pointer = 0

        # Reset all operations
        for key in self.flag:
            self.flag[key] = False

    def add(self):
        """
        Saves the number currently displayed on the screen into
        the calculator's memory (register).

        The pointer for the register is then incremented to tell
        the calculator to expect another operand.
        """

        self.flag['add'] = True
        # Increment the pointer so next number can be
        # saved in memory
        # pointer can only be 0 or 1 [0,1]
        self.pointer = (self.pointer + 1) % 2

    def subtract(self):
        """
        Saves the number currently displayed on the screen into
        the calculator's memory (register).

        The pointer for the register is the incremented to tell
        the calculator to expect another operand.
        """
        self.flag['subtract'] = True
        # Increment pointer so next number may
        # be saved into memory
        self.pointer = (self.pointer + 1) % 2

    def multiply(self):
        """
        Saves the number currently displayed on the screen into
        the calculator's memory (register).

        The pointer for the register is the incremented to tell
        the calculator to expect another operand.
        """
        self.flag['multiply'] = True
        # Increment pointer so next number may
        # be saved into memory
        self.pointer = (self.pointer + 1 ) % 2

    def divide(self):
        """
        Saves the number currently displayed on the screen into
        the calculator's memory (register).

        The pointer for the register is the incremented to tell
        the calculator to expect another operand.
        """
        self.flag['divide'] = True
        self.pointer = (self.pointer + 1) % 2

    def equals(self):
        """
        Takes the operand saved in register with operand
        displayed on screen. Uses operator selected by User.

        Also handles the special case of DivisionByZero
        """
        if self.flag['add']:
            sum = self.register[0] + self.register[1]
            self.text_value.set( sum )

            # Reset Flags, pointers, memory, etc...
            self.flag['add'] = False
            self.pointer = 0
            # For adding multiple numbers together easily
            # (Chaining operations together)
            self.register[0] = sum

        if self.flag['subtract']:
            difference = self.register[0] - self.register[1]
            self.text_value.set( difference )

            # Reset Flags, pointers, memory, etc...
            self.flag['subtract'] = False
            self.pointer = 0
            # For chaining operations together
            self.register[0] = difference

        if self.flag['multiply']:
            product = self.register[0] * self.register[1]
            self.text_value.set( product )

            # Reset Flags, pointers, memory, etc...
            self.flag['multiply'] = False
            self.pointer = 0
            # For chaining operations together
            self.register[0] = product

        if self.flag['divide']:
            # Catch DivisionByZero Exception
            # Dividing by zero results in 'ERROR' printing to the "LCD"
            try:
                quotient = self.register[0] / self.register[1]
            except ZeroDivisionError:
                quotient = 'ERROR'

            self.text_value.set( quotient )

            # Reset Flags, pointers, memory, etc...
            self.flag['divide'] = False
            self.pointer = 0
            # For chaining operations together
            self.register[0] = quotient




# Creates and runs the calculator application.
startCalculator = Calculator()