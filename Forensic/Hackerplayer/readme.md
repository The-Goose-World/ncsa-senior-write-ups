## hackerplayer

ทำการแสกน port ที่เปิดอยู่

```console
goose@kali:~$ strings hackerwow.mp4
typisom
isomiso2avc1mp41
free
`mdat
x264 - core 160 r3011 cde9a93 - H.264/MPEG-4 AVC codec - Copyleft 2003-2020 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=11 lookahead_threads=1 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
)/'t;
v]D$B
wII!
"-IU
F#P4
oQFiG
>-m/
.
.
.
ISO Media file produced by Google Inc. Created on: 02/12/2019.
ISO Media file produced by Google Inc. Created on: 02/12/2019.
CaV494mhq2UskP628yS9kVT8E8qdMLtXL6jcvvTdCLUHdGZgm1Zn
Lavf58.45.100
```

จะเห็นอะไรมากมายเลยครับ แต่มีที่เตะตาอยู่อันหนึ่ง

```bash
CaV494mhq2UskP628yS9kVT8E8qdMLtXL6jcvvTdCLUHdGZgm1Zn
```

เจ้าสิ่งนี้คือ base58 เมื่อเรา decode ก็จะได้

```bash
NCSA{e64016ff53f69578c05ef94aa2f866ba}
```
