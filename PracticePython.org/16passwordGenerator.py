# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 16
# Written by Danny Brown on November 26, 2017
# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a
main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords,
pick a word or two from a list.
"""
import random, sys

def passwordStrength():
    while True:
        try:
            print "\nHow complex do you need your password to be?"
            print "1: Weak • 2: Moderate • 3: Strong • 4: (Exit the program.)"
            pwstr = str(raw_input(""))
        except ValueError:
            print "That's not a valid value.\n", 
            continue
        if pwstr != "1" and pwstr != "2" and pwstr != "3" and pwstr != "4":
            print "That's not a valid value.\n", 
            continue
        if pwstr == "4":
            exit()
        else:
            return int(pwstr)

def passwordBuilder(strength):
    pwbuild = ""
    passWords = ['dinosaur', 'puppy', 'kisses', 'angel', 'demon', 'scimitar',
                 'sword', 'magic', 'airplane', 'boat', 'car', 'face', 'camel',
                 'elephant', 'donkey', 'horse', 'tapir', 'noble', 'steed',
                 'baby', 'cute', 'laughter', 'monkey', 'elf', 'skill', 'angle',
                 'square', 'rectangle', 'triangle', 'circle', 'fork', 'spatula',
                 'pentagon', 'lion', 'hyena', 'tiger', 'bear', 'redhead',
                 'blonde', 'brunette', 'kangaroo', 'piglet', 'fox', 'bunny',
                 'rabbit', 'grotto', 'old', 'young', 'love', 'bagel', 'plate',
                 'chicken', 'viola', 'spicy', 'butter', 'oil', 'leaf', 'plant',
                 'noodle', 'soup', 'rainbow', 'gay', 'bland', 'flavorful',
                 'sweet', 'trumpet', 'guitar', 'bugle', 'cello', 'violin',
                 'trombone', 'cry', 'lennon', 'mccartney', 'harrison', 'tongs',
                 'star', 'piano', 'ukulele', 'boxer', 'fighter', 'trade',
                 'carry', 'reminder', 'blimp', 'blame', 'military', 'tank',
                 'bomb', 'every', 'fake', 'nonfiction', 'book', 'spa', 'web',
                 'shed', 'glove', 'laid', 'down', 'cut', 'cried', 'anger',
                 'shame', 'leaving', 'remains', 'southern', 'red', 'fiction',
                 'news', 'changes', 'still', 'same', 'bus', 'truck', 'bangle',
                 'tangle', 'south', 'leaves', 'crumble', 'wind', 'air', 'fire',
                 'water', 'park', 'central', 'northern', 'western', 'eastern',
                 'pulpchef', 'poor', 'rich', 'token', 'black', 'white', 'brown',
                 'yellow', 'random', 'computer', 'memory', 'manifesto', 'box',
                 'blue', 'purple', 'pink', 'bat', 'ball', 'net', 'hoop', 'hole',
                 'goal', 'microphone', 'soda', 'pop', 'soft', 'hard', 'hops',
                 'mild', 'barley', 'gangster', 'rap', 'sharp', 'sour', 'bitter',
                 'crazy', 'spoon', 'banner', 'ska', 'shingle', 'beam', 'wall',
                 'panda', 'grizzly', 'polar', 'hog', 'blanket', 'table']
    if strength == 1:
        times = random.randint(2,4)
        for x in range(times):
            pwbuild += passWords[random.randint(0,len(passWords))-1]
        return pwbuild
    if strength == 2:
        times = random.randint(2,3)
        addon = ""
        for x in range(times):
            pwbuild += passWords[random.randint(0,len(passWords))-1]
        addon = passwordAddons()
        pwbuild += addon
        return pwbuild
    if strength == 3:
        pwbuild = passwordGenerator(random.randint(11,30))
        return pwbuild

def passwordAddons():
    newAddon = ""
    for x in range(random.randint(1,2)):
        char = random.randint(48,57)
        newAddon += unichr(char)
    for x in range(random.randint(1,2)):
        char = random.randint(33,38)
        newAddon += unichr(char)
    return newAddon
                        
def passwordGenerator(length):
    newpw = ""
    for x in range(length):
        char = random.randint(33,122)
        newpw += unichr(char)
    return newpw        

# Main
keepGoing = True
while keepGoing == True:
    strength = passwordStrength()
    password = passwordBuilder(strength)
    print password
