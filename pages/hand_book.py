import streamlit as st

st.title("Hand Book")

with st.expander("Class 1"):
    st.write(
        '''好呀～我幫你把今天的上課內容整理成 **「小學生也看得懂」的 Python 筆記** 📒✨
用很簡單的說法，重點清楚、不難記！)

-

## 🐍 Python 小學生筆記（今天上課重點）

### ✏️ 1. 註解（給人看的說明）

註解是「給人看，不會執行」的文字。

Python
# 這是單行註解
"""
這裡可以寫很多行註解
"""
'''
        """

👉 電腦會跳過，不會執行。



### 🔢 2. 常見的資料種類（資料型態）

| 類型  | 範例             | 說明   |
| - | |  |
| 整數  | 3           | 沒有小數 |
| 浮點數 | 3.14         | 有小數  |
| 布林值 | True / False | 對或錯  |
| 字串  | "hello"      | 文字   |

python
n1 = 3
n2 = 3.14
b1 = True
s1 = "hello"


-

### 🖨️ 3. print：把東西顯示出來

python
print(3)
print(True)
print("hello")
"""
        """

👉 'print' 就是「顯示給我們看」。

-

### ➕➖✖️➗ 4. 數學運算

python
a = 10
b = 20

print(a + b)   # 加法
print(a - b)   # 減法
print(a * b)   # 乘法
print(a / b)   # 除法
print(a // b)  # 取整數
print(a % b)   # 餘數
print(a ** 2)  # 次方




### 🔤 5. 字串（文字）可以做的事

python
print("hello" + "world")      # 接起來
print("hello" + " " + "world")
print("hello" * 3)            # 重複

-

### 🧩 6. f-string（把變數放進句子）

python
name = "Python"
age = 31
print(f"My name is {name}, and I am {age} years old.")


👉 很方便做「會變的句子」。

-

### 📏 7. len：數一數有幾個字

python
print(len(""))       # 0
print(len("hi"))     # 2
print(len("hello"))  # 5


-

### 🔍 8. type：看看是什麼資料

python
print(type(10))
print(type(3.14))
print(type(True))
print(type("hello"))

-

### 🔄 9. 資料型態轉換

python
int("123")     # 123
float("3.14")  # 3.14
str(123)       # "123"


#### 布林值小技巧

python
bool(0)      # False
bool(1)      # True
bool("")     # False
bool("Hi")   # True


-

### ⌨️ 10. input：請使用者輸入

python
age = int(input("你的年齡："))
print(age ** 2)


👉 input 得到的是「文字」，要記得轉成 `int` 或 `float`。

-

### 🔵 11. 算圓形面積

python
radius = float(input("請輸入半徑："))
area = 3.14 * radius ** 2
print("圓形面積是：", area)


-

### ⚖️ 12. 比較運算（對或錯）

python
print(1 == 1)  # True
print(1 != 1)  # False
print(2 > 1)   # True
print(2 < 1)   # False


-

### 🧠 13. 邏輯運算

python
print(not True)        # False
print(True and False) # False
print(True or False)  # True


👉

* and：兩個都對才對
* or：有一個對就對
* not：相反

-

### 🔐 14. if 判斷（做選擇）

python
password = input("請輸入密碼：")

if password == "1234":
    print("登入成功")
else:
    print("密碼錯誤")


"""
    )
