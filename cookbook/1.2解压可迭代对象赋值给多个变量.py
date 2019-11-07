def drop_first_last(grades):
    first,*middle,last = grades
    return sum(middle) / len(middle)


gra = (100,99,89,70,56)
print(drop_first_last(gra))

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(":")
print(uname,fields,homedir,sh)
uname,*_,homedir,sh = line.split(":")
print(uname,homedir,sh)

# 实现递归算法
def sumlist(items):
    header,*tail = items
    if tail:
        return header + sumlist(tail)
    else:
        return header


print(sum([1,10,7,4,5,9]))
