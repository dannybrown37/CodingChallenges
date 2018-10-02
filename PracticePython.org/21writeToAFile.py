# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 21
# Written by Danny Brown on December 3, 2017
# http://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
"""
Take the code from the How To Decode A Website exercise (if you didn’t do it or
just want to play with some different code, use the code from the solution), and
instead of printing the results to a screen, write the results to a txt file. In
your code, just make up a name for the file you are saving to.
Extras: Ask the user to specify the name of the output file that will be saved.
"""
import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
vf = requests.get(url)
soup = BeautifulSoup(vf.text, 'lxml')
a = len(soup.find_all('p'))

fileName = str(raw_input("Please enter a name for the output file. "))
fileName = fileName + ".txt"
article = open(fileName, "w")
for item in range(0, a):
    article.write(soup.find_all('p')[item].text.encode('utf-8'))
    article.write('\n\n')
article.close()
