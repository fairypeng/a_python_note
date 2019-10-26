# shell
### 基础说明
以`.sh`为后缀结尾的文件是shell文件

demo test.sh
```
#!/bin/bash
echo 'Hello World'
```
`#！/bin/bash`注释标记该文件的解释器路径
### 执行方式：
- 第一种：作为可执行程序
    ```
    chmod 755 test.sh  # 修改文件的执行权限 或者 chmod +x ./test.sh
    ./test.sh  # 执行文件，调用的解释器为文件头的解释器
    ```
- 第二种：作为解释器参数
    ```
    /bin/sh test.sh # 这种情况下，test.sh的头部文件没有效果
    ```
### 基本语法
##### 1.变量
###### 定义变量
- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。
- 中间不能有空格，可以使用下划线（_）。
- 不能使用标点符号。
- 不能使用bash里的关键字（可用help命令查看保留关键字）。

###### 使用变量
变量使用时需要在变量前面加上$符号

eg1：
```
your_name="python"
echo $your_name
echo ${your_name} #变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界

# 输出结果
python
python
```
eg2:
```
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done

# 输出结果
I am good at AdaScript
I am good at CoffeScript
I am good at JavaScript
```

###### 只读变量
使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变。
eg1:
```
#!/bin/bash
readonly myUrl="http://www.google.com"
myUrl="http://www.baidu.com"

# 运行结果
myUrl: readonly variable
```

###### 删除变量
`unset`变量被删除后不能再次使用。unset 命令不能删除只读变量。
```
#!/bin/sh
myUrl="http://www.google.com"
unset myUrl
echo $myUrl

# 输出结果
unset: myUrl: cannot unset: readonly variable
www.google.com
```

###### 变量类型
- 局部变量：局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
- 环境变量：所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
- shell变量：由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行


### shell字符串
- 单引号：单引号的任何字符都会原样输出，单引号字符串中的变量是无效的，不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。
- 双引号：双引号，可以有变量，可以出现转义字符

```
num=3
echo '$num'
echo "$num"
输出结果：
$num # 单引号
3 # 双引号
```

- 拼接字符串
```
name = "Jack"
# 双引号
introduce1="my name is" $name"!"
introduce2="my name is ${name} !"
# 单引号
introduce3='my name is' $name '!'
introduce4='my name is ${name}!'

echo introduce1
echo introduce2
echo introduce3
echo introduce4

# 输出结果：
my name is Jack!
my name is Jack!
my name is Jack!
my name is ${name}!
```
- 获取字符串长度
```
string="abcdefg"
echo ${#string}

# 输出结果
7
```
- 提取子字符串
```
string="abcdefg"
echo ${string:1:4} # 从索引为1的开始截取4个字符
# 输出结果
bcde
```
- 查找子字符串
```
string="abcdefg"
echo `expr index "$string" bi` # 从string中查找字符b或者i的位置，哪个字母先出现就计算哪个，没有找到的返回0
# 输出结果
2
```

### shell数组
支持一维数组，不支持多维数组，没有限定数组的大小，数组的下表由0开始编号。下标可以是整数或者算数表达式，其值应大于或等于0

- 定义数组`array_name=(value0 value1 value2 value3)`

用括号来表示数组，数组元素用"空格"符号分割开
```
# 第一种
my_array=(1 2 3 4 5 6 7 8 9 0)
# 第二种
my_array1=(11
22
33
44
55
)
# 第三种
my_array2[0]="a"
my_array2[1]="b"
my_array2[2]="c"
my_array2[3]="d"
my_array2[4]="e"
my_array2[5]="f"
```
- 读取数组`valuen=${array_name[n]}`
 使用`@`符号获取数组中的所有元素`echo ${array_name[@]}`
```
echo ${my_array[@]}
echo ${my_array[2]}
# 输出结果：
1 2 3 4 5 6 7 8 9 0
3
```
- 获取数组的长度`${#my_array[@]}`
```
# 获取数组的元素个数
echo ${#my_array1[@]}
echo ${#my_array1[*]}
# 获取数组单个元素的长度
echo ${#my_array1[2]}

# 输出结果：
5
0
2
```
