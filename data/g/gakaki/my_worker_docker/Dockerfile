FROM openresty/openresty:alpine-fat  
  
MAINTAINER gakaki <gakaki@qq.com>  
  
RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/main/" >
/etc/apk/repositories \  
&& apk update \  
&& apk add --no-cache gd perl ncurses-libs ncurses-dev pcre-dev linux-headers
wget build-base autoconf re2c tar make file \  
libtool git mysql-client curl-dev libmcrypt libmcrypt-dev openssh-client icu-
dev \  
libxml2-dev freetype-dev libpng libpng-dev libjpeg-turbo-dev g++ autoconf \  
libgcrypt libcurl libedit ncurses-libs \  
gcc libc-dev pkgconf openssl-dev sqlite-dev  
# && /usr/local/openresty/luajit/bin/luarocks install moonscript \  
# && /usr/local/openresty/luajit/bin/luarocks install lapis  
# && /usr/local/openresty/luajit/bin/luarocks install moonrocks  
VOLUME ["/var/www"]  
EXPOSE 80  
ENTRYPOINT ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]  

