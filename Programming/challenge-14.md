## Challenge 14

สำหรับข้อนี้เรามาดูที่โค้ดกันก่อนเลย

```python
#!/usr/bin/env python3
import os

KEY = 'REDACTED'
FLAG = 'REDACTED'

n = int.from_bytes(os.urandom(1), 'little')
print(n)


def encode_key(n):
  key = []
  print(KEY[0::2] + KEY[1::2])
  for k in KEY[0::2] + KEY[1::2]:
    o = ord(k) ^ n
    key.append(bytes([o]))
  return b''.join(key)

en_key = encode_key(n)
print(en_key)

# en_key = b'\xd7\xfb\xe1\xe7\xed\xf6\xf2\xee\xe2\xff\xfe\xf8\xf2\xfe\xed\xe1\xe5\xfa\xf4\xb6'

def encode_flag():
  key = (KEY * int(len(FLAG)/len(KEY) + 1))[:len(FLAG)]
  out = []
  for f, k in zip(FLAG, key):
    s = ord(f) ^ ord(k)
    out.append(bytes([s]))

  return b''.join(out)

en_flag = encode_flag()
print(en_flag)

# en_flag = b'2\x06\x1f\n\x05E\x11\x1b\x1fZ\x13\x13\x01^Y\x1b\x1c\x0c\x04D4\x1aL\x0e\x04\x00P\x0b\x16\x0f\x04ZE\x1a\x1c\x1f\x10C\x01R`\x1d\x04\nV\x16\x15\n\x08\x1f\x15ZE<:>4\x18P@!PZ]AUHY\x19JQ\x12WF\x1b\x08\x14U\t\x12$^\x0e^\x13PH\x0f\x19O\x1cV\x0c\x01Y\x0b\x1a\x11HX/\x1c'
```

ข้อนี้มีความซับซ้อนจของการเข้ารหัสมากขึ้น เพราะเข้ารหัสทั้ง key และ flag แถมการเจข้ารหัสยังมีการสุ่มด้วย

ทีนี้เรามาลอง run โค้ดดูกันสักรอบ

```console
goose@kali:~$ python3 challenge.py
163
RDCEEATD
b'\xf1\xe7\xe0\xe6\xe6\xe2\xf7\xe7'
b'\x00\x00\x00\x00\x00\x00\x00\x00'

goose@kali:~$ python3 challenge.py
33
RDCEEATD
b'sebdd`ue'
b'\x00\x00\x00\x00\x00\x00\x00\x00'
```

มันกลับมาอีกแล้ว กับการ run ทุกครั้งแล้วผลไม่เหมือนกัน ซึ่งผมคิดในใจไว้เลย ได้ bruteforce แน่ๆ

ผมจะแยกคิด 2 ส่วน คือ 1.ส่วน key และ 2.ส่วน flag
โดยเราจะทำการ bruteforce key จากการ reverse ฟังก์ชั่นก่อน

```python
def decode_key(ekey,n):
  skey = []
  # อันนี้คือ list ที่เอาไว้เก็บ key ที่ยังไม่สมบูรณ์ก่อน
  # เพราะจาก code จะเห็นได้ว่า key ถูกเอาไปปู้ยี้ปู้ยำ สลับไปมาก่อนเอามา encode
  for i in ekey:
    o = i ^ n
    skey.append(bytes([o]))
  key = []
  # อันนี้คือ list ที่เอาไว้เก็บ key ที่สมบูรณ์
  for i in range(len(skey)//2):
    # เพราะเราเห็นจากโค้ดด้านบนว่า เค้าจะเอา key ในตำแหน่งเลขคู่มาก่อน และ join กับ key ในตำแหน่งเลขคี่
    # ตัวอย่างง่ายๆ คือ 0123456 จะกลายเป็น '0246' + '135' = '0246135'
    key.append(skey[i])
    key.append(skey[i+len(skey)//2])
  return b''.join(key)
```

ทีนี้ก็ได้เวลา brute force หา key

```python
def decode_key(ekey,n):
  skey = []
  for i in ekey:
    o = i ^ n
    skey.append(bytes([o]))
  key = []
  for i in range(len(skey)//2):
    key.append(skey[i])
    key.append(skey[i+len(skey)//2])
  return b''.join(key)

en_key = b'\xd7\xfb\xe1\xe7\xed\xf6\xf2\xee\xe2\xff\xfe\xf8\xf2\xfe\xed\xe1\xe5\xfa\xf4\xb6'

for i in range(256):
  print(decode_key(en_key,i))
```

จากนั้นก็พยายามหาตัวที่หล่อที่สุด

```bash
...
b'Bknmtgrkxxctgp{owaj#'
b'Ahmnwdqh{{`wdsxltbi '
b'@ilovepizzaverymuch!'
b'Ofc`yj\x7ffuunyj}vbzlg.'
b'Ngbaxk~gttoxk|wc{mf/'
...
```

จะได้ว่า key คือ **@ilovepizzaverymuch!**

จากนั้นเราไปทำ decoder ของ flag กันต่อ

```python
def decode_flag(en_flag):
  flag = []
  for i in range(len(en_flag)):
    # เรารู้จากการดูโค้ดด้านบนว่า len ของ flag และ en_flag นั้นเท่ากัน
    ikey = i % len(KEY)
    # เราจะหาตำแหน่งของอักษรใน KEY ที่จะเอามา XOR ด้วย
    f = en_flag[i] ^ ord(KEY[ikey])
    # เรารู้จากโค้ดด้านบนว่า s = ord(f) ^ ord(k)
    # นั่นหมายถึง ord(f) = s ^ ord(k) ด้วย
    flag.append(chr(f))

  return ''.join(flag)
```

เอาไปใช้กันเลย

```python
KEY = '@ilovepizzaverymuch!'

def decode_flag(en_flag):
  flag = []
  for i in range(len(en_flag)):
    ikey = i % len(KEY)
    f = en_flag[i] ^ ord(KEY[ikey])
    flag.append(chr(f))

  return ''.join(flag)

en_flag = b'2\x06\x1f\n\x05E\x11\x1b\x1fZ\x13\x13\x01^Y\x1b\x1c\x0c\x04D4\x1aL\x0e\x04\x00P\x0b\x16\x0f\x04ZE\x1a\x1c\x1f\x10C\x01R`\x1d\x04\nV\x16\x15\n\x08\x1f\x15ZE<:>4\x18P@!PZ]AUHY\x19JQ\x12WF\x1b\x08\x14U\t\x12$^\x0e^\x13PH\x0f\x19O\x1cV\x0c\x01Y\x0b\x1a\x11HX/\x1c'

print(decode_flag(en_flag))
```

จากนั่นหาตัวที่หน้าตาหล่อที่สุดในพวก

```bash
roses are red, violets are blue, here is the secret, NCSA{8aa9627080c00d24bea6a3d7b1e58fc5} is for you
```

เท่านี้ก็ได้ flag แล้ว

```bash
NCSA{8aa9627080c00d24bea6a3d7b1e58fc5}
```
