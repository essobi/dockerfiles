FROM alpine:3.4  
  
MAINTAINER nechehin "nechehin@gmail.com"  
  
ENV NGINX_VERSION 1.13.9  
  
WORKDIR /tmp  
  
RUN apk add --no-cache --virtual .build-deps \  
ca-certificates \  
git \  
gcc \  
libc-dev \  
linux-headers \  
make \  
openssl-dev \  
pcre-dev \  
wget \  
zlib-dev \  
&& apk --update add tar \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -O
nginx.tar.gz \  
&& mkdir /tmp/nginx \  
&& tar -xvzf nginx.tar.gz -C /tmp/nginx --strip-components=1 \  
&& git clone https://github.com/wandenberg/nginx-push-stream-module.git
nginx/nginx-push-stream-module  
  
WORKDIR /tmp/nginx  
  
RUN addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& ./configure \  
\--with-http_realip_module \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--add-module=nginx-push-stream-module \  
\--user=nginx \  
\--group=nginx \  
&& make \  
&& make install \  
&& apk del wget git gcc \  
&& rm -rf /tmp/* \  
&& mkdir /usr/local/nginx/conf/upstreams  
  
  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /usr/local/nginx/logs/access.log \  
&& ln -sf /dev/stderr /usr/local/nginx/logs/error.log  
  
COPY ./conf/ /usr/local/nginx/conf/  
  
EXPOSE 80 443  
  
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]  

