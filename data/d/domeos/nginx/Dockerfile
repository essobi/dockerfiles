FROM alpine:3.2  
MAINTAINER domeos  
  
ENV NGINX_VERSION nginx-1.9.4  
RUN mkdir -p /tmp/src  
  
RUN apk update && apk upgrade && \  
apk --apdate add openssl-dev pcre-dev zlib-dev bash curl build-base && \  
curl -ssL http://nginx.org/download/${NGINX_VERSION}.tar.gz -o
/tmp/src/${NGINX_VERSION}.tar.gz && \  
cd /tmp/src && \  
tar -zxvf ${NGINX_VERSION}.tar.gz && \  
cd /tmp/src/${NGINX_VERSION} && \  
./configure \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--prefix=/etc/nginx \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--sbin-path=/usr/local/sbin/nginx && \  
make && \  
make install && \  
apk del build-base && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/* && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/log/nginx"]  
  
WORKDIR /etc/nginx  
  
EXPOSE 80 433  
CMD ["nginx", "-g", "daemon off;"]  
  

