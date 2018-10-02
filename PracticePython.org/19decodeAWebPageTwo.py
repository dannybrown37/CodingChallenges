# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 19
# Written by Danny Brown on December 1, 2017
# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
"""
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
vf = requests.get(url)
soup = BeautifulSoup(vf.text, 'lxml')
a = len(soup.find_all('p'))
for i in range(0, a):
    print soup.find_all('p')[i].text
    print '\n'
