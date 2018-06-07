FROM centos  
MAINTAINER Yoshiaki Kawazu <kawazzz@gmail.com>  
  
## nginx  
RUN yum -y install git tar make gcc-c++  
RUN yum -y install lua-devel openssl-devel pcre-devel zlib-devel  
RUN mkdir -p /usr/local/src/luagit-2.0 && cd $_ && curl -sL
http://luajit.org/download/LuaJIT-2.0.3.tar.gz | tar xz --strip=1 && make &&
make install  
RUN git clone git://github.com/simpl/ngx_devel_kit.git
/usr/local/src/ngx_devel_kit  
RUN git clone git://github.com/chaoslawful/lua-nginx-module.git
/usr/local/src/lua-nginx-module  
RUN v=1.7.3; curl -sL http://nginx.org/download/nginx-$v.tar.gz | tar xz && cd
nginx-$v && ./configure \  
\--add-module=/usr/local/src/ngx_devel_kit \  
\--add-module=/usr/local/src/lua-nginx-module \  
\--with-file-aio \  
\--with-ipv6 \  
\--with-http_ssl_module \  
\--with-http_spdy_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_auth_request_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module && make && make install  
ENV PATH /usr/local/nginx/sbin:$PATH  
  
EXPOSE 80  
#ENTRYPOINT [ "/usr/local/nginx/sbin/nginx", "-g", "daemon off;" ]  
CMD [ "/usr/local/nginx/sbin/nginx", "-g", "daemon off;" ]  

