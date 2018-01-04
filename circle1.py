# PwxCircleSolverimport itertools
import math
from itertools import combinations 
import pandas as pd  
import numpy as np 
import datetime
import sklearn as sk 
import pickle
# k = [10,11]
# for L in range(0, len(k)+1):
# 	for subset in itertools.combinations(k, L):
# 		print(subset)
print ("started")
total = 31
x = 10
y = 10
z = 11
kk = math.pi

add = x + y 
sub = x - y
div = x / y
tim = x * y
floordiv = x//y
modulo = x%y
exponent = x**y
sqrtx = math.sqrt(x) 
sqrty = math.sqrt(y) 



selfaddx = x+x
selfsubx = x-x 
selfdivx = x/x
selftimx = x*x

selfexponentx = x**x

selfaddy = y + y
selfsuby = y - y
selfdivy = y / y
selftimy = y * y

selfexponenty = y**y


add2 = y + x 
sub2 =  y - x
div2 =  y / x
tim2 = y * x
roun = kk
exponent2 = y**x

mean = add/2
j = ['roun','mean','add2', 'sub2', 'div2', 'tim2',  'exponent2','add', 'sub', 'div', 'tim', 'exponent', 'sqrtx', 'sqrty','selfaddx','selfsubx','selfdivx','selftimx','selfexponentx','selfaddy','selfsuby','selfdivy','selftimy','selfexponenty']  

print (mean)
for L in range(0, len(j)+1):
	for subset in combinations(j, L):
		break #print(subset) 


#make a list of all the combinations
mynum = []
for x in range(0, len(j)+1):
	mynum += combinations(j,x)


# print mynum 
print ("about to start")
#filter
limit = 11
valid_combos = []
for i in mynum:
    operators = i
    result = sum([eval(v) for v in i])
    if result == limit:
        valid_combos.append({'operators': operators})


# valid_combos = [i for i in mynum if  sum([eval(v) for v in i]) == limit]
#print valid_combos , "these are the valid combos"
print ("There is", len(valid_combos), "combinations")


#lets get the serialization 
# this is how i get the pickle out

circle1 = open('circle1.pickle', 'wb')
pickle.dump(valid_combos, circle1)

