# http://www.pythonchallenge.com/pc/def/equality.html

import re

with open("3 character list.txt") as f:
    chars = f.read()
    expression = "[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]"
    result = re.findall(expression, chars)
    print result

# ['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj',
#  'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']
# = linkedlist
