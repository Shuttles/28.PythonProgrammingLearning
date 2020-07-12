

# 1.一些内置方法

## 1.1len()

1. 获取字符串长度(有时是==字节数==， 有时是字符数(比如汉字))



## 1.2截取字符串

### 1.2.1切片

```python
string = '你的名字'

string[2:3]
#输出是'名'
```



### 1.2.2split

```python
string.split(sep="None", maxsplit(默认不限次数))
#sep默认空格、换行等
#返回结果是列表，但不会更改原字符串内容
```



## 1.3合并字符串

将list合并成一个string

```python
strnew = 'sep'.join(iterable)

string = string.split(" ")
string = '@'.join(string)

#结果是'你@的@名@字'
```





## 1.4检索字符串

### 1.4.1cout

```python
str.count(sub[start, end]) #start，end代表母串检索范围

#例子
string = "hello world"
sub = "l"
string.count(sub)
```



### 1.4.2find

```python
str.find(sub[start, end])

#例子
string = "hello world"
sub = 'orl'
string.find(sub)
#返回第一次出现sub的index，没有则返回-1
#返回7
```



注意`index()方法`和find一致，但是找不到会抛出异常



## 1.5去除多余字符

### 1.5.1strip()

去掉字符串两端的特殊字符

```python
str.strip([chars]) #默认是空格

#例子
string = "  hello world "
string.strip(" @ #")
```



## 1.6格式化字符串

```python
 %[- + 0] expression
 -:左对齐
 +:右对齐
 0:左对齐，不够的补0
    
    
 #例子
template = '编号 ：%09d\t公司名称 : %s\t官网：www.%s.com'
contex1 = (7, '海贼科技', 'haizeix')

print(template % contex1)
```

```python
str.format()
```



## 1.7字符串编码转换

### 1.7.1encode

```python
str.encode(encoding = "utf-8", errors = 'strict', replace = '?')
#strict代表抛出异常，ignore代表忽略，
```



### 1.7.2decode

```python
二进制文本信息.decode(参数同uncode)
```



## 1.5其他

### 1.5.1startswith()

### 1.5.2endswith()



### 1.5.3lower()

大写转小写



### 1.5.4upper()

小写转大写