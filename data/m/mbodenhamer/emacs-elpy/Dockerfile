FROM mbodenhamer/emacs:onbuild  
MAINTAINER Matt Bodenhamer <mbodenhamer@mbodenhamer.com>  
  
# Custom user setup  
ONBUILD ARG uid=1000  
ONBUILD ARG gid=1000  
  
ONBUILD RUN sudo groupmod -g $gid user \  
&& sudo usermod -g $gid -u $uid user  

