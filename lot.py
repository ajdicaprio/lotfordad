import os

def minus10(x):
    if x >= 10:
        x = x - 10
    return x

def printList(x):
    print (x, end = "")
    return
    


#Step In:6 Out:5
# def st65(st):
#     out = []
#     out.append(st[0] + st[1])
#     out.append(st[1] + st[2])
#     out.append(st[2] + st[3])
#     out.append(st[3] + st[4])
#     out.append(st[4] + st[5])
#     out = list(map(minus10, out))
#     return out

#Step In:5 Out:4
def st54(st):
    out = []
    out.append(st[0] + st[1])
    out.append(st[1] + st[2])
    out.append(st[2] + st[3])
    out.append(st[3] + st[4])
    out = list(map(minus10, out))
    return out

#Step In:4 Out:3
def st43(st):
    out = []
    out.append(st[0] + st[1])
    out.append(st[1] + st[2])
    out.append(st[2] + st[3])
    out = list(map(minus10, out))
    return out

#Step In:3 Out:2
def st32(st):
    out = []
    out.append(st[0] + st[1])
    out.append(st[1] + st[2])
    out = list(map(minus10, out))
    return out


#START
while True:

    #Clear screen
    os.system('cls' if os.name=='nt' else 'clear')
        
    num = ""
    while len(num)<5 or len(num)>5:
        num = input ("Inserte Nro. (5 digitos): ")
        # num = "82502"
        try: int(num)
        except: num = ""

    numlist = []
    numlen = len(num)

    for i in range (numlen):
        numlist.append(int(num[i]))

    for j in range (90):
        if j < 9: cerodigit = "0"
        else: cerodigit = ""
        print (">> Ciclo " + cerodigit + str(j+1), end=": ")
        
        # Ciclo 1
        if j == 0: st5 = numlist
        st4 = st54(st5)
        st3 = st43(st4)
        st2 = st32(st3)
        list(map(printList, st5))
        print ("", end=" ")
        # print (st5)
        # print (st4)
        # print (st3)
        # print (st2)

        # Ciclo2
        st5 = []
        st5.append(numlist[0])
        st5.append(numlist[1])
        st5.append(numlist[3]) #segundo numero del triple base
        st5.append(st2[0])
        st5.append(st2[1])
        st4 = st54(st5)
        st3 = st43(st4)
        st2 = st32(st3)
        list(map(printList, st5))
        print ("", end=" " )
        # print (st5)
        # print (st4)
        # print (st3)
        # print (st2)

        # Ciclo3
        st5 = []
        st5.append(numlist[0])
        st5.append(numlist[1])
        st5.append(numlist[4]) #tercer numero del triple base
        st5.append(st2[0])
        st5.append(st2[1])
        st4 = st54(st5)
        st3 = st43(st4)
        st2 = st32(st3)
        list(map(printList, st5))
        print ("")
        # print (st5)
        # print (st4)
        # print (st3)
        # print (st2)

        # Ciclo4 para solo armar el nuevo st5
        st5 = []
        st5.append(numlist[0])
        st5.append(numlist[1])
        st5.append(numlist[2]) #primer numero del triple base
        st5.append(st2[0])
        st5.append(st2[1])

    print()
    input ("Presione una tecla para continuar...")
