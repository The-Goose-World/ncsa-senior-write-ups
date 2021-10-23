## Challenge 13

สำหรับข้อนี้เรามาดูที่โค้ดกันก่อนเลย

```python
#!/usr/bin/env python3
import os

flag = "REDACTED"

def super_encode(flag):
  old = sum(os.urandom(8))
  out = []
  for f in flag:
    new = (ord(f) - old) % 256
    out.append(new)
    old = ord(f)

  return out

secret = super_encode(flag)
print(secret)

# secret = [189, 20, 253, 187, 70, 6, 245, 6, 185, 73, 10, 173, 46, 245, 16, 238, 58, 184, 4, 252, 49, 207, 0, 5, 42, 213, 42, 5, 253, 0, 209, 1, 251, 52, 208, 4, 254, 3, 43, 212, 41, 211, 253, 3, 45, 0, 214, 255, 1, 70, 177, 242, 55, 14, 7, 0, 180, 36, 43, 255, 247]

```

จะเห็นว่าคลายข้อที่แล้ว แต่มีความแตกต่างกันที่ old และการสร้างลำดับ ที่นี้เรามาทดสอบรันโปรแกรม ว่าจะได้ผลลัพธ์เป็นยังไง

```console
goose@kali:~$ python3 challenge.py
[41, 151, 137, 133, 132, 151, 153, 137]
goose@kali:~$ python3 challenge.py
[147, 151, 137, 133, 132, 151, 153, 137]
```

จะเห็นว่าการ run ทั้งสองครั้งของเราได้ผลไม่เหมือนกัน แต่ก็ต่างกันเพียงตัวแรก ซึ่งนั่นเกิดจาก

```python
old = sum(os.urandom(8))
```

แต่ algorithm ในการ encode ก็ยังคล้ายๆเดิม ผมก็จะนำฟังก์ชั่นจากข้อที่แล้วมาปรับใช้ได้

และผมจะใช้วิธีการ bruteforce เพื่อหาตัวลำดับที่หน้าตาดูดีที่สุด

```python
def super_decode(secret, i):
  old = i
  # เราจะเริ่มที่ i
  out = []
  for s in secret[1:]:
    # ทำตั้งแต่ตัวที่ 2 เป็นต้นมา
    f = (s + old) %256
    # การ encode เรานำ old ไปบวก ตอน decode ก็เอาไปลบออก
    old = f
    # แทนที่ old
    out.append(chr(f))
    # แปลงกลับไปเป็น char
  return out
```

เอาไป brute force กัน

```python
def super_decode(secret, i):
  old = i
  # เราจะเริ่มที่ i
  out = []
  for s in secret[1:]:
    # ทำตั้งแต่ตัวที่ 2 เป็นต้นมา
    f = (s + old) %256
    # การ encode เรานำ old ไปบวก ตอน decode ก็เอาไปลบออก
    old = f
    # แทนที่ old
    out.append(chr(f))
    # แปลงกลับไปเป็น char
  return out

secret = [189, 20, 253, 187, 70, 6, 245, 6, 185, 73, 10, 173, 46, 245, 16, 238, 58, 184, 4, 252, 49, 207, 0, 5, 42, 213, 42, 5, 253, 0, 209, 1, 251, 52, 208, 4, 254, 3, 43, 212, 41, 211, 253, 3, 45, 0, 214, 255, 1, 70, 177, 242, 55, 14, 7, 0, 180, 36, 43, 255, 247]

for i in range(0,256):
    this_flag = super_decode(secret,i)
    print(('').join(this_flag))
```

จากนั่นหาตัวที่หน้าตาหล่อที่สุดในพวก

```bash
...
he flag is NCSA{373d338b7afcc450d4869d8a414aa767}. Well Done
if!gmbh!jt!ODTB|484e449c8bgdd561e597:e9b525bb878~/!Xfmm!Epof
jg"hnci"ku"PEUC}595f55:d9chee672f6:8;f:c636cc9890"Ygnn"Fqpg
...
```

เท่านี้ก็ได้ flag แล้ว

```bash
NCSA{373d338b7afcc450d4869d8a414aa767}
```
