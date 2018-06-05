FROM alpine:latest  
  
MAINTAINER Trung Nguyen Dinh <nguyendinhtrung141@gmail.com>  
  
ADD http://ftp.gnu.org/gnu/bison/bison-2.7.tar.gz /tmp/  
ADD http://kannel.org/download/1.4.4/gateway-1.4.4.tar.gz /tmp/  
  
RUN apk update && apk add \--no-cache libxml2 mariadb-client-libs pcre musl
hiredis \  
&& apk add \--no-cache libxml2-dev mariadb-dev pcre-dev g++ musl-dev hiredis-
dev make perl m4 \  
&& ln -sf /usr/include/poll.h /usr/include/sys/poll.h \  
&& ln -sf /usr/include/unistd.h /usr/include/sys/unistd.h \  
&& tar -xzpf /tmp/bison-2.7.tar.gz -C /tmp/ && tar -xzpf
/tmp/gateway-1.4.4.tar.gz -C /tmp/ \  
&& cd /tmp/bison-2.7 && ./configure && make && make install \  
&& cd /tmp/gateway-1.4.4 && ./configure \--with-mysql \--with-redis && make &&
make install \  
&& cd /tmp/gateway-1.4.4/addons/opensmppbox && ./configure && make && make
install \  
&& cd /tmp/gateway-1.4.4/addons/sqlbox && ./configure && make && make install
\  
&& apk del libxml2-dev mariadb-dev pcre-dev g++ musl-dev hiredis-dev make perl
m4 \  
&& rm -rf /tmp/* && mkdir -p /var/log/kannel && mkdir -p /var/spool/kannel &&
mkdir -p /var/run/kannel && mkdir -p /etc/kannel  

