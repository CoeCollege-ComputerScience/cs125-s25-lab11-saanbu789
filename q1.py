# all math-cs double majors, all majoring in math or cs, all strictly cs majors


def mathmajors():
    m=set()
    num=0
    infile=open('math.txt','r')
    for line in infile:
        num+=1
        if num==1:
            continue
        line=line.strip().replace(","," ")
        m.add(line)
    infile.close()
    return m


def csmajors():
    c=set()
    num=0
    infile=open('cs.txt','r')
    for line in infile:
        num+=1
        if num==1:
            continue
        line=line.strip().replace(","," ")
        c.add(line)
    infile.close()
    return c

# print(mathmajors())
# print(csmajors())
m=mathmajors()
c=csmajors()
print(m.intersection(c))
print(m.symmetric_difference(c))
print(c.difference(m))