## Challenge 12

สำหรับข้อนี้เรามาดูที่โค้ดกันก่อนเลย

```python
#!/usr/bin/env python3

flag = "REDACTED"

def super_encode(flag):
  old = 0
  out = []
  for f in flag:
    new = (ord(f) + old) % 256
    out.append(new)
    old = ord(f)

  return out

secret = super_encode(flag)
print(secret)

# secret = [71, 150, 111, 103, 150, 111, 110, 145, 150, 148, 188, 172, 149, 149, 98, 101, 101, 105, 109, 154, 200, 148, 104, 106, 106, 156, 155, 110, 109, 105, 152, 154, 151, 148, 105, 109, 106, 103, 149, 194, 197, 149, 147, 223, 157, 103, 150, 111, 103, 150]

```

ที่นี้เรามาทดสอบรันโปรแกรม ว่าจะได้ผลลัพธ์เป็นยังไง

```console
goose@kali:~$ python3 challenge.py
[82, 151, 137, 133, 132, 151, 153, 137]
```

หลักการของการ encode ข้อนี้คือมันจะนำรหัส ascii ของตัวก่อนหน้ามันมารวมกับตัวมันแล้ว mod ด้วย 256 จากนั้นก็เก็บไว้ในลิสต์

ฉะนั้นวิธีการถอดก็คือ **ทำย้อนกลับมัน**

```python
def super_decode(secret):
  old = 0
  # เราจะเริ่มที่ 0 เหมือนกับการ encode
  out = []
  for s in secret:
    f = s - old
    # การ encode เรานำ old ไปบวก ตอน decode ก็เอาไปลบออก
    out.append(chr(f))
    # แปลงกลับไปเป็น char
```

เอาไปลองใช้กันเลย

```python
def super_decode(secret):
  old = 0
  # เราจำเริ่มที่ 0 เหมือนกับการ encode
  out = []
  for s in secret:
    f = s - old
    # การ encode เรานำ old ไปบวก ตอน decode ก็เอาไปลบออก
    old = f
    # แทนค่า old อันใหม่
    out.append(chr(f))
    # แปลงกลับไปเป็น char
  return out

secret = [71, 150, 111, 103, 150, 111, 110, 145, 150, 148, 188, 172, 149, 149, 98, 101, 101, 105, 109, 154, 200, 148, 104, 106, 106, 156, 155, 110, 109, 105, 152, 154, 151, 148, 105, 109, 106, 103, 149, 194, 197, 149, 147, 223, 157, 103, 150, 111, 103, 150]

flag = super_decode(secret)
print(('').join(flag))
```

เท่านี้ก็ได้ flag แล้ว

```bash
GO GO NCSA{1d114185ec1737e6854d6a36734aad1b} GO GO
```
