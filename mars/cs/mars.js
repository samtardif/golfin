(function() {
  var o, r;
  o = 'NESW';
  r = function(p, i) {
    var k;
    if (i.length) {
      k = i.shift();
      if (k === 'M') {
        if (p[2] % 4 < 2) {
          p[p[2] % 2] += 1;
        } else {
          p[p[2] % 2] -= 1;
        }
      } else if (k === 'R') {
        p[2]--;
      } else {
        p[2]++;
      }
      return r(p, i);
    }
      
    return [p[1], p[0], o.charAt(p[2] % 4)];
  };
  console.log(r([0, 0, 1], 'MRMLM'.split('')));
}).call(this);
