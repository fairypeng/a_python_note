#!/bin/bash
num=3
echo '$num'
echo "$num"
# 双引号
your_name="jack"
introduce1="my name is"," $your_name"
introduce2="my name is ${your_name}"
echo $introduce1 $introduce2
# 单引号
introduce3='my name is ,'$your_name' !'
introduce4='my name is ${your_name}'
echo $introduce3 $introduce4

# 获取字符串长度
string="abcdefghijk"
echo ${#string}
#获取子字符串
echo ${string:0:5}
# 查找子字符串
echo `expr index "$string" b`

# 定义数组
my_array=(1 2 3 4 5 6 7 8 9 0)
my_array1=(11
22
33
44
55
)
my_array2[0]="a"
my_array2[1]="b"
my_array2[2]="c"
my_array2[3]="d"
my_array2[4]="e"
my_array2[5]="f"
# 获取所有的元素
echo ${my_array[@]}
echo ${my_array1[@]}
echo ${my_array2[@]}
# 读取数组的某个元素
echo ${my_array[1]}
echo ${my_array1[2]}
echo ${my_array2[3]}
# 获取数组的长度
echo ${#my_array1[@]}
echo ${#my_ayyay1[*]}
# 获取数组中单个元素的长度
echo ${#my_array1[2]}





