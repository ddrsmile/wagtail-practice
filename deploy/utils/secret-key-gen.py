#-*- coding: utf-8 -*-
import os
import random, string
PUNCTUATION = '`~!@#$%^&*()_-+={}[]|<>?/,.;:'

def gen_key():
    return "".join([random.SystemRandom() \
             .choice(string.digits + string.ascii_letters + PUNCTUATION) for i in range(50)])

def gen_file():
    with open('SECRET_KEY', 'w') as f:
        f.write(gen_key())


if __name__=='__main__':
    gen_file()

