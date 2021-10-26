## Challenge 15

สำหรับข้อนี้เรามาดูที่โค้ดกันก่อนเลย

```python
#!/usr/bin/env python3
import random
import os

FLAG = 'REDACTED'
random.seed(os.urandom(2))

def generate_key(flag):
  key = []
  for i in range(len(flag)):
    key.append(bytes([random.randint(1, 255)]))
  return b''.join(key)

key = generate_key(FLAG)
print(key)

def encode_flag(key):
  out = []
  for f, k in zip(FLAG, key):
    o = ord(f) * k
    out.append("%06d" % o)
    # print('ord(f)=%d k=%d o=%d' % (ord(f), k, o))
  return ''.join(out)
en_flag = encode_flag(key)
print(en_flag)
```

มันมาอีกแล้วครับ การเข้ารหัสด้วยการสุ่มแถมครั้งนี้ key เป็นการสุ่มทั้งหมดเลยด้วย เรามาลองทดสอบกันเลยดีกว่า

```console
goose@kali:~$ python3 challenge.py
b'\xb4\xea\x9d\t\r\x04\r\xfc'
014760016146010676000585000871000336000897017136

goose@kali:~$ python3 challenge.py
b'\xbak\xeb\xa6\xaf\x81\x92+'
015252007383015980010790011725010836010074002924
```

แต่การ encode flag นั้นดูไม่ยากเลย เอาแค่ ASCII ของ flag มาคูณกับ key ที่เข้าคู่กัน แล้วแปลงเป็นเลข 6 หลัก แล้วเอามา join กัน ทำให้เรา reverse ง่ายแน่ๆ

```python
def decode_flag():
    flag = []
    split_en_flag = [en_flag[i:i+6] for i in range(0, len(en_flag), 6)]
    # แยก en_flag ออกเป้นชุดๆ ชุดละ 6 ตัว
    for i in range(len(split_en_flag)):
        o = int(split_en_flag[i])
        # แปลงกลับมาเป็นตัวเลข
        ordf = int(o / key[i])
        # หารด้วย key ที่ pair กัน เพื่อให้ได้ ASCII ออกมา
        flag.append(chr(ordf))

    return(''.join(flag))
```

ทดลองหา flag กันเลย

```python
key = b'K\xdfX\x03\x7f\xff>W\xb2\xce\xfd\xea\x1b\x0e.ofe\x15\x82\x06\xd3(\xe6\nj\xe9\xba\xaf/\x03\xa4\xe8\n\xe4\xec\x99!\x9c\x91\x83\xb8\xe9.|\xc5\xce\xe3\xf3\xab\x8c\xce\x92\x8a\x10\xce\xf8X\xc2&`\xe4\xf8\x89\xf5\xca\xd5\xdf\xe7\x04\x1d\xee\xd6p\xd6U\x855\xe3o\xa0k/U`*\xceM\x01*6\xcc+\x15\x80\xfb\x1f\xbfb\xc6n\xfa$L\xd9\x9a\xccW(<W/7\xcd\xd5g\x1c\xad\x9d`C\xd7\x8a/\xd0\xb7p\xe1&\x0f\x85@e\xc4:\xfd\x97\xcd\x9d\xd9C\x8a\x19\xfd\x97\xfdj\x8fMy\xb8B\xf6\x01q:6po\xca"\xb0\xbf\xd9\xf6_\xcdo\xd0\x83h\xa5\x86\xe5\x86\x18P4m\xc2\xb33|\x8dG\xcd\x10\xdd&A\x89\xcc\xc5"q&\xdb?\xec\n\x0b6y`(Iu\x154\x19\xaeN\xff\xe8\'\xa6G\x19'

en_flag = '007725024084008536000300013335024735007192009657020292011948017963027144002106001092003588009102009180007878001638010140000474014981003120017940000780008268015844012648013650003666000234013940023664000780017784018408012087003927012168011310010218014352020970003128009672015366016068019068018468013338010920016068011388014766001248016068019344006864017460002964007488017784019344011508022050015756016614017394018249000488002262018564016692008736016478006630010374004134017706008991012160008346003666006630007488002016016068006006000078003276004860015912003354001638009984020331002356014898007644015444008580026750002808005928016926012012013464006786003120004680006786003807003740015990016614008034002184008996012246007488005226016770008970003666016224014274008736018900003116001170010374004992007878021168004524019734011778015990011932014756005226010764001950020493010268019734008268011154006006006171014352005148019188000078007345003944004212008736008658016968003060013728014898016926019188010165015990008658016224010218009360011220010452017862010452001944005440004056008502015132013962005457009672010998005538015990001440017238002964005070010686017136014972002652008814002964017301007560018408000780000858004212010890010176003120005694009126001785002496001950013572006084019890024128003042012948005538001950'


def decode_flag():
  flag = []
  split_en_flag = [en_flag[i:i+6] for i in range(0, len(en_flag), 6)]
  for i in range(len(split_en_flag)):
    o = int(split_en_flag[i])
    ordf = int(o / key[i])
    flag.append(chr(ordf))

  return(''.join(flag))

print(decode_flag())
```

ผลลัพธ์ที่ได้

```bash
gladiator:GtNNNRZNNNOGNNNNDDNNNUfNNNOwNNNNZDNNNTLNNNNkNNNNZNNNNTZNNNOzNNNNMNNNNQLNNNN0NNNNZNNNNQLNNNNkNNNNBNNNNQDNNNN4NNNNANNNNTRNNNNlNNNNLDNNNQDNNNN3NNNNADNNNTZNNNNkNNNNZDNNNQDNNNNkNNNNZNNNNTLNNNOxNNNNZjNNNU0NNNNhNNNN
```

เอา graditor ออก ก็จะเหลือ

```bash
GtNNNRZNNNOGNNNNDDNNNUfNNNOwNNNNZDNNNTLNNNNkNNNNZNNNNTZNNNOzNNNNMNNNNQLNNNN0NNNNZNNNNQLNNNNkNNNNBNNNNQDNNNN4NNNNANNNNTRNNNNlNNNNLDNNNQDNNNN3NNNNADNNNTZNNNNkNNNNZDNNNQDNNNNkNNNNZNNNNTLNNNOxNNNNZjNNNU0NNNNhNNNN
```

จากนั้นเราเอาไป decrypt กันต่อ

ขั้นแรกเรา Decrypt ด้วย BASE64 แบบ ROT13 จะได้ออกมาเป็น

```bash
N...C...S...A...{...c...1...f...1...0...c...f...d...6...4...0...6...1...8...4...8...4...a...2...a...4...7...5...c...1...1...4...1...0...f...d...3...}.......
```

เราก็เอาจุดออก จะได้เป็น

```bash
NCSA{c1f10cfd640618484a2a475c11410fd3}.
```
