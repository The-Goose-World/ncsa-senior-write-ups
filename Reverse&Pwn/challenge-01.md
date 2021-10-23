## Challenge 01

ทดลอง run มันกันก่อนเลย

```console
goose@kali:~$ chmod +x challenge

goose@kali:~$ ./challenge
password is gu3ssm3

You have 8 bytes!
no shell code

555 What are you gonna do now???

Please enter the password:
```

ลองกรอกอะไรมั่วๆดูก่อน

```console
goose@kali:~$ ./challenge
password is gu3ssm3

You have 8 bytes!
no shell code

555 What are you gonna do now???

Please enter the password: goose
Oh too bad!
Access Denied!
```

อยากรู้จังเลย ข้างในทำงานยังไง ลอง ltrace ดูดีกว่า

```console
goose@kali:~$ ltrace ./challenge
__libc_start_main(0x5655a567, 1, 0xfffe24b4, 0x5655a5f0 <unfinished ...>
printf("password is %s\n", "gu3ssm3"password is gu3ssm3
)                 = 20
puts("\nYou have 8 bytes!\nno shell code"...
You have 8 bytes!
no shell code

)         = 34
puts("555 What are you gonna do now???"...555 What are you gonna do now???
)           = 33
printf("\nPlease enter the password: "
)               = 28
__isoc99_scanf(0x5655b0d2, 0xfffe23ac, 0xfffe23e8, 0x5655a382Please enter the password:
```

ลองกรอกอะไรลงไป

```console
goose@kali:~$ ltrace ./challenge
__libc_start_main(0x5655a567, 1, 0xfffe24b4, 0x5655a5f0 <unfinished ...>
printf("password is %s\n", "gu3ssm3"password is gu3ssm3
)                 = 20
puts("\nYou have 8 bytes!\nno shell code"...
You have 8 bytes!
no shell code

)         = 34
puts("555 What are you gonna do now???"...555 What are you gonna do now???
)           = 33
printf("\nPlease enter the password: "
)               = 28
__isoc99_scanf(0x5655b0d2, 0xfffe23ac, 0xfffe23e8, 0x5655a382Please enter the password: goose
) = 1
strcmp("goose", "password")                           = -1
strcmp("goose", "p@ssword")                           = -1
strcmp("goose", "p@ssw0rd")                           = -1
strcmp("goose", "P@ssw0rd")                           = 1
strcmp("goose", "P@$$w0rd")                           = 1
strcmp("goose", "ll3hs0n")                            = -1
puts("Oh too bad!"Oh too bad!
)                                   = 12
puts("Access Denied!"Access Denied!
)                                = 15
+++ exited (status 0) +++
```

จากที่ดูแล้ว มีรหัสหนึ่งน่าสนใจมาก **ll3hs0n**

เราลองกรอกรหัสนี้กัน

```console
goose@kali:~$ ./challenge
password is gu3ssm3

You have 8 bytes!
no shell code

555 What are you gonna do now???

Please enter the password: ll3hs0n
Oh wow wow!
Access Granted: X05DU0F7ZjM5ODM2ZmQ1MmY1YzNhMThkYjhjZDY4MTNmNWYwMTZ9
```

มี text อะไรโผล่ออกมาด้วย **X05DU0F7ZjM5ODM2ZmQ1MmY1YzNhMThkYjhjZDY4MTNmNWYwMTZ9**
หน้าตาดูเหมือน base64 เลย

ลองเอาไป decode ดู

```console
goose@kali:~$ echo 'X05DU0F7ZjM5ODM2ZmQ1MmY1YzNhMThkYjhjZDY4MTNmNWYwMTZ9' | base64 --decode
_NCSA{f39836fd52f5c3a18db8cd6813f5f016}
```

ได้แล้ว flag ของเรา

```bash
NCSA{f39836fd52f5c3a18db8cd6813f5f016}
```
