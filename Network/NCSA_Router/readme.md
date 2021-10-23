# NCSA_Router

มานั่งไล่ๆดู มามี password อะไรบ้างและ hash ด้วยอะไร
จะได้

|             Password             |       Type       |
| :------------------------------: | :--------------: |
|        021F0B4E4B0A00325F        | CISCO Password 7 |
|         022827682A2D2A18         | CISCO Password 7 |
| 84d961568a65073a3bcf0eb216b2a576 |       MD5        |
|  30820248 308201B1 A0030201 ...  |     PKI/RSA      |
|  $1$fMdg$.6qnjVSPs6Y6EIbBRrCYB.  |  CISCO Secret 5  |
| b41eab52c22a7b7518828bd30a512618fa2c72052660b7450fd0f22ac12bfe00172c14d951d87576 |       DES        |

ลองมาถอดดูกันเลย

|             Password             |          Type          | Plaintext |
| :------------------------------: | :--------------------: | :-------: |
|        021F0B4E4B0A00325F        |    CISCO Password 7    | you loss  |
|         022827682A2D2A18         |    CISCO Password 7    |  NCSAKEY  |
| 84d961568a65073a3bcf0eb216b2a576 |          MD5           | superman  |
|  30820248 308201B1 A0030201 ...  |        PKI/RSA         | _Unknown_ |
|  $1$fMdg$.6qnjVSPs6Y6EIbBRrCYB.  |     CISCO Secret 5     | _Unknown_ |
| b41eab52c22a7b7518828bd30a512618fa2c72052660b7450fd0f22ac12bfe00172c14d951d87576  | DES-ECB (key=superman) | N	C	S	A	{	f	3	3	9	5	c	d	5	4	c	f 8	5	7	d	d	f	8	f	2	0	5	6	7	6	8	f f 4	9	a	e	}

Credit: [UnkAtreus](https://github.com/UnkAtreus)
