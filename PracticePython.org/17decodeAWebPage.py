# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 17
# Written by Danny Brown on November 26, 2017
# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
"""
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.
"""

import urllib2, requests
from bs4 import BeautifulSoup

url = "http://www.newyorktimes.com"
nyt = requests.get(url)
nyt_html = nyt.text
soup = BeautifulSoup(nyt_html, "html.parser")

"""
headlines = soup.find("h2", {'class': 'story-heading'}).string
print headlines
"""

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
