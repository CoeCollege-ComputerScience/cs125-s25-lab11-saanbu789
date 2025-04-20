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
    return c
