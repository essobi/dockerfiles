FROM centos:7  
ARG NH_VER=3.6.0  
ARG JNH_VER=3.6.0-0.9  
RUN \  
yum install -y byacc curl flex gcc glibc-headers groff-base make ncurses-devel
patch tar && \  
yum reinstall -y glibc glibc-common && \  
localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \  
curl -sL
http://www.nethack.org/download/${NH_VER}/nethack-${NH_VER//.}-src.tgz | tar
zxf - && \  
cd nethack-${NH_VER} && \  
curl -sL https://ja.osdn.net/dl/jnethack/jnethack-${JNH_VER}.diff.gz | zcat |
iconv -f cp932 -t euc-jp-ms | patch -p1 && \  
sed -i -e 's/cp -n/cp/g' -e '/^PREFIX/s:=.*:=/usr:' sys/unix/hints/linux && \  
sh sys/unix/setup.sh sys/unix/hints/linux && \  
make all && \  
make install && \  
cd .. && \  
rm -rf nethack-${NH_VER}  
  
ENV LANG ja_JP.UTF-8  
ENV NETHACKOPTIONS kcode:u  
  
# for backup  
VOLUME /usr/games/lib/jnethackdir  
  
ENTRYPOINT ["/usr/games/jnethack"]  

