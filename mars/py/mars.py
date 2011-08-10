m='NESW'
v=raw_input
v()
def r(p,i):
  if i:x=i[0];p[[p[2]%2,2][x!='M']]+=[1,-1][x>'M']if x!='M'else p[2]%4<2 or-1
  return r(p,i[1:])if i else(p[1],p[0],m[p[2]%4])
try:
  while 1:x,y,z=v()[::2];print"%d %d %s"%r(map(int,[y,x,m.find(z)]),v())
except:1
