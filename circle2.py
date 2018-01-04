# PwxCircleSolver
import itertools
import math
from itertools import combinations
import csv
import pickle

# k = [10,11]
# for L in range(0, len(k)+1):
# 	for subset in itertools.combinations(k, L):
# 		print(subset)
print ("started")
total = 79
x = 13
y = 39
z = 27

add = x + y 
sub = x - y
div = x / y
tim = x * y
floordiv = x//y
modulo = x%y
exponent = x**y
sqrtx = math.sqrt(x) 
sqrty = math.sqrt(y) 
ceil = math.copysign(x,y)

powxy = math.pow(x,y)
powyx = math.pow(y,x)  


selfaddx = x+x
selfsubx = x -x 
selfdivx = x/x
selftimx = x*x
selffloordivx = x//x
selfmodulox = x%x
selfexponentx = x**x
factx = math.factorial(x)
truncx = math.trunc(x)
cosx = math.cos(x)
sinx = math.sin(x)
tanx = math.tan(x)

selfaddy = y + y
selfsuby = y - y
selfdivy = y / y
selftimy = y * y
selffloordivy = y//y
selfmoduloy = y%y
selfexponenty = y**y
facty = math.factorial(y)
truncy = math.trunc(y)
cosy = math.cos(y)
siny = math.sin(y)
tany = math.tan(y)


j = ['tany','tanx','sinx','siny','cosy','cosx','powxy','powyx','factx','facty','truncx', 'truncy' ,'add', 'sub', 'div', 'tim', 'floordiv', 'modulo', 'exponent', 'sqrtx', 'sqrty','selfaddx','selfsubx','selfdivx','selftimx','selffloordivx','selfmodulox','selfexponentx','selfaddy','selfsuby','selfdivy','selftimy','selffloordivy','selfmoduloy','selfexponenty']  

#make a list of all the combinations
mynum = []
for x in range(1, len(j)+1):
	mynum += combinations(j,x)
print (len(mynum))
# mynumpick = open('mynumpick.pickle', 'wb')
# pickle.dump(mynum, mynumpick)

# upmy = open('mynumpick.pickle', 'rb')
# upmy = pickle.load(upmy)

# # print mynum 
print ("about to start")
#filter
limit = 52
valid_combos = []
for i in upmy:
    operators = i
    result = sum([eval(v) for v in i])
    if result == limit:
        valid_combos.append({'operators': operators})


# # valid_combos = [xi for i in mynum if  sum([eval(v) for v in i]) == limit]
# #print valid_combos , "these are the valid combos"
print ("There is", len(valid_combos), "combinations")


# #lets get the serialization 
# # this is how i get the pickle out

circle2 = open('circle2.pickle', 'wb')
pickle.dump(valid_combos, circle2)
