FROM openresty/openresty:alpine-fat  
  
RUN \  
apk update && \  
apk add \  
\--virtual build-deps \  
make gcc musl-dev \  
pcre-dev openssl-dev zlib-dev ncurses-dev readline-dev \  
curl perl git lua-dev luajit-dev python && \  
git clone --recursive --branch v0.11.1 \--depth 1
https://github.com/p0pr0ck5/lua-resty-waf.git /tmp/lua-resty-waf && \  
cd /tmp/lua-* && \  
make lua-aho-corasick lua-resty-htmlentities libinjection decode && \  
make install && \  
sed -i 's/mime.types/\/usr\/local\/openresty\/nginx\/conf\/mime.types/g'
/usr/local/openresty/nginx/conf/nginx.conf && \  
sed -i 's/#access_log/access_log \/dev\/stdout;#/g'
/usr/local/openresty/nginx/conf/nginx.conf && \  
cp -pR '/usr/local/openresty/nginx/conf/.' '/etc/nginx/' && \  
echo "daemon off;error_log /dev/stdout;" >> "/etc/nginx/nginx.conf" && \  
ln -s /usr/local/openresty/bin/openresty /usr/local/bin/nginx && \  
cd / && \  
rm -rf /tmp/lua-* && \  
apk del build-deps && \  
rm -rf /var/cache/apk/*  

