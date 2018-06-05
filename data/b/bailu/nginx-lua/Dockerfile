FROM centos:centos6  
  
ENV VER_NGINX_DEVEL_KIT=0.2.19  
ENV VER_LUA_NGINX_MODULE=0.9.16  
ENV VER_NGINX=1.9.3  
ENV VER_LUAJIT=2.0.4  
ENV NGINX_DEVEL_KIT ngx_devel_kit-${VER_NGINX_DEVEL_KIT}  
ENV LUA_NGINX_MODULE lua-nginx-module-${VER_LUA_NGINX_MODULE}  
ENV NGINX_ROOT=/nginx  
ENV WEB_DIR ${NGINX_ROOT}/html  
  
ENV LUAJIT_LIB /usr/local/lib  
ENV LUAJIT_INC /usr/local/include/luajit-2.0  
# ***** BUILD DEPENDENCIES *****  
# Common dependencies (Nginx and LUAJit)  
RUN yum -y install wget tar make gcc-c++  
RUN yum -y install lua-devel openssl-devel pcre-devel zlib-devel  
# ***** DOWNLOAD AND UNTAR *****  
# Download  
RUN wget http://nginx.org/download/nginx-${VER_NGINX}.tar.gz  
RUN wget http://luajit.org/download/LuaJIT-${VER_LUAJIT}.tar.gz  
RUN wget
https://github.com/simpl/ngx_devel_kit/archive/v${VER_NGINX_DEVEL_KIT}.tar.gz
-O ${NGINX_DEVEL_KIT}.tar.gz  
RUN wget https://github.com/openresty/lua-nginx-
module/archive/v${VER_LUA_NGINX_MODULE}.tar.gz -O ${LUA_NGINX_MODULE}.tar.gz  
# Untar  
RUN tar -xzvf nginx-${VER_NGINX}.tar.gz && rm nginx-${VER_NGINX}.tar.gz  
RUN tar -xzvf LuaJIT-${VER_LUAJIT}.tar.gz && rm LuaJIT-${VER_LUAJIT}.tar.gz  
RUN tar -xzvf ${NGINX_DEVEL_KIT}.tar.gz && rm ${NGINX_DEVEL_KIT}.tar.gz  
RUN tar -xzvf ${LUA_NGINX_MODULE}.tar.gz && rm ${LUA_NGINX_MODULE}.tar.gz  
  
# ***** BUILD FROM SOURCE *****  
# LuaJIT  
WORKDIR /LuaJIT-${VER_LUAJIT}  
RUN make  
RUN make install  
# Nginx with LuaJIT  
WORKDIR /nginx-${VER_NGINX}  
RUN ./configure --prefix=${NGINX_ROOT} \--with-ld-
opt="-Wl,-rpath,${LUAJIT_LIB}" \--add-module=/${NGINX_DEVEL_KIT} \--add-
module=/${LUA_NGINX_MODULE}  
RUN make -j2  
RUN make install  
RUN ln -s ${NGINX_ROOT}/sbin/nginx /usr/local/sbin/nginx  
  
WORKDIR ${NGINX_ROOT}/conf  
RUN wget https://raw.githubusercontent.com/bailu/17moncn/master/ngx_lua/ip.lua  
RUN mv nginx.conf nginx.conf.bak  
RUN wget https://github.com/bailu/17moncn/raw/master/ngx_lua/nginx.conf  
  
ADD ./17monipdb.dat ${NGINX_ROOT}/conf/17monipdb.dat  
  
# ***** MISC *****  
WORKDIR ${WEB_DIR}  
EXPOSE 80  
# ***** CLEANUP *****  
RUN rm -rf /nginx-${VER_NGINX}  
RUN rm -rf /LuaJIT-${VER_LUAJIT}  
RUN rm -rf /${NGINX_DEVEL_KIT}  
RUN rm -rf /${LUA_NGINX_MODULE}  
# TODO: Uninstall build only dependencies?  
# TODO: Remove env vars used only for build?  
# This is the default CMD used by nginx:1.9.2 image  
CMD ["nginx", "-g", "daemon off;"]  

