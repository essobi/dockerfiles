FROM debian:wheezy  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2015-03-09  
ENV VIRTUOSO_VERSION 7.1.0  
RUN apt-get update && apt-get -y install \  
dpkg-dev build-essential autoconf \  
automake libtool flex bison gperf \  
gawk m4 make odbcinst libxml2-dev \  
libssl-dev libreadline-dev openssl net-tools wget && \  
\  
wget --no-check-certificate \  
https://github.com/openlink/virtuoso-
opensource/archive/v$VIRTUOSO_VERSION.tar.gz && \  
\  
tar zxvf v$VIRTUOSO_VERSION.tar.gz && \  
cd /virtuoso-opensource-$VIRTUOSO_VERSION && \  
\  
./autogen.sh && \  
./configure CFLAGS="-O2" --prefix=/usr/local --with-readline && \  
\  
make && \  
\  
make install && \  
\  
rm /v$VIRTUOSO_VERSION.tar.gz && \  
\  
rm -rf /virtuoso-opensource-$VIRTUOSO_VERSION && \  
\  
apt-get -y purge \  
dpkg-dev build-essential autoconf \  
automake libtool flex bison gperf \  
gawk m4 make libxml2-dev \  
libssl-dev libreadline-dev net-tools wget && \  
\  
apt-get clean autoclean && \  
\  
apt-get autoremove -y &&\  
\  
rm -rf /var/lib/{apt,dpkg,cache,log}/ &&\  
\  
mkdir /var/log/virtuoso-http  
EXPOSE 8890 1111  
CMD /usr/local/bin/virtuoso-t -f -c \  
/usr/local/var/lib/virtuoso/db/virtuoso.ini  

