f=open("date.in")
g=open("date.out","w")
n=int(f.readline())     #starile sunt de la 0 la n-1
m=int(f.readline())
a=f.readline().split()  #alfabetul
d={}
for i in range(m):
    d[a[i]]=i
d['$']=m    #lambda
qz=int(f.readline())    #stare initiala
k=int(f.readline() )         #nr stari finale
qf=f.readline().split()  #stari finale
for i in range(k):
    qf[i]=int(qf[i])
t=int(f.readline())     #nr de tranzitii

M=[ [ [] for i in range(m+1) ] for j in range(n) ]
M[3][d['b']].append(4)
for i in range(t):
    xyz=f.readline().split()
    x=int(xyz[0])
    y=xyz[1]
    z=int(xyz[2])
    M[x][d[y]].append(z)

#Accepter
def stare_finala(q):
    global qf
    for i in range(len(qf)):
        if qf[i]==q:
            return True
    return False

def accepter(cuv,k,i,ok):   #ok este 0 daca am intrat cu o litera si 1 daca am intrat cu lambda
    global M,d,m,okfinal
    if ok==0:
        col=d[cuv[k]]
    else:
        col=m
    for j in range(len(M[i][col])):
        q_next=M[i][col][j]
        if k == len(cuv) - 2:
            if stare_finala(q_next):
                okfinal=0
                print("Acceptat")
            else:
                if len(M[q_next][m]) > 0 and okfinal:  # daca exista lambda
                    accepter(cuv, k, q_next, 1)
                else:
                    if okfinal:
                        okfinal=0
                        print("Neacceptat")
        else:
            if len(M[q_next][d[cuv[k+1]]])>0 and okfinal:   #daca exista drum de la starea in care intra litera k din cuv, catre o alta stare pt litera k+1
                accepter(cuv,k+1,q_next,0)
            if len(M[q_next][m])>0 and okfinal:   #daca exista lambda
                accepter(cuv,k,q_next,1)


#citesc cuvintele:
for i in range(5):
    cuv=f.readline()
    print(cuv[:len(cuv)-1])
    okfinal=1
    accepter(cuv,0,qz,0)
    if okfinal==1:
        print("Neacceptat")
    print('\n')
