FROM centos:7.3.1611  
RUN rm /etc/yum.repos.d/CentOS-Base.repo  
ADD http://mirrors.aliyun.com/repo/Centos-7.repo /etc/yum.repos.d/CentOS-
Base.repo  
RUN \  
yum makecache && \  
yum -y install gcc gcc-c++ make libtool zlib zlib-devel openssl openssl-devel
libssl-dev pcre pcre-devel patch unzip bzip2  
# openssl-libs-1.0.1e-60.el7_3.1.x86_64  
# zlib-1.2.7-17.el7.x86_64  
# ENV lua_v=lua-5.1  
ENV nginx_v=nginx-1.11.1  
ENV ngx_devel_kit_v=ngx_devel_kit-0.3.0  
ENV lua_nginx_module_v=lua-nginx-module-0.10.5  
ENV lua-upstream-nginx-module_v=lua-upstream-nginx-module-0.06  
ENV nginx_upstream_check_module_v=nginx_upstream_check_module-master  
ENV luajit_v=LuaJIT-2.1.0-beta2  
ENV jemalloc_v=jemalloc-4.5.0  
ENV lua-cjson_v=lua-cjson-2.1.0  
# ADD http://www.lua.org/ftp/lua-5.1.tar.gz /usr/local/src/$lua_v.tar.gz  
ADD http://nginx.org/download/nginx-1.11.1.tar.gz
/usr/local/src/$nginx_v.tar.gz  
ADD http://luajit.org/download/LuaJIT-2.1.0-beta2.tar.gz
/usr/local/src/$luajit_v.tar.gz  
ADD https://github.com/simpl/ngx_devel_kit/archive/v0.3.0.tar.gz
/usr/local/src/$ngx_devel_kit_v.tar.gz  
ADD https://www.kyne.com.au/~mark/software/download/lua-cjson-2.1.0.tar.gz
/usr/local/src/$lua-cjson_v.tar.gz  
ADD https://github.com/openresty/lua-nginx-module/archive/v0.10.5.tar.gz
/usr/local/src/$lua_nginx_module_v.tar.gz  
ADD https://github.com/openresty/lua-upstream-nginx-
module/archive/v0.06.tar.gz /usr/local/src/$lua-upstream-nginx-module_v.tar.gz  
# ADD
https://github.com/yaoweibin/nginx_upstream_check_module/archive/v0.3.0.tar.gz
/usr/local/src/$nginx_upstream_check_module_v.tar.gz  
ADD
https://codeload.github.com/yaoweibin/nginx_upstream_check_module/zip/master
/usr/local/src/$nginx_upstream_check_module_v.tar.gz  
ADD https://github.com/jemalloc/jemalloc/archive/4.5.0.tar.gz
/usr/local/src/$jemalloc_v.tar.gz  
# ADD http://www.canonware.com/download/jemalloc/jemalloc-3.6.0.tar.bz2
/usr/local/src/$jemalloc_v.tar.bz2  
WORKDIR /usr/local/src  
RUN \  
tar xvf $nginx_v.tar.gz && \  
tar xvf $luajit_v.tar.gz && \  
tar xvf $jemalloc_v.tar.gz && \  
tar xvf $lua-cjson_v.tar.gz && \  
tar xvf $ngx_devel_kit_v.tar.gz && \  
tar xvf $lua_nginx_module_v.tar.gz && \  
tar xvf $lua-upstream-nginx-module_v.tar.gz && \  
unzip $nginx_upstream_check_module_v.tar.gz  
  
WORKDIR /usr/local/src/$luajit_v  
RUN make PREFIX=/usr/local/luajit && make install PREFIX=/usr/local/luajit  
  
# RUN cd ../ && sed -i -e 's/${NGINX_VERSION}//g' -e 's/nginx\//ERROR/g' -e
's/"NGINX"/"ERROR"/g' src/core/nginx.h  
WORKDIR /usr/local/src/lua-cjson-2.1.0  
RUN \  
sed -i '14s#5.1#luajit-2.1#' Makefile && \  
sed -i '16s#/usr/local#/usr/local/luajit#' Makefile && \  
sed -i '21s#include#include/$(LUA_VERSION)#' Makefile && \  
sed -i '22s#$(LUA_VERSION)#5.1#' Makefile && \  
make && \  
make install  
  
WORKDIR /usr/local/src/$jemalloc_v  
RUN ./autogen.sh && touch doc/jemalloc.html doc/html.xsl doc/jemalloc.xml
doc/jemalloc.3 && make && make install  
RUN echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf && ldconfig  
  
WORKDIR /usr/local/src/$nginx_v  
RUN patch -p0 <
/usr/local/src/$nginx_upstream_check_module_v/check_1.11.1+.patch  
WORKDIR /usr/local/src/$nginx_v  
RUN \  
export LUAJIT_LIB=/usr/local/luajit/lib && \  
export LUAJIT_INC=/usr/local/luajit/include/luajit-2.1 && \  
./configure --prefix=/usr/local/nginx \  
\--user=www --group=www \  
\--with-pcre \  
\--with-stream \  
\--with-http_v2_module \  
\--with-http_ssl_module \  
\--with-ld-opt=-ljemalloc \  
\--with-ld-opt="-Wl,-rpath,$LUAJIT_LIB" \  
\--with-http_realip_module \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module \  
\--add-module=/usr/local/src/$ngx_devel_kit_v \  
\--add-module=/usr/local/src/$lua_nginx_module_v \  
\--add-module=/usr/local/src/lua-upstream-nginx-module-0.06 \  
\--add-module=/usr/local/src/$nginx_upstream_check_module_v && \  
make && \  
make install  
  
WORKDIR /usr/local/nginx  
COPY get_env.lua /usr/local/nginx/lua_modules/get_env.lua  
COPY boot.sh /boot.sh  
RUN chmod +x /boot.sh  
  
RUN yum clean all && rm -rf /usr/local/src/*.gz  
# EXPOSE 80 443  
ENTRYPOINT ["/boot.sh"]  

