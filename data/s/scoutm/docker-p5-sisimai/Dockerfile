FROM perl:5  
RUN mkdir -p /usr/src && cd /usr/src && git clone
https://github.com/sisimai/p5-Sisimai.git && cd ./p5-Sisimai && make install-
from-local  
  
CMD perl -MSisimai -lE 'binmode(STDOUT, ":utf8");print Sisimai->dump(shift);'
/data

