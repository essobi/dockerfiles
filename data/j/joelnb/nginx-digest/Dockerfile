FROM alpine:3.6  
MAINTAINER Joel Noyce Barnham <joelnbarnham@gmail.com>  
  
ENV NGINX_VERSION=1.10.1  
  
RUN \  
apk add \--no-cache \--virtual build-deps \  
build-base \  
git \  
gnupg \  
wget \  
&& \  
apk add \--no-cache \  
openssl-dev \  
pcre-dev \  
python \  
zlib-dev \  
&& \  
apk add \--no-cache \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
tini \  
&& \  
wget -O - http://nginx.org/keys/mdounin.key | gpg \--import && \  
wget -O /tmp/nginx-${NGINX_VERSION}.tar.gz
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
wget -O /tmp/nginx-${NGINX_VERSION}.tar.gz.asc
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz.asc && \  
gpg \--verify /tmp/nginx-${NGINX_VERSION}.tar.gz.asc && \  
cd /tmp && \  
git clone https://github.com/atomx/nginx-http-auth-digest.git && \  
tar zxvf nginx-${NGINX_VERSION}.tar.gz && \  
cd nginx-${NGINX_VERSION} && \  
./configure \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--prefix=/etc/nginx \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--sbin-path=/usr/local/sbin/nginx \  
\--add-module=../nginx-http-auth-digest \  
&& \  
make && \  
make install && \  
cp /tmp/nginx-http-auth-digest/htdigest.py /usr/local/bin/ && \  
apk del build-deps && \  
rm -rf /tmp/* && \  
:  
  
RUN \  
mkdir -p /opt/httpd/conf/ && \  
cp -r /etc/nginx/html/ /etc/nginx/private/ && \  
:  
  
COPY ["nginx.conf", "/etc/nginx/conf/nginx.conf"]  
COPY ["passwd.digest", "/opt/httpd/conf/"]  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["nginx", "-g", "daemon off;"]  

