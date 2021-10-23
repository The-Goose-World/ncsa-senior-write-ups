## Challenge 09

สำหรับข้อนี้เรามาดูที่โค้ดกันก่อนเลย


```python
#!/usr/bin/env python3

flag = b'REDACTED'

def enc(plaintext):
    out = b''
    for c in plaintext:
        h = (int(c & 0xF0) >> 4) - 2
        l = (int(c & 0x0F) + 1) << 4
        o = int(h) + int(l)
        out += bytes([o])
    return out

ciphertext = enc(flag)
print(ciphertext)

e_flag = b'\xf2BC"\xc5QaT1\x114!T1DD1Ta1d\x81Q4AD4t!\x81a\x11$1dA!\xe5'

```

ที่นี้เรามาทดสอบรันโปรแกรม ว่าจะได้ผลลัพธ์เป็นยังไง

```console
goose@kali:~$ python3 challenge.py
b'3bR"BSbR'
```

จะเห็นว่าการเข้ารหัสจะเป็นการเข้ารหัสจะตกไปตรงมาเลยนั่นคือ<br />
R -> 3<br />
E -> b<br />
D -> R<br />
A -> "<br />
C -> B<br />
T -> S<br />

ผมเลยคิดว่า งั้นเราก็ไม่ต้องมา reverse แล้ว<br />
ทำตารางแก้ไปเลยดีกว่า

อันนี้คือโค้ดที่เอาไว้สร้างตารางในการแปลงค่า เนื่องจากผมรู้ว่า flag มีแค่เลขกับอักษรเท่านั้น

```python
#!/usr/bin/env python3

wordlist = b'1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}'
dictionary ={}

def table_gen(plaintext):
    for c in plaintext:
        h = (int(c & 0xF0) >> 4) - 2
        l = (int(c & 0x0F) + 1) << 4
        o = (int(h) + int(l)) % 256
        dictionary[o] = chr(c)

table_gen(wordlist)   
print(dictionary)

```

เท่านี้ก็จะได้ตารางในการแปลงค่า flag แล้ว

```bash
{b'!': '1', b'1': '2', b'A': '3', b'Q': '4', b'a': '5', b'q': '6', b'\x81': '7', b'\x91': '8', b'\xa1': '9', b'\x11': '0', b'"': 'A', b'2': 'B', b'B': 'C', b'R': 'D', b'b': 'E', b'r': 'F', b'\x82': 'G', b'\x92': 'H', b'\xa2': 'I', b'\xb2': 'J', b'\xc2': 'K', b'\xd2': 'L', b'\xe2': 'M', b'\xf2': 'N', b'\x02': 'O', b'\x13': 'P', b'#': 'Q', b'3': 'R', b'C': 'S', b'S': 'T', b'c': 'U', b's': 'V', b'\x83': 'W', b'\x93': 'X', b'\xa3': 'Y', b'\xb3': 'Z', b'$': 'a', b'4': 'b', b'D': 'c', b'T': 'd', b'd': 'e', b't': 'f', b'\x84': 'g', b'\x94': 'h', b'\xa4': 'i', b'\xb4': 'j', b'\xc4': 'k', b'\xd4': 'l', b'\xe4': 'm', b'\xf4': 'n', b'\x04': 'o', b'\x15': 'p', b'%': 'q', b'5': 'r', b'E': 's', b'U': 't', b'e': 'u', b'u': 'v', b'\x85': 'w', b'\x95': 'x', b'\xa5': 'y', b'\xb5': 'z', b'\xc5': '{', b'\xe5': '}'}
```

ได้เวลาเอาตารางที่ได้ไปแปลงค่า flag

```python
e_flag = b'\xf2BC"\xc5QaT1\x114!T1DD1Ta1d\x81Q4AD4t!\x81a\x11$1dA!\xe5'

wordlist = b'1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}'
dictionary ={}

def table_gen(plaintext):
    for c in plaintext:
        h = (int(c & 0xF0) >> 4) - 2
        l = (int(c & 0x0F) + 1) << 4
        o = (int(h) + int(l)) % 256
        dictionary[o] = chr(c)

table_gen(wordlist)  

flag = ''

for f in e_flag:
    flag += dictionary[f]

print(flag)
```

```bash
NCSA{45d20b1d2cc2d52e74b3cbf1750a2e31}
```
