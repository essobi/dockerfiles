#http://qiita.com/hnakamur/items/0b72590136cece29faee  
FROM typista/base  
#FROM typista/base:0.4  
  
RUN wget https://raw.githubusercontent.com/typista/docker-nginx-
lua/master/files/entrypoint.sh -O /etc/entrypoint.sh && \  
echo "#########################" && \  
echo " install LuaJIT" && \  
echo "#########################" && \  
cd /usr/local/src && \  
curl -O http://luajit.org/download/LuaJIT-2.0.3.tar.gz && \  
tar xf LuaJIT-2.0.3.tar.gz && \  
cd LuaJIT-2.0.3 && \  
make && \  
make PREFIX=/usr/local/luajit install && \  
adduser nginx && \  
export LUAJIT_LIB=/usr/local/luajit/lib && \  
export LUAJIT_INC=/usr/local/luajit/include/luajit-2.0 && \  
cd /usr/local/src && \  
git clone git://github.com/simpl/ngx_devel_kit.git && \  
git clone git://github.com/chaoslawful/lua-nginx-module.git && \  
curl -LO
http://downloads.sourceforge.net/project/pcre/pcre/8.36/pcre-8.36.tar.bz2 && \  
tar xf pcre-8.36.tar.bz2 && \  
echo "#########################" && \  
echo " install nginx" && \  
echo "#########################" && \  
curl -O http://nginx.org/download/nginx-1.7.6.tar.gz && \  
tar xf nginx-1.7.6.tar.gz && \  
cd nginx-1.7.6 && \  
./configure --prefix=/usr/local/nginx \  
\--user=nginx \  
\--group=nginx \  
\--with-http_ssl_module \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-pcre=/usr/local/src/pcre-8.36 \  
\--add-module=/usr/local/src/ngx_devel_kit \  
\--add-module=/usr/local/src/lua-nginx-module \  
\--with-ld-opt="-Wl,-rpath,$LUAJIT_LIB" && \  
make && \  
make install && \  
chmod +x /etc/entrypoint.sh  
#EXPOSE 80  

