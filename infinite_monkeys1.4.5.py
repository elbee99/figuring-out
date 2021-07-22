# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:50:06 2021

@author: Larry
"""
import random
import time

# Generate n length string
def generate(n,goal_string="",indices=[]):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    string = ""
    for i in range(n):
        # Get a random letter from 27 length letters
        if i not in indices:
            string = string+letters[random.randrange(27)]
           
        else:
            string = string + goal_string[i]

    return string

# Score by comparing 
def score(string, goal_string):
    score = 0
    indices = []
    for i in range(28):
        if string[i] == goal_string[i]:
            score+=1
            indices.append(i)
    return score,indices
    
# Repeatedly call generate and score
def call():
    goal_string = 'methinks it is like a weasel'
    new_string = generate(28)
    new_score,indices = score(new_string, goal_string)
    best_score = 0
    best_string = ""
    best_indices = []
    loop_count = 0
    while new_score != 28:        
            if new_score > best_score:
                best_score = new_score
                best_string = new_string
                best_indices=indices
            new_string = generate(28,goal_string,best_indices)
            new_score,indices = score(new_string, goal_string)
            loop_count += 1
            
            if loop_count % 1000 == 0:
                print(best_string, best_score, loop_count)
    # When the loop_while break
    print("You have typed '%s' in %d iterations" % (new_string, loop_count))
    return 


    
    
if __name__ == "__main__":
    call()

