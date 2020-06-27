#單引號跟雙引號都可以
s = "Hello"
print(s)

#跳脫(跟外面符號做區隔)
s = "Hell\"o"
print(s)

#字串串接(用加號)
s = "Hello"+"World"
print(s)

#字串串接(用空白)
s = "Hello" "World"
print(s)

#字串換行(用\n)
s = "Hello\nWorld"
print(s)

#字串換行(用""")
s = """Hello

World"""
print(s)

#字串運算
s = "Hello"*3+"World"
print(s)

#字串會對內部字元編號(索引)，從0開始算起
#印出一個字母
s = "Hello"
print(s[0])

#表達開頭編號跟結束編號，包含開頭不包含結尾
s = "Hello"
print(s[1:4])

#忽略結尾，給開頭不給結尾，從開頭算起取道全部
s = "Hello"
print(s[1:])

#不給開頭只給結尾，不要這個結尾前免所有字
s = "Hello"
print(s[:4])