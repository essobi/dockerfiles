FROM ubuntu  
MAINTAINER konder "konders@gmail.com"  
RUN apt-get -qq update  
  
RUN apt-get install -y build-essential zip wget gcc make curl libpcre3-dev
openssl libssl-dev  
  
RUN wget -O /tmp/nginx-1.7.9.tar.gz
http://nginx.org/download/nginx-1.7.9.tar.gz && \  
wget -O /tmp/LuaJIT-2.0.3.tar.gz
http://luajit.org/download/LuaJIT-2.0.3.tar.gz && \  
wget -O /tmp/lua-nginx-module-0.9.13.zip https://github.com/openresty/lua-
nginx-module/archive/v0.9.13.zip && \  
wget -O /tmp/ngx_devel_kit-0.2.19.zip
https://github.com/simpl/ngx_devel_kit/archive/v0.2.19.zip && \  
wget -O /tmp/ngx_cache_purge-2.3.tar.gz
http://labs.frickle.com/files/ngx_cache_purge-2.3.tar.gz && \  
wget -O /tmp/luarocks-2.2.0.tar.gz
http://luarocks.org/releases/luarocks-2.2.0.tar.gz && \  
( cd /tmp/ && tar zxf nginx-1.7.9.tar.gz ) && \  
( cd /tmp/ && tar zxf LuaJIT-2.0.3.tar.gz ) && \  
( cd /tmp/ && tar zxf luarocks-2.2.0.tar.gz ) && \  
( cd /tmp/ && tar zxf ngx_cache_purge-2.3.tar.gz ) && \  
( cd /tmp/ && unzip lua-nginx-module-0.9.13.zip ) && \  
( cd /tmp/ && unzip ngx_devel_kit-0.2.19.zip ) && \  
rm -f /tmp/*.tar.gz && \  
rm -f /tmp/*.zip && \  
( bash && \  
cd /tmp/LuaJIT-2.0.3 && \  
make && \  
make install ) && \  
ln -s /usr/local/bin/luajit /usr/sbin/lua && \  
( bash && \  
cd /tmp/luarocks-2.2.0 && \  
./configure --with-lua-include=/usr/local/include/luajit-2.0 && \  
make bootstrap ) && \  
luarocks install lua-cjson && \  
( cd /tmp/nginx-1.7.9 && \  
export LUAJIT_LIB=/usr/local/lib && \  
export LUAJIT_INC=/usr/local/include/luajit-2.0 && \  
./configure --prefix=/etc/nginx \  
\--with-ld-opt=-Wl,-rpath,/usr/local/lib \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_gzip_static_module \  
\--with-ipv6 \  
\--add-module=../ngx_devel_kit-0.2.19 \  
\--add-module=../lua-nginx-module-0.9.13 \  
\--add-module=../ngx_cache_purge-2.3 && \  
make -j2 && \  
make install ) && \  
ln -s /usr/local/lib/libluajit-5.1.so.2 /lib64/libluajit-5.1.so.2 && \  
mkdir -p /var/cache/nginx/client_temp && \  
rm -rf /tmp/*  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN mkdir -p /var/log/nginx; mkdir -p /home/cache/  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.1/dockerize-linux-
amd64-v0.0.1.tar.gz  
RUN tar -C /usr/local/bin -xvzf dockerize-linux-amd64-v0.0.1.tar.gz  
  
EXPOSE 80  
EXPOSE 443  
  
CMD dockerize -stdout /var/log/nginx/access.log -stderr
/var/log/nginx/error.log nginx  
  

