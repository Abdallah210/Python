#coding:utf-8
'''
    Method                          	Description
__________________________________________________________________________________________________________________________________________________________________________________
1  - seed() 	        Initialize the random number generator
2  - getstate()        	Returns the current internal state of the random number generator
3  - setstate() 	    Restores the internal state of the random number generator
4  - getrandbits() 	    Returns a number representing the random bits
5  -   *randrange() 	    Returns a random number between the given range
6  -   *randint() 	    Returns a random number between the given range
7  -   *choice() 	        Returns a random element from the given sequence
8  -   *choices() 	    Returns a list with a random selection from the given sequence
9  -   *shuffle() 	    Takes a sequence and returns the sequence in a random order
10 -   *sample() 	        Returns a given sample of a sequence
11 -   *random() 	        Returns a random float number between 0 and 1
12 -   *uniform() 	    Returns a random float number between two given parameters
13 -   *triangular() 	    Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
14 - betavariate() 	    Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
15 - expovariate() 	    Returns a random float number based on the Exponential distribution (used in statistics)
16 - gammavariate()    	Returns a random float number based on the Gamma distribution (used in statistics)
17 - gauss() 	        Returns a random float number based on the Gaussian distribution (used in probability theories)
18 - lognormvariate() 	Returns a random float number based on a log-normal distribution (used in probability theories)
19 - normalvariate() 	Returns a random float number based on the normal distribution (used in probability theories)
20 - vonmisesvariate() 	Returns a random float number based on the von Mises distribution (used in directional statistics)
21 - paretovariate() 	Returns a random float number based on the Pareto distribution (used in probability theories)
22 - weibullvariate() 	Returns a random float number based on the Weibull distribution (used in statistics)

'''

import random 



#5 randrange() : 
"""
Syntaxe : random.randrange(a, b)

Returns a number between a (included) and b (not included)
"""

print("\n\n5 - randrange() :\nrandom.randrange(1, 11)")
print(random.randrange(3, 9))




#6 randint() : 
"""
Syntaxe : random.randint(a, b)

Returns a number between a and b (both included)
"""

print("\n\n6 - randint() :\nrandom.randint(5,10)")
print(random.randint(5, 10))




#7 choice() : 
"""
Syntaxe : random.choice(sequence)

Returns a randomly selected element from the specified sequence.
(The sequence can be a str, a range, a list, a tuple or any other kind of sequence.)
"""

print("\n\n7 - choice() :\nrandom.choice(oiseaux)")

oiseaux = ["aigle","coq","pigeon", "canard", "flamant"]
print(random.choice(oiseaux))




#8 choices() : 
"""
Syntaxe : random.choices(sequence, weights=None, cum_weights=None, k=1) 

*weights : poids (cette fonctionalité augmente la possibilité d'un élément par rapport aux autres)
*k : lenght of the returned list

"""

print("\n\n8 - choices :\nrandom.choices(jackpot,weights=[10,10,1], k=3)")

jackpot3 = ["lose","near","win"]
print(random.choices(jackpot3,weights=[100,100,1],k=3))




#9 shuffle() : 
"""
Syntaxe : random.shuffle(sequence,function)

Takes a sequence (list, string, or tuple) and reorganize the order of the items

*function : ??? (default : random.random() )

"""

print("\n\n9 - shuffle :\nrandom.shuffle(fruits)")

fruits = ["pomme","poire","banane","cerise"]
print(random.shuffle(fruits))




#10 random() : 
"""
Syntaxe : random.random()

Return random number between 0.0 and 1.0
"""

print("\n\n10 - random() :\nrandom.random()")
print(random.random())




#11 sample() : 
"""
Syntaxe : random.sample(sequence,k)

Returns a list with a randomly selection of a specified number of items from a sequnce.

*k : the size of the returned list  (important! : 0 < k <= len(list) )

"""
print("\n\n11 - sample() :\nrandom.sample(names,k=2)")

names = ["Abdellah"]
print(random.sample(names,k=2))




#12 uniform() : 
"""

Syntaxe : random.
"""
print("\n\n12 - uniform() :\nrandom.")
print(random.)




#13 triangular() : 
"""

Syntaxe : random.
"""
print("\n\n13 - triangular() :\nrandom.")
print(random.)

















