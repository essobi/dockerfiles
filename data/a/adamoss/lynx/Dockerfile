FROM alpine  
  
RUN apk add zlib bison make gcc g++ openssl-dev ncurses-dev --no-cache && \  
wget https://invisible-mirror.net/archives/lynx/tarballs/lynx2.8.9dev.17.zip
&& \  
unzip lynx2.8.9dev.17.zip && \  
cd lynx2.8.9dev.17 && \  
export TERM=vt100 && \  
export GCC=g++ && \  
./configure --with-ssl=/usr/include --with-zlib=/usr/include --enable-
use_mouse && \  
make && \  
make install && \  
sed -i -e 's%#USE_MOUSE:FALSE%USE_MOUSE:TRUE%g' /usr/local/etc/lynx.cfg && \  
sed -i -e 's%#SET_COOKIES:TRUE%SET_COOKIES:FALSE%g' /usr/local/etc/lynx.cfg &&
\  
sed -i -e 's%#ACCEPT_ALL_COOKIES:FALSE%ACCEPT_ALL_COOKIES:FALSE%g'
/usr/local/etc/lynx.cfg  
  
ENTRYPOINT ["/usr/local/bin/lynx"]  

