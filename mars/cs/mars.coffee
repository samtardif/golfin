o='NESW'
r=(p, i) ->
  if i.length
    k=i.shift();if k=='M'
      if p[2]%4<2then p[p[2]%2]+=1else p[p[2]%2]-=1
    else if k=='R'then p[2]--else p[2]++
    r(p, i)
  else[p[1],p[0],o.charAt(p[2]%4)]
    
console.log(r([0,0,1],'MRMLM'.split('')))
