a = (1,2,3,4,5)
c,d,e,f,g = a  # 拆包
print(c,d,e,f,g)

s = 'hello'
c,d,e,f,g = s
print(c,d,e,f,g)  # 对可迭代对象都适用

l = ("a",1,4,(2,3,5))
f,s,t,ft = l
print(f,s,t,ft)  # 元素个数一致

str = ("name","age","gender","heigth","weight")
name,age,gender,_,_ = str
print(name,age,gender)  #不需要元素用_占位
