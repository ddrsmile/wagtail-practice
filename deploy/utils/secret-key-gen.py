#-*- coding: utf-8 -*-

import os

def gen_key():
    import random, string
    return "".join([random.SystemRandom() \
             .choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)])

def gen_file():
    with open('SECRET_KEY', 'w') as f:
        f.write(gen_key())


if __name__=='__main__':
    gen_file()

