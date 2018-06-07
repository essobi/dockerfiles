FROM centos  
  
WORKDIR /usr/local/openresty  
  
RUN yum-config-manager --add-repo
https://openresty.org/yum/centos/OpenResty.repo && \  
yum install -y openresty unzip gcc make openssl && \  
curl -O http://luarocks.github.io/luarocks/releases/luarocks-2.4.2.tar.gz && \  
tar xzf luarocks-2.4.2.tar.gz && \  
cd luarocks-2.4.2 && \  
./configure --prefix=/usr/local/openresty/luajit/ \--with-lua-
include=/usr/local/openresty/luajit/include/luajit-2.1 && \  
make build && make install && \  
rm -rf luarocks-2.4.2* && \  
ln -s /usr/local/openresty/luajit/bin/luarocks /usr/local/bin/ && \  
luarocks install lua-resty-auto-ssl && \  
chmod 755 /usr/local/openresty/luajit/share/lua/5.1/resty/auto-
ssl/shell/start_sockproc && \  
chmod 755 /usr/local/openresty/luajit/share/lua/5.1/resty/auto-
ssl/vendor/sockproc && \  
chmod 755 /usr/local/openresty/luajit/share/lua/5.1/resty/auto-
ssl/vendor/dehydrated && \  
chmod 755 /usr/local/openresty/luajit/share/lua/5.1/resty/auto-
ssl/shell/letsencrypt_hooks  
  
ADD certs.d nginx.conf /usr/local/openresty/nginx/conf/  
  
CMD ["openresty", "-g", "daemon off;"]  

