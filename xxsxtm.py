# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:57:12 2020

@author: ASUS
"""
import random
from fractions import Fraction
import profile
def timu(nianji,n):                                                  #生成题目
    shuzi=[random.randint(1,100)for i in range(n)]
    ti=""
    if(nianji<=3):                                                    #三年级以下只用做加减法
        fuhao=[random.choice(['+','-'])for i in range(n-1)]
    else:
        fuhao=[random.choice(['+','-','*','/'])for i in range(n-1)]
    for i in range(n-1):
        if(fuhao[i]=='/'):
            while(shuzi[i]>=shuzi[i+1]):
                shuzi[i]=random.randint(1,shuzi[i+1])
    for i in range(n-1):
        ti=ti+str(shuzi[i])+fuhao[i]
    ti=ti+str(shuzi[i+1])+" ="
    return shuzi,fuhao,ti
def jisuan(shuzi,fuhao,n):                                  #题目计算
    i=0
    while (i<n-1):
        if(fuhao[i]=='*' or fuhao[i]=='/'):
            j=i
            temp=shuzi[i]
            while(j<n-1 and (fuhao[j]=='*' or fuhao[i]=='/')):
                if(fuhao[j]=='*'):
                    temp=temp*shuzi[j+1]
                elif(fuhao[i]=='/'):
                    temp=temp/shuzi[j+1]
                j=j+1
            shuzi[i]=temp;
            i=j
        i=i+1
    daan=shuzi[0]
    for i in range(n-1):
        if(fuhao[i]=='+'):
            daan=daan+shuzi[i+1]
        elif(fuhao[i]=='-'):
            daan=daan-shuzi[i+1]
    return daan

def main():
    nianji=int(input("你所在的年级是：(n>=1 and n<=6)"))
    tishu=10                                                           #一共十道题
    fenshu=0
    for i in range(1,tishu+1):
        n=random.randint(2,10) 
        shuzi,fuhao,ti=timu(nianji,n)
        daan=jisuan(shuzi,fuhao,n)
        while(daan<0):
            shuzi,fuhao,ti=timu(nianji,n)
            daan=jisuan(shuzi,fuhao,n)
        print(ti,end='')
        jieguo=int(input(""))
        if(jieguo==Fraction('{}'.format(daan)).limit_denominator()):         #判断是否正确
            print("正确")
            fenshu=fenshu+10
        else:
            print("错误答案为：",end='')
            print(Fraction('{}'.format(daan)).limit_denominator())
    print("答题结束，总分为"+str(fenshu))                                              #给出总分
if __name__=="__main__":
    profile.run('main()')