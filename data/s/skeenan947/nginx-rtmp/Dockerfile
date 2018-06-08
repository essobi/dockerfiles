FROM alpine:latest  
MAINTAINER Shaun Keenan <skeenan@gmail.com>  
  
WORKDIR /tmp  
  
RUN apk --no-cache add \  
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
openssl-dev \  
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
coreutils \  
make  
  
ENV NGINX_VERSION 1.13.5  
RUN curl -O http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
git clone https://github.com/arut/nginx-rtmp-module.git  
  
RUN tar xzf nginx-${NGINX_VERSION}.tar.gz && \  
cd nginx-${NGINX_VERSION} && \  
./configure \  
\--prefix=/opt/nginx \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module \  
\--with-http_ssl_module \  
\--add-module=../nginx-rtmp-module && \  
make && \  
make install  
  
FROM alpine:latest  
MAINTAINER Shaun Keenan <skeenan@gmail.com>  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 1935  
EXPOSE 8090  
EXPOSE 8081  
VOLUME /etc/letsencrypt  
VOLUME /video  
  
RUN apk --no-cache add ca-certificates openssl libstdc++ pcre ffmpeg  
WORKDIR /opt  
  
RUN adduser -D www-data  
  
COPY \--from=0 /opt/nginx /opt/nginx  
COPY conf/ /opt/nginx/conf/  
COPY run.sh /opt/nginx/run.sh  
RUN chown -R www-data: /opt/nginx  
  
WORKDIR /opt/nginx  
RUN mkdir -p /var/log/nginx  
CMD sh -x ./run.sh  

