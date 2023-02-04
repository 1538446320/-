
def sum():
  
   from itertools import accumulate  #导包
   def fun(a,b):
      return a*b
       L=[1,2,3,4,5,6,7]
       sum = list(accumulate(L))  #返回L的前缀和序列 
       sum = list(accumulate(L,initial=0))  # 在L的前缀和序列前面添加一个初始元素,并且后继在此基础上累加
       sum = list(accumulate(L,fun))  # 自定义累加函数
       sum = list(accumulate(L,fun,initial=1))  # 自定义累加函数
