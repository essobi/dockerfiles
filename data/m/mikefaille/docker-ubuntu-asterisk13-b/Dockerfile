FROM ubuntu:15.10  
WORKDIR /usr/src  
  
RUN apt update && apt install git-core subversion libjansson-dev sqlite
autoconf automake libtool libxml2-dev libncurses5-dev build-essential uuid-dev
libsqlite3-dev pkg-config wget -y  
  
RUN wget http://downloads.xiph.org/releases/opus/opus-1.1.1.tar.gz -O
/usr/src/opus-1.1.1.tar.gz && tar xvfp /usr/src/opus-1.1.1.tar.gz && cd
/usr/src/opus-1.1.1 && ./configure --enable-float-approx --enable-intrinsics
&& make && make install && cd .. && git clone
https://github.com/seanbright/asterisk-opus.git -b asterisk-13.3 --depth=1  
  
RUN git clone \--depth=1 -b 13.6.0 http://gerrit.asterisk.org/asterisk
asterisk-13 && cd asterisk-13 && patch -p1 < /usr/src/asterisk-
opus/asterisk.patch && ./bootstrap.sh && ./configure --prefix=$HOME/asterisk-
bin --sysconfdir=$HOME/asterisk-bin/etc --localstatedir=$HOME/asterisk-bin/var  
  
RUN cd /usr/src/asterisk-13 && make menuselect.makeopts &&
menuselect/menuselect --disable BUILD_NATIVE --enable EXTRA-SOUNDS-FR-GSM
--enable EXTRA-SOUNDS-EN-GSM --enable CORE-SOUNDS-FR-GSM menuselect.makeopts
&& make && make install && make config && make install-logrotate  

