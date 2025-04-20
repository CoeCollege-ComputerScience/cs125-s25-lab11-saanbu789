# all sophomore level cs majors, all freshmen not majoring in math or cs, all senior math and cs majors

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


def freshmen():
    f=set()
    
    infile=open('studentYear.txt','r')
    for line in infile:
        if line[0]==1:
            line=line.strip().replace(","," ")
            f.add(line[0:])
    infile.close()
    return f

def sophomores():
    s=set()
    
    infile=open('studentYear.txt','r')
    for line in infile:
        if line[0]==2:
            line=line.strip().replace(","," ")
            s.add(line[0:])
    infile.close()
    return s

def seniors():
    se=set()
    
    infile=open('studentYear.txt','r')
    for line in infile:
        
        if line[0]==4:
            print(line)
            line=line.strip().replace(","," ")
            se.add(line[0:])
    infile.close()
    return se

# m=mathmajors()
# c=csmajors()
# f=freshmen()
# s=sophomores()
se=seniors()

# print(m)
print(seniors())





# WHY IS THE STUDENT YEAR NOT WORKING 
# ITS BASICALLY THE SAME AS THE MAJOR ONES 
# SO WHY IS IT BEING A BIATCH

# print(s.intersection(c))
# print(f.difference(m).difference(c))
# print(se.intersection(m).intersection(c))