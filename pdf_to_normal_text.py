# -*- coding: utf-8 -*-
"""pdf to normal text

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Es6hTMTsuynyXYWNiBjV_tfRnq5tCaqv
"""

pip install PyPDF2

import pandas as pd
import PyPDF2 as pdf

def read_text_file(enlishpoem):
  with open('enlishpoem.pdf','r') as f:
    text=f.read()
    return text

text=read_text_file('outputtext.txt')
print(text)

