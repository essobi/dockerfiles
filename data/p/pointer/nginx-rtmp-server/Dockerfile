FROM alpine:latest  
MAINTAINER thomaspb  
  
ENV NGINX_VERSION 1.12.2  
ENV TOKEN 123456  
ENV AUTHURL http://localhost/auth.php  
  
RUN apk update && \  
apk add \  
git \  
gcc \  
binutils-libs \  
binutils \  
gmp \  
isl \  
libgomp \  
libatomic \  
libgcc \  
openssl \  
pkgconf \  
pkgconfig \  
mpfr3 \  
mpc1 \  
libstdc++ \  
ca-certificates \  
libssh2 \  
curl \  
expat \  
pcre \  
musl-dev \  
libc-dev \  
pcre-dev \  
zlib-dev \  
openssl-dev \  
php7-fpm \  
make  
  
RUN cd /tmp/ && \  
wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
git clone https://github.com/arut/nginx-rtmp-module.git  
  
RUN cd /tmp && \  
tar xzf nginx-${NGINX_VERSION}.tar.gz && \  
cd nginx-${NGINX_VERSION} && \  
./configure \  
\--prefix=/opt/nginx \  
\--with-http_ssl_module \  
\--add-module=../nginx-rtmp-module && \  
make && \  
make install  
  
RUN cd /opt/ && \  
tar cvzf /tmp/nginx.tar.gz nginx  
  
ADD nginx.conf /opt/nginx/conf/nginx.conf  
ADD auth.php /opt/nginx/html/auth.php  
ADD start.sh /root/start.sh  
  
EXPOSE 1935  
EXPOSE 80  
CMD ["sh", "/root/start.sh"]  

