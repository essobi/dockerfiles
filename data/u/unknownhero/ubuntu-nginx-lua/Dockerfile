FROM ubuntu  
RUN apt-get -qq update  
  
RUN apt-get install -y build-essential zip wget gcc make curl libpcre3-dev
openssl libssl-dev gettext  
  
RUN curl -L
https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux >
/usr/local/bin/envplate \  
&& echo -n "8366c3c480379dc325dea725aac86212c5f5d1bf55f5a9ef8e92375f42d55a41
/usr/local/bin/envplate"|sha256sum -c \  
&& chmod 755 /usr/local/bin/envplate  
  
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
( cd /tmp/ && tar zxf nginx-1.7.9.tar.gz ) && \  
( cd /tmp/ && tar zxf LuaJIT-2.0.3.tar.gz ) && \  
( cd /tmp/ && tar zxf ngx_cache_purge-2.3.tar.gz ) && \  
( cd /tmp/ && unzip lua-nginx-module-0.9.13.zip ) && \  
( cd /tmp/ && unzip ngx_devel_kit-0.2.19.zip ) && \  
rm -f /tmp/*.tar.gz && \  
rm -f /tmp/*.zip && \  
( bash && \  
cd /tmp/LuaJIT-2.0.3 && \  
make && \  
make install ) && \  
( cd /tmp/nginx-1.7.9 && \  
export LUAJIT_LIB=/usr/local/lib && \  
export LUAJIT_INC=/usr/local/include/luajit-2.0 && \  
./configure --prefix=/etc/nginx --with-ld-opt=-Wl,-rpath,/usr/local/lib
--sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-
path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-
path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-
temp-path=/var/cache/nginx/client_temp --http-proxy-temp-
path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-
path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-
path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-
path=/var/cache/nginx/scgi_temp --with-http_ssl_module --with-
http_realip_module --with-http_addition_module --with-http_sub_module --with-
http_dav_module --with-http_flv_module --with-http_mp4_module --with-
http_gunzip_module --with-http_gzip_static_module --with-
http_random_index_module --with-http_secure_link_module --with-
http_stub_status_module --with-http_auth_request_module --with-mail --with-
mail_ssl_module --with-file-aio --with-ipv6 --with-http_spdy_module --add-
module=../ngx_devel_kit-0.2.19 \--add-module=../lua-nginx-module-0.9.13
\--add-module=../ngx_cache_purge-2.3 && \  
make -j2 && \  
make install ) && \  
ln -s /usr/local/lib/libluajit-5.1.so.2 /lib64/libluajit-5.1.so.2 && \  
mkdir -p /etc/nginx/sites && \  
mkdir -p /etc/nginx/certs && \  
mkdir -p /var/cache/nginx/client_temp && \  
rm -rf /tmp/*  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
WORKDIR /etc/nginx  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
EXPOSE 80  
EXPOSE 443  
CMD ["nginx"]  
  

