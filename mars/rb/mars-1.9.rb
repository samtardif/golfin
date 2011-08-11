c,L,M=%w(NESW m.rotate! y+=m[0]-m[2];x+=m[1]-m[3])
R=L+' -1'
$<.read.scan(/(.+) (.+) (.)(\n.+)/){x=eval$1
y=eval$2
m=[0]*4
m[c.index $3]=1
eval$4.split('')*';eval '
puts [x,y,c[m.index 1]]*' '}
