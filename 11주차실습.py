#문제1
t1=input('복사할 파일명을 입력하시오')
t2=input('복사될 파일명을 입력하시오')

f1=open(t1,'r')
f2=open(t2,'w')

lines=f1.readlines()

data= lines
f2.write(data)

f1.close
f2.close


#문제2
f=open('README.txt','r')
t1=0
t2=0

for line in f:
    line= line.replace('\n')
    words=line.split()
    t1=t1+1
    for word in words:
        t2=t2+1
        
print(' of lines ',t1)

print(' of words ',t2)

f.close
#문제3
class calc:
    def sum(self, a,b):
        result = a+b
        print(a,"+",b,'=',result)
    def sub(self, a,b):
        result = a-b
        print(a,"-",b,'=',result)
    def multi(self, a,b):
        result = a*b
        print(a,"*",b,'=',result)     
    def div(self, a,b):
        result = a/b
        print(a,"/",b,'=',result)
