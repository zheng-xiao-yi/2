# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:57:12 2020

@author: ASUS
"""
import random
from fractions import Fraction
import profile
def kuohao(fuhao,n):                                          #如果temp为1.则生成括号，反之，则不
    i=0
    f=[]
    while(i<len(fuhao)):
        if (i != 0 and (f[len(f)-1] != ')' and f[len(f)-1] != '(') and (fuhao[i] == '+' or fuhao[i] == '-')):
            temp = random.randint(0,1);
            if(temp == 1):
                f.append('(')
                f.append(fuhao[i])
                f.append(')')
                i=i+1
                continue
        f.append(fuhao[i])
        i = i+1
    return f
def lianjie(fuhao,shuzi,n):                                        #将数字和符号连成题目
    ti=""
    j=0
    for i in range(n-1):
        if(fuhao[i+j] == '('):
            ti=ti+fuhao[i+j]
            j = j+1
        ti=ti+str(shuzi[i])+fuhao[i+j]
        if(fuhao[i+j]==')'):
            j = j+1
            ti=ti+fuhao[i+j]
    ti=ti+str(shuzi[i+1])
    if(fuhao[len(fuhao)-1]==')'):
        ti = ti + ')'
    ti = ti + '='
    return ti
def timu(nianji,n):                                                  #生成题目,返回题目和答案
    if(nianji<=2):                                                   #2年级以下只用做10以内的加减法
        shuzi=[random.randint(1,10)for i in range(n)] 
        fuhao=[random.choice(['+','-'])for i in range(n-1)]
    elif(nianji<=4):
        shuzi=[random.randint(1,10)for i in range(n)]               #4,3年级需要会10以内的四则运算
        fuhao=[random.choice(['+','-','*','/'])for i in range(n-1)]
    else:
        shuzi=[random.randint(1,100)for i in range(n)]               #5,6年级的题目为100以内的四则运算
        fuhao=[random.choice(['+','-','*','/'])for i in range(n-1)]
    for i in range(n-1):
        if(fuhao[i]=='/'):                                           #分数全为真分数
            while(shuzi[i]>=shuzi[i+1]):
                shuzi[i]=random.randint(1,shuzi[i+1])
    if(nianji>2):
        fuhao = kuohao(fuhao,n)
    ti=lianjie(fuhao,shuzi,n)
    daan = jisuan(shuzi,fuhao,n)
    return daan,ti
def jisuan(shuzi,fuhao,n):                                            #题目计算的结果
    i=0
    k=0
    while (i<n-1):
        if(fuhao[i+k]=='('):
            if(fuhao[i+k+1]=='+'):
                shuzi[i] = shuzi[i]+shuzi[i+1]
            else:
                shuzi[i] = shuzi[i]-shuzi[i+1]
                if(shuzi[i]<=0):
                    return -1
            shuzi[i+1]=shuzi[i]
            k=k+2
        elif(fuhao[i+k]=='*' or fuhao[i+k]=='/'):
            j=i
            temp=shuzi[i]
            while(j<n-1 and (fuhao[j+k]=='*' or fuhao[j+k]=='/')):
                if((j+k+1)<len(fuhao) and fuhao[j+k+1]=='('):
                    if(fuhao[j+k+2]=='+'):
                        shuzi[j+1] = shuzi[j+2]+shuzi[j+1]
                    else:
                        shuzi[j+1] = shuzi[j+1]-shuzi[j+2]
                        if(shuzi[j+1]<=0):
                            return -1
                if(fuhao[j+k]=='*'):
                    temp=temp*shuzi[j+1]
                elif(fuhao[j+k]=='/'):
                    temp=temp/shuzi[j+1]
                j=j+1
                if((j+k)<len(fuhao) and fuhao[j+k]=='('):
                    k=k+2
                    j=j+1
            shuzi[i]=temp;
            i=j
        i=i+1
    k=0
    daan=shuzi[0]
    for i in range(n-1):
        if(fuhao[i+k]=='+'):
            daan=daan+shuzi[i+1]
        elif(fuhao[i+k]=='-'):
            daan=daan-shuzi[i+1]
        elif(fuhao[i+k]=='('):
            k=k+2
    return daan
def jieguozhuanhuan(jieguo):                                              #将输入的答案转化为数字
    temp = 0
    sum1 = 0
    sum2 = 0
    jieguo = jieguo +'/'
    for i in jieguo:
        if(i != '/'):
            temp = temp*10+int(i)
        elif(sum1==0):
            sum1=temp/10
            temp = 0
        else:
            sum2 = temp/10
            temp = 0
    if(sum2 != 0):
        sum = sum1/sum2
        if(gongyinshu==-1):
            return -1
    else:
        sum = sum1
    return Fraction('{}'.format(sum)).limit_denominator()
     
def gongyinshu(sum1,sum2):                                   #判断输入的数是否为约分后的数，如果还可以约分，则为错误
    if(sum1>sum2):
        a=sum1
        b=sum2
    else:
        a=sum2
        b=sum1
    while(a%b!=0):
        t=b
        b=a%b
        a=t
    if(b==1):
        return 1
    else:
        return -1
def main():
    nianji=int(input("你所在的年级是：(n>=1 and n<=6)"))
    tishu=10                                                                #一共十道题
    fenshu=0
    shurucishu=1
    while(shurucishu<=3 and nianji<1 or nianji>6):                                       #小学生是1~6年级
        nianji=int(input("您是小学生,请注意,如果输入错误年级次数大于三次你的成绩将为0，你所在的年级是：(n>=1 and n<=6)"))
        shurucishu = shurucishu+1
    for i in range(1,tishu+1):
        if(shurucishu>3):
            break
        if nianji>3:                                                        #三年级以下题目长度较短
            n=random.randint(3,10)
        else:
            n=random.randint(2,4)
        daan = -1
        while(daan<0):
            daan,ti=timu(nianji,n)
        jieguo=jieguozhuanhuan(input(ti+""))
        if(jieguo==Fraction('{}'.format(daan)).limit_denominator()):         #判断是否正确
            print("正确")
            fenshu=fenshu+10
        else:
            print("错误,答案为：",end='')
            print(Fraction('{}'.format(daan)).limit_denominator())
    print("答题结束，总分为"+str(fenshu))                                      #给出总分
if __name__=="__main__":
   profile.run('main()')