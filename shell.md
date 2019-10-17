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
