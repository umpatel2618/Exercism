import string
import operator


mul = range(10,0,-1)
conversion = {d: int(d) for d in string.digits}
def is_valid(isbn):
    normlaized = isbn.replace('-',"")



