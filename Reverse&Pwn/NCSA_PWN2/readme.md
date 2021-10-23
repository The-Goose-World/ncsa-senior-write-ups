# NCSA_PWN2 [Privillage Escalation]

ทำการแสกน port ที่เปิดอยู่

```console
goose@kali:~$ nmap 159.138.237.28
```

![alt text](https://cdn.discordapp.com/attachments/698793956472913941/901505458379034684/unknown.png)

จากภาพจะเราจะเห็นว่ามีพอร์ตที่เปิดอยู่คือ 2021 ฉะนั้นเราจึงทำการ `ssh` 

```console
goose@kali:~$ ssh user@159.138.237.28 -p 2021
```

เข้าไปแล้วทำการสำรวจดูเราจะพบไฟล์ตามภาพ

![alt text](https://cdn.discordapp.com/attachments/698793956472913941/901505800676204564/unknown.png)

ซึ่งจะเห็นได้ว่ามี PwnSysNcsa ที่เป็น Executable อยู่ซึ่งเมื่อรันจะเห็นได้ว่าเราต้องหา passphase ใส่ไป

![alt text](https://cdn.discordapp.com/attachments/698793956472913941/901506621962866728/unknown.png)

ลองทำการ สำรวจเบื้องต้นด้วย `strings`

![alt text](https://cdn.discordapp.com/attachments/698793956472913941/901506277807652915/unknown.png)

เมื่อเรานำ `iamancsa` ไปใส่กับ `PwnSysNcsa` จะได้ตามรูป

![alt text](https://cdn.discordapp.com/attachments/698793956472913941/901507090940559520/unknown.png)

เห็นได้ว่ามีการ execute `sh` เกิดขึ้นฉะนั้นเราจึงทดลองเติมคำสั่งลงไป

![alt text](https://cdn.discordapp.com/attachments/698793956472913941/901507746107637830/unknown.png)

พบว่าเราสามารถรันคำสั่งได้รวมไปถึงได้สิทธิ์ `root`
ฉะนั้นเราก็สามารถดูไฟล์ `flag` ได้แล้ว

![alt text](https://cdn.discordapp.com/attachments/698793956472913941/901508685027762226/unknown.png)
