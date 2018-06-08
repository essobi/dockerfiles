# Openresty  
#  
# VERSION 1.7.10.1  
# use the centos base image provided by dotCloud  
FROM centos  
MAINTAINER Marco Palladino, marco@mashape.com  
  
# Dependencies versions  
ENV OPENRESTY_VERSION 1.7.10.1  
ENV LUAROCKS_VERSION 2.2.0  
ENV LUA_VERSION 5.1.5  
# make sure the system is up to date  
RUN yum -y upgrade  
  
# install dependencies required to compile and build OpenResty  
RUN yum -y install wget tar perl gcc-c++ readline-devel pcre-devel openssl-
devel git make unzip  
  
# download Lua  
RUN cd /tmp && wget http://www.lua.org/ftp/lua-$LUA_VERSION.tar.gz && tar xzf
lua-$LUA_VERSION.tar.gz  
  
# configure, build and install Lua  
run cd /tmp/lua-$LUA_VERSION && make linux && make install  
  
# download LuaRocks  
RUN cd /tmp && wget
http://luarocks.org/releases/luarocks-$LUAROCKS_VERSION.tar.gz && tar xzf
luarocks-$LUAROCKS_VERSION.tar.gz  
  
# configure, build and install LuaRocks  
RUN cd /tmp/luarocks-$LUAROCKS_VERSION && ./configure && make build && make
install  
  
# download OpenResty  
RUN cd /tmp && wget
http://openresty.org/download/ngx_openresty-$OPENRESTY_VERSION.tar.gz && tar
xzf ngx_openresty-$OPENRESTY_VERSION.tar.gz  
  
# configure, build and install OpenResty  
RUN cd /tmp/ngx_openresty-$OPENRESTY_VERSION && ./configure --with-luajit
--with-http_realip_module --with-pcre-jit --with-ipv6 && make && make install  
  
# adding OpenResty to the PATH  
ENV PATH $PATH:/usr/local/openresty/nginx/sbin  

