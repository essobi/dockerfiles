  
FROM alpine:3.3  
MAINTAINER Florian Girardey <florian@girardey.net>  
  
ENV NGINX_VERSION 1.9.12  
RUN apk --update add openssl-dev pcre-dev zlib-dev curl build-base \  
&& cd /tmp \  
&& curl -O http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && tar
-zxvf nginx-${NGINX_VERSION}.tar.gz \  
&& cd /tmp/nginx-${NGINX_VERSION} \  
&& ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/local/sbin/nginx \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--with-http_v2_module \  
&& make -j $(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make install \  
&& apk del build-base \  
&& rm -rf /tmp/* \  
/var/cache/apk/* \  
/usr/share/man \  
&& apk search --update  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
WORKDIR /etc/nginx  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

