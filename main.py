import os,struct,zlib
W=H=1024
PAPER=(246,241,231);INK=(20,20,20);NAVY=(14,42,71);GREEN=(47,208,122)
GOLD=(242,194,0);CRIM=(179,39,30);AMBER=(199,125,10);SLATE=(74,90,106)
WHITE=(255,255,255)
CS="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,%+-$&|:"
FT=">AAOAAANAANAAN>A@@@A>NAAAAANO@@N@@OO@@N@@@>A@GAA?AAAOAAA>44444>72222B<ABDHDBA@@@@@@OAKEEAAAAIECAAA>AAAAA>NAAN@@@>AAAEB=NAANDBA?@@>11NO444444AAAAAA>AAAAA:4AAAEEE:AA:4:AAAA:4444O1248@O>ACEIA>4<4444>>A168@OO2421A>26:BO22O@N11A>68@NAA>O124888>AA>AA>>AA?12<000000000000<<0000<48IJ248;C044O440000O0004?D>5N4<BD8EB=44444440<<0<<0"
px=bytearray(W*H*3)
def fill(x,y,w,h,c):
 for j in range(y,y+h):
  o=(j*W+x)*3;px[o:o+w*3]=bytes(c)*w
def text(s,x,y,sc,c,al=0):
 w=len(s)*6*sc-sc
 if al: x-=w//2
 for ch in s:
  i=CS.find(ch)
  if i<0: i=CS.find(" ")
  for r in range(7):
   b=ord(FT[i*7+r])-48
   for k in range(5):
    if b>>(4-k)&1: fill(x+k*sc,y+r*sc,sc,sc,c)
  x+=6*sc
def wrap(s,sc,mw):
 ls=[];cur=""
 for wd in s.split():
  t=(cur+" "+wd).strip()
  if len(t)*6*sc-sc<=mw: cur=t
  else:
   if cur: ls.append(cur)
   cur=wd
 if cur: ls.append(cur)
 return ls
def para(s,cx,y,sc,mw,c,al=1):
 for ln in wrap(s,sc,mw):
  text(ln,cx,y,sc,c,al);y+=9*sc
fill(0,0,W,H,PAPER)
text("THE WORLD",W//2,14,10,INK,1)
text("TUESDAY 24 NOVEMBER 2026",W//2,90,3,INK,1)
fill(24,116,976,4,INK)
fill(24,128,976,340,NAVY)
text("THE COMEBACK",W//2,142,3,GOLD,1)
text("HUANG IS BACK",W//2,170,9,WHITE,1)
text("+31%",W//2,244,18,GREEN,1)
text("NVIDIA SOARS AS BOARD REINSTATES ITS CEO",W//2,380,3,WHITE,1)
para("SHARES JUMP 31% IN A DAY, ADDING A RECORD $952 BILLION IN VALUE. THE S&P 500 CLIMBS 4.7%.",W//2,410,2,940,WHITE)
def cell(x,y,a,big,bs,head,line):
 fill(x,y,476,8,a)
 text(big,x+16,y+24,bs,a)
 para(head,x+16,y+100,3,444,INK,0)
 para(line,x+16,y+164,2,444,INK,0)
cell(24,480,NAVY,"7 DRONES",8,"UKRAINE SINKS RUSSIAN WARSHIP IN LIBYA","THE CORVETTE MERKURY GOES DOWN AT BENGHAZI, A HELICOPTER ABOARD IS DESTROYED.")
cell(524,480,CRIM,"GAZA",8,"HAMAS SECURITY CHIEF KILLED","NAEEM ABU NAHEL, 50, DIES IN AN ISRAELI STRIKE IN GAZA CITY, ONE OF AT LEAST 7 KILLED ON TUESDAY.")
cell(24,728,AMBER,"26 DEAD",8,"CANDY FACTORY FIRE IN INDONESIA","DEATH TOLL CONFIRMED ON TUESDAY, DOZENS STILL MISSING AFTER THE BLAZE IN BANTEN.")
cell(524,728,SLATE,"40 WOUNDED",7,"ZAPORIZHZHIA HIT OVERNIGHT","2 KILLED IN AN OVERNIGHT RUSSIAN STRIKE ON HOMES, FOUR OF THE WOUNDED ARE CHILDREN.")
fill(0,964,W,60,INK)
text("MARKETS: S&P 500 +4.7% | NASDAQ +6.5% | NIKKEI +3.91% | BRENT $86.71",W//2,987,2,WHITE,1)
def chunk(t,d):
 c=t+d;return struct.pack(">I",len(d))+c+struct.pack(">I",zlib.crc32(c)&0xffffffff)
raw=b"".join(b"\x00"+bytes(px[i*W*3:(i+1)*W*3]) for i in range(H))
dat=b"\x89PNG\r\n\x1a\n"+chunk(b"IHDR",struct.pack(">IIBBBBB",W,H,8,2,0,0,0))+chunk(b"IDAT",zlib.compress(raw,9))+chunk(b"IEND",b"")
os.makedirs("/output",exist_ok=True)
open("/output/entry.png","wb").write(dat)
