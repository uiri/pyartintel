import os, random, copy

randstr = os.urandom(28)

def fitness(string):
    perfect = "METHINKS IT IS LIKE A WEASEL"
    fit = 0
    for i in xrange(28):
        if string[i] == perfect[i]:
            fit += 1
    return fit

def evolve(string):
    fit = fitness(string)
    for i in xrange(100):
        newstring = ""
        for j in xrange(28):
            if random.random() < 0.05:
                newstring += os.urandom(1)
            else:
                newstring += string[j]
        newfit = fitness(newstring)
        if newfit > fit:
            string = newstring
    return string

randfit = fitness(randstr)
gencount = 0
while randfit != 28:
    randstr = evolve(randstr)
    if fitness(randstr) > randfit:
        randfit = fitness(randstr)
        if randfit > 15:
            print randstr
    gencount += 1

print gencount
