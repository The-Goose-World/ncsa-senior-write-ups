## Challenge 06

หลังจากที่ทนฟังแสบหูไปสักพัก ผมก็คิดว่ามันน่าจะเป็นรหัสมอส เลยลองเอาไป decode ดู

![alt text](https://i.ibb.co/m52p8pp/morse1.png)

ได้ข้อความออกมาว่า

```bash
57MEWTVHXVMSU6WETKGQ6WQOKTYWLTQIW7MMRANUQEWRMG5LIT8Y6DYME
```

ซึ่งมันดูไม่ได้ใกล้เคียงกับ flag เลย

ผมจึงนำเสียงไป reverse ใน audacity แล้วค่อยไป decode จึงได้ออกมาเป็น

```bash
EMQU4Q2TIF5WCMZRGEYDANRZMM3GIYTFGQZTKOJYG4YWKZTEG4ZDSMBXHBTGEM35
```

ซึ่งสิ่งนี้คือ Base32 เราเอาไป decode อีกรอบได้เป็น

```
#!NCSA{a3110069c6dbe4359871efd729078fb3}
```
