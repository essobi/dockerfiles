FROM alpine:3.1  
MAINTAINER John Allen <john.allen@connexiolabs.com>  
  
ENV NGINX_VERSION nginx-1.7.11  
ENV DYNAMIC_VERSION f893a7971d85335127f080f03857065a22d82c79  
  
RUN apk --update add openssl-dev pcre-dev zlib-dev wget build-base && \  
mkdir -p /tmp/src && \  
cd /tmp/src && \  
wget --no-check-certificate https://github.com/GUI/nginx-upstream-dyanmic-
servers/archive/${DYNAMIC_VERSION}.tar.gz && \  
tar -zxvf ${DYNAMIC_VERSION}.tar.gz && \  
wget http://nginx.org/download/${NGINX_VERSION}.tar.gz && \  
tar -zxvf ${NGINX_VERSION}.tar.gz && \  
cd /tmp/src/${NGINX_VERSION} && \  
./configure \  
\--add-module=/tmp/src/nginx-upstream-dyanmic-servers-${DYNAMIC_VERSION} \  
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
rm -rf /var/cache/apk/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/log/nginx"]  
  
WORKDIR /etc/nginx  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

