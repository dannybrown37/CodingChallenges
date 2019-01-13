# http://www.pythonchallenge.com/pc/def/ocr.html

with open("2 character list.txt") as f:
    chars = f.read()
    char_count = {}
    for char in chars:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1s

    print char_count

# a e i l q u t y = equality?
    
