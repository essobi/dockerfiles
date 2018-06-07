FROM debian:latest  
MAINTAINER ywfwj2008 <ywfwj2008@163.com>  
  
ENV RUN_USER=www \  
LIBICONV_VERSION=1.14 \  
CURL_VERSION=7.54.1 \  
LIBMCRYPT_VERSION=2.5.8 \  
MHASH_VERSION=0.9.9.9 \  
MCRYPT_VERSION=2.6.8 \  
JEMALLOC_VERSION=5.0.1  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y ca-certificates wget gcc g++ make cmake autoconf patch
bzip2 psmisc pkg-config sendmail openssl libssl-dev curl libcurl4-openssl-dev
libxslt1-dev libicu-dev libxml2 libxml2-dev libjpeg-dev libpng-dev libpng16-16
libfreetype6 libfreetype6-dev libsasl2-dev libevent-dev vim && \  
rm -rf /var/lib/apt/lists/*  
RUN useradd -M -s /sbin/nologin ${RUN_USER} && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
WORKDIR /tmp  
  
# install libiconv  
ADD ./libiconv-glibc-2.16.patch /tmp/libiconv-glibc-2.16.patch  
RUN wget -c --no-check-certificate
http://ftp.gnu.org/pub/gnu/libiconv/libiconv-${LIBICONV_VERSION}.tar.gz && \  
tar xzf libiconv-${LIBICONV_VERSION}.tar.gz && \  
patch -d libiconv-${LIBICONV_VERSION} -p0 < libiconv-glibc-2.16.patch && \  
cd libiconv-${LIBICONV_VERSION} && \  
./configure --prefix=/usr/local && \  
make && make install && \  
rm -rf /tmp/*  
  
# install curl  
RUN wget -c --no-check-certificate
https://curl.haxx.se/download/curl-${CURL_VERSION}.tar.gz && \  
tar xzf curl-${CURL_VERSION}.tar.gz && \  
cd curl-${CURL_VERSION} && \  
./configure --prefix=/usr/local && \  
make && make install && \  
rm -rf /tmp/*  
  
# install mhash  
RUN wget -c --no-check-certificate
http://downloads.sourceforge.net/project/mhash/mhash/${MHASH_VERSION}/mhash-${MHASH_VERSION}.tar.gz
&& \  
tar xzf mhash-${MHASH_VERSION}.tar.gz && \  
cd mhash-${MHASH_VERSION} && \  
./configure && \  
make && make install && \  
rm -rf /tmp/*  
  
# install libmcrypt  
RUN wget -c --no-check-certificate
http://downloads.sourceforge.net/project/mcrypt/Libmcrypt/${LIBMCRYPT_VERSION}/libmcrypt-${LIBMCRYPT_VERSION}.tar.gz
&& \  
tar xzf libmcrypt-${LIBMCRYPT_VERSION}.tar.gz && \  
cd libmcrypt-${LIBMCRYPT_VERSION} && \  
./configure && \  
make && make install && \  
ldconfig && \  
cd libltdl && \  
./configure --enable-ltdl-install && \  
make && make install && \  
rm -rf /tmp/*  
  
# install mcrypt  
RUN wget -c --no-check-certificate
http://downloads.sourceforge.net/project/mcrypt/MCrypt/${MCRYPT_VERSION}/mcrypt-${MCRYPT_VERSION}.tar.gz
&& \  
tar xzf mcrypt-${MCRYPT_VERSION}.tar.gz && \  
cd mcrypt-${MCRYPT_VERSION} && \  
ldconfig && \  
./configure && \  
make && make install && \  
rm -rf /tmp/*  
  
# install jemalloc  
# 查看jemalloc状态 lsof -n | grep jemalloc  
RUN wget -c --no-check-certificate
https://github.com/jemalloc/jemalloc/releases/download/${JEMALLOC_VERSION}/jemalloc-${JEMALLOC_VERSION}.tar.bz2
&& \  
tar xjf jemalloc-${JEMALLOC_VERSION}.tar.bz2 && \  
cd jemalloc-${JEMALLOC_VERSION} && \  
./configure && \  
make && make install && \  
echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf && \  
ldconfig && \  
rm -rf /tmp/*  

