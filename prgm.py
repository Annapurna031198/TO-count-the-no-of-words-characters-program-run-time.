# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:50:39 2020

@author: Ajith Kumar
"""
import time
import re
start=time.time()
time.sleep(0)
file=open("sam.txt","r")
num_words=0

with open("sam.txt","r") as f:
    for line in f:
        words=line.split()
        num_words+=len(words)
print("no of words")
print(num_words)

file=open("sam.txt","r")
sam=file.read()
no_of_characters=len(sam)
print("no of characters(space)",no_of_characters)

sam=re.sub(r"\s+", "",sam,flags=re.UNICODE)
no_of_characters=len(sam)
print("no of character(no space)",len(sam))
end=time.time()
print(f"run time of the program is:{end-start}seconds")

        