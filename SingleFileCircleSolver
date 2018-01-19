'''
Many persons who are not conversant with mathematical studies,
imagine that because the business of the engine is to give its results 
in numerical notation, the nature of its processes must consequently be arithmetical 
and numerical, rather than algebraic and analytical. This is an error. 
The engine can arrange and combine its numerical quantities exactly as if they were letters
or any other general symbols; and in fact it might bring out its results in algebraic notation,
 were provisions made accordingly"   --Augusta Ada, Countess of Lovelace
'''

# PwxCircleSolver
import math
from itertools import combinations
import pickle

print ("started circle 1")

#these are the 2 known numbers in all cases.
x = 10
y = 10
# this is the hinted number that is trying to be solved in the third case.
z = 11

total = x + y + z


add = x + y 
sub = x - y
div = x / y
tim = x * y
selfaddx = x+x
selfsubx = x-x 
selfdivx = x/x
selftimx = x*x
selfaddy = y + y
selfsuby = y - y
selfdivy = y / y
selftimy = y * y
add2 = y + x 
sub2 =  y - x
div2 =  y / x
tim2 = y * x
mean = add/2


# roun = kk
# kk = math.pi
# selfexponentx = x**x
# sqrtx = math.sqrt(x) 
# sqrty = math.sqrt(y) 
# floordiv = x//y
# modulo = x%y
# exponent = x**y
# selfexponenty = y**y
# exponent2 = y**x
# j = ['roun','mean','add2', 'sub2', 'div2', 'tim2',  'exponent2','add', 'sub', 'div', 'tim', 'exponent', 'sqrtx', 'sqrty','selfaddx','selfsubx','selfdivx','selftimx','selfexponentx','selfaddy','selfsuby','selfdivy','selftimy','selfexponenty']  

j = ['mean','add2', 'sub2', 'div2', 'tim2',  
		'add', 'sub', 'div', 'tim', 'selfaddx','selfsubx','selfdivx','selftimx',
		'selfaddy','selfsuby','selfdivy','selftimy']  


# for L in range(0, len(j)+1):
# 	for subset in itertools.combinations(j, L):
# 		break #print(subset) 


#make a list of all the combinations
mynum = []
for x in range(0, len(j)+1):
	mynum += combinations(j,x)
print (len(mynum),'circle 1 has this many possible combinations')


mynumpick = open('myNumPickCirle2.pickle', 'wb')
pickle.dump(mynum, mynumpick)

upmy = open('myNumPickCirle2.pickle', 'rb')
upmy = pickle.load(upmy)



# print mynum 
print ("about to start creating the valid combos")

#filter
limit = 11
valid_combos = []
for i in mynum:
    operators = i
    result = sum([eval(v) for v in i])
    if result == limit:
        valid_combos.append({'operators': operators})

# gc for memory 
mynum = None

# valid_combos = [i for i in mynum if  sum([eval(v) for v in i]) == limit]
#print valid_combos , "these are the valid combos"
print ("There is", len(valid_combos), "combinations")


#lets get the serialization 
# this is how i get the pickle out
circle1 = open('circle1.pickle', 'wb')
pickle.dump(valid_combos, circle1)


#gc for memory
circle1 = None
mynumpick = None
upmy = None

########################################################################################################################################################################################

########################################################################################################################################################################################

########################################################################################################################################################################################
									#### 				CIRCLE 2 STARTS HERE					####
########################################################################################################################################################################################

########################################################################################################################################################################################

########################################################################################################################################################################################
print ("started Circle 2")
x = 13
y = 39
z = 27
total = x + y + z

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



selfaddx = x+x
selfsubx = x -x 
selfdivx = x/x
selftimx = x*x
selffloordivx = x//x
selfmodulox = x%x
selfexponentx = x**x
truncx = math.trunc(x)

selfaddy = y + y
selfsuby = y - y
selfdivy = y / y
selftimy = y * y





# factx = math.factorial(x)
# powxy = math.pow(x,y)
# powyx = math.pow(y,x)  
#removed for memory add for complex problems
# cosx =  math.cos(x)
# sinx =  math.sin(x)
# tanx =  math.tan(x)
# selffloordivy  = y//y
# selfmoduloy  = y%y
# selfexponenty  =  y**y
# facty =  math.factorial(y)
# truncy =  math.trunc(y)
# cosy =  math.cos(y)
# siny  = math.sin(y)
# tany =  math.tan(y)
# j = ['tany','tanx','sinx','siny','cosy','cosx','powxy','powyx','factx','facty','truncx', 'truncy' ,'add', 'sub', 'div', 'tim', 'floordiv', 'modulo', 'exponent', 'sqrtx', 'sqrty','selfaddx','selfsubx','selfdivx','selftimx','selffloordivx','selfmodulox','selfexponentx','selfaddy','selfsuby','selfdivy','selftimy','selffloordivy','selfmoduloy','selfexponenty']  

# Smaller resource usage version
j = ['truncx', 
		'add', 'sub', 'div', 'tim', 'floordiv', 'modulo', 'exponent',
		'sqrtx', 'sqrty','selfaddx','selfsubx','selfdivx','selftimx','selffloordivx',
		'selfmodulox','selfexponentx','selfaddy','selfsuby','selfdivy','selftimy']  

#make a list of all the combinations
mynum = []
for x in range(1, len(j)+1):
	mynum += combinations(j,x)
print (len(mynum), 'total combinations for circle2')
#send data to pickles to make the 
mynumpick = open('mynumpick.pickle', 'wb')
pickle.dump(mynum, mynumpick)

upmy = open('mynumpick.pickle', 'rb')
upmy = pickle.load(upmy)

#Free up ram
mynum = None
# gc.collect()

# # print mynum 
print ("about to start creating the valid combos")
#filter
limit = 27
valid_combos = []
for i in upmy:
    operators = i
    result = sum([eval(v) for v in i])
    if result == limit:
        valid_combos.append({'operators': operators})


# # valid_combos = [xi for i in mynum if  sum([eval(v) for v in i]) == limit]
# #print valid_combos , "these are the valid combos"
print ("There is", len(valid_combos), "possible combinations")


# #lets get the serialization 
# # this is how i get the pickle out
circle2 = open('circle2.pickle', 'wb')
pickle.dump(valid_combos, circle2)

print ('finding the pairs between circle1 and circle2')

c1 = open('circle1.pickle', 'rb')
cc1 = pickle.load(c1)

c2 = open('circle2.pickle', 'rb')
# c2 = pickle.load(c2)
try:
    cc2 = pickle.load(c2)
except EOFError:
    cc2 = list(c2)

cc1 = list(cc1)
cc2 = list(cc2)

for i in cc1:
	if i not in cc2:
		cc1.remove(i)
print (cc1)
