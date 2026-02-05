好，這堂課內容很多，我幫你**整理成「小學生也能看懂」的超白話筆記** ✨
我會分主題，用「在幹嘛＋重點一句話」的方式來講。

---

# 📘 今天上課重點筆記（超簡單版）

---

## 一、Streamlit 是什麼？

👉 **把 Python 變成網頁的工具**

你寫 Python，
Streamlit 幫你變成：

- 有圖片 🖼️
- 有按鈕 🔘
- 可以點、可以選的網站

---

## 二、顯示圖片（st.image）

```python
st.image("圖片路徑", width=1000)
```

意思是：

> 「在網頁上顯示一張圖片」

你今天學到三種顯示方式：

1️⃣ 指定寬度

```python
st.image("xxx.jpg", width=300)
```

2️⃣ 自動填滿畫面

```python
st.image("xxx.jpg", use_container_width=True)
```

3️⃣ 加標題（caption）

```python
st.image("xxx.jpg", caption="圖片名字")
```

---

## 三、用資料夾一次顯示很多圖片

```python
image_files = os.listdir("image")
```

意思是：

> 「把 image 資料夾裡所有檔名抓出來」

搭配 `for` 迴圈：

```python
for image_file in image_files:
    st.image("image/" + image_file)
```

👉 **不用一張一張寫，很省力！**

---

## 四、下拉選單（selectbox）

```python
selected_image = st.selectbox("請選圖片", image_files)
```

效果：

- 出現一個下拉選單
- 讓使用者選圖片

```python
st.image("image/" + selected_image)
```

👉 選哪張，就顯示哪張 👍

---

## 五、按鈕＋訊息提示

```python
st.button("按鈕")
```

搭配不同訊息：

- ✅ `st.success()` 成功
- ❌ `st.error()` 錯誤
- ⚠️ `st.warning()` 警告
- ℹ️ `st.info()` 資訊

```python
time.sleep(1)
st.rerun()
```

意思是：

> 等 1 秒 → 重新整理畫面

---

## 六、Session State（記憶力）

```python
ss = st.session_state
```

👉 這是 **Streamlit 的「記憶」**

不然：

- 一按按鈕
- 東西就全部忘光 😵

---

## 七、商品系統（Shop）

### 商品長這樣（字典）

```python
ss.products = {
  "商品名": {
      "image_path": "...",
      "price": 10,
      "stock": 10
  }
}
```

👉 一個商品有：

- 圖片
- 價格
- 庫存

---

### 顯示商品（for + columns）

```python
for name, details in ss.products.items():
```

意思是：

> 一個一個商品拿出來

```python
st.button(f"購買 {name}")
```

點了會：

- 庫存 -1
- 顯示成功或沒貨

---

## 八、補貨功能（Generate Product）

```python
ss.products[商品]["stock"] += 數量
```

👉 幫商品「加庫存」

---

## 九、Python 函式（Function）

### 1️⃣ 最簡單的函式

```python
def hello():
    print("Hello")
```

👉 呼叫一次，做一次

---

### 2️⃣ 有參數的函式

```python
def greet(name):
    print("Hello", name)
```

👉 可以丟東西進去用

---

### 3️⃣ 有回傳值的函式（return）

```python
def two_num_min(a, b):
    return a if a < b else b
```

👉 函式算完，**把答案交回來**

---

## 十、變數的地盤（超重要）

### 🏠 全域變數（global）

- 在函式外
- 大家都看得到

```python
length = 5
```

---

### 🏠 區域變數（local）

- 在函式裡
- 外面看不到

```python
def func():
    area = length * length
```

---

### ⚠️ 常見地雷

❌ 函式裡直接改全域變數
要嘛：

- 用 `return`
- 或寫 `global area`

---

## 十一、最安全寫法（老師最愛）

```python
def calculate():
    return length * length

area = calculate()
```

👉 **清楚、安全、不容易錯**

---

## 🌟 一句話總結

> 今天學的是
> **用 Streamlit 做網站 + 用 Python 管資料 + 函式怎麼用**

如果你要，我也可以幫你：

- 整理成「考前重點」
- 變成一張 A4 懶人包
- 或幫你出「老師可能考的題目」😄
