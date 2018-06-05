FROM ubuntu:trusty  
  
MAINTAINER Luar Roji "cyberplant@roji.net"  
RUN echo 'deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty
main ' > /etc/apt/sources.list.d/gcc.list  
RUN apt-get update && apt-get -fy --force-yes install build-essential wget
libssl-dev \  
libncurses5-dev libnewt-dev libxml2-dev libjansson-dev \  
libsqlite3-dev uuid-dev file autoconf unzip g++-5  
  
RUN mkdir /usr/asterisk-src && cd /usr/asterisk-src/ && wget \  
http://downloads.asterisk.org/pub/telephony/dahdi-linux-complete/dahdi-linux-
complete-2.11.1+2.11.1.tar.gz \  
http://downloads.asterisk.org/pub/telephony/libpri/libpri-current.tar.gz \  
http://downloads.asterisk.org/pub/telephony/libss7/libss7-2.0-current.tar.gz \  
http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13-current.tar.gz
&& \  
for i in *tar.gz; do tar xvfz $i; rm $i; done  
  
RUN cd /usr/asterisk-src/libss7* && make && make install  
RUN cd /usr/asterisk-src/asterisk-13* && \  
echo yes | contrib/scripts/install_prereq install && \  
./configure --with-pjproject-bundled && \  
make menuselect.makeopts && \  
menuselect/menuselect --disable BUILD_NATIVE menuselect.makeopts && \  
sed -i "s/BUILD_NATIVE //" menuselect.makeopts && \  
menuselect/menuselect --list-options && \  
make NOISY_BUILD=yes && \  
make install && make config && make samples  
  
COPY entrypoint.sh /usr/bin  
  
# Cleanup  
RUN rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD start  

