m='NESW'
v=raw_input
v()
def r(p,i):
  if i:x=i[0]!='M';p[[p[2]%2,2][x]]+=x or p[2]%4<2 or-1
  return r(p,i[1:])if i else(p[1],p[0],m[p[2]%4])
try:
  while 1:x,y,z=v()[::2];print"%d %d %s"%r(map(int,[y,x,m.find(z)]),v())
except:1
