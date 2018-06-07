FROM alpine:latest  
#定义nginx版本  
ENV NGINX_VERSION 1.12.1  
  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gd-dev \  
jemalloc-dev \  
git && \  
  
mkdir -p /var/run/nginx/ && \  
wget -c http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar -zxvf nginx-${NGINX_VERSION}.tar.gz && \  
cd nginx-${NGINX_VERSION} && \  
addgroup -S www && adduser -S -g www www && \  
#隐藏nginx版本信息  
#sed -i -e 's/${NGINX_VERSION}//g' -e 's/nginx\//ERROR/g' -e
's/"NGINX"/"ERROR"/g' src/core/nginx.h && \  
./configure --prefix=/usr/local/nginx \  
\--user=www \  
\--group=www \  
\--with-pcre \  
\--with-http_stub_status_module \  
\--with-http_ssl_module \  
\--with-ld-opt="-ljemalloc" && \  
make -j $(awk '/processor/{i++}END{print i}' /proc/cpuinfo) && make install &&
\  
  
#清理安装产生的文件  
rm -rf ../{ngx*,nginx*}  
#rm ../nginx-${NGINX_VERSION}.tar.gz && \  
#不能删!  
#apk del .build-deps  
  
#启动nginx，保留一个前台进程，以免被docker强制退出  
CMD ./usr/local/nginx/sbin/nginx && tail -f /usr/local/nginx/logs/error.log  

