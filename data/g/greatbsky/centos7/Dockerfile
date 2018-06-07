FROM centos  
MAINTAINER architect.bian  
LABEL name="centos7" license="MIT" build-date="20180119"  
  
ENV VERSION 7.4  
ENV OPENSSL_VERSION OpenSSL_1_1_0g  
ENV ZLIB_VERSION 1.2.11  
RUN yum update -y && yum install -y epel-release && yum install -y gcc gcc-c++
perl automake autoconf libtool make yum-plugin-priorities sudo && mv
/etc/localtime /etc/localtime.bak && ln -s /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && yum install -y wget net-tools && mkdir -p /data/softs &&
mkdir -p /data/env && mkdir -p /data/web && cd /data/softs && wget
"http://zlib.net/zlib-$ZLIB_VERSION.tar.gz" && tar -zxf
zlib-$ZLIB_VERSION.tar.gz && cd zlib-$ZLIB_VERSION && ./configure && make &&
make install && cd /data/softs && yum remove openssl -y && wget
"https://codeload.github.com/openssl/openssl/tar.gz/$OPENSSL_VERSION" && tar
-zxf $OPENSSL_VERSION && cd openssl-$OPENSSL_VERSION && ./config
--prefix=/usr/ --openssldir=/etc/ssl shared zlib && make && make install && rm
-rf /data/softs/*  
  
CMD ["/bin/bash"]  

