#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*2'20

length = input('password length?')
length = int(length)

for p in range(10):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
