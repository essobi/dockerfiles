#  
# - Base nginx  
#  
FROM ubuntu:14.04  
MAINTAINER JINWOO <jinwoo@yellotravel.com>  
#  
# Prepare the container  
#  
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
ENV NGINX_VERSION nginx-2.7  
RUN echo $NGINX_VERSION  
ENV DOCKERIZE_VERSION v0.2.0  
  
ENV NGINX_EXTRA_CONFIGURE_ARGS --sbin-path=/usr/sbin \  
\--conf-path=/etc/nginx/nginx.conf \  
\--with-md5=/usr/lib --with-sha1=/usr/lib \  
\--with-http_ssl_module --with-http_dav_module \  
\--without-mail_pop3_module --without-mail_imap_module \  
\--without-mail_smtp_module  
  
ENV NGINX_BUILD_DEPS bzip2 \  
file \  
libbz2-dev \  
libcurl4-openssl-dev \  
libmcrypt-dev \  
libreadline6-dev \  
openssl \  
libssl-dev \  
libxslt1-dev \  
libxml2-dev \  
libpcre3 \  
libpcre3-dev \  
curl \  
libc6  
ENV NGINX_EXTRA_BUILD_DEPS gcc libc-dev make pkg-config \  
libxml2 \  
ca-certificates \  
autoconf \  
runit nano less tmux wget git  
  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list

