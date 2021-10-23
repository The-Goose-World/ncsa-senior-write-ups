## challenge-01

มานั่งไล่ๆดู มามี password อะไรบ้างและ hash ด้วยอะไร
จะได้

|             Password             |       Type       |
| :------------------------------: | :--------------: |
|        021F0B4E4B0A00325F        | CISCO Password 7 |
|         022827682A2D2A18         | CISCO Password 7 |
| 84d961568a65073a3bcf0eb216b2a576 |       MD5        |
|  30820248 308201B1 A0030201 ...  |     PKI/RSA      |
|  $1$fMdg$.6qnjVSPs6Y6EIbBRrCYB.  |  CISCO Secret 5  |

ลองมาถอดดูกันเลย

|             Password             |       Type       | Plaintext |
| :------------------------------: | :--------------: | :-------: |
|        021F0B4E4B0A00325F        | CISCO Password 7 | you loss  |
|         022827682A2D2A18         | CISCO Password 7 |  NCSAKEY  |
| 84d961568a65073a3bcf0eb216b2a576 |       MD5        | superman  |
|  30820248 308201B1 A0030201 ...  |     PKI/RSA      | _Unknown_ |
|  $1$fMdg$.6qnjVSPs6Y6EIbBRrCYB.  |  CISCO Secret 5  | _Unknown_ |
