#!/usr/bin/env python3

## Dillon Bartram Advanced Programming Seminar spring 2020

print ("Price Comparison\n")

price_one = float ( input ("Price of 64 oz size: "))
price_two = float ( input ("Price of 32 oz size: "))
print ("\n")

x = round (price_one / 64, 2)
y = round (price_two / 32, 2)

print ("Price per oz (64 oz) : " + str(x))
print ("Price per oz (32 oz) : " + str(y))


##This is correct as of 1/1##
