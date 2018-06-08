FROM ubuntu:14.04  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
RUN apt-get -y install git curl wget unzip vim  
RUN apt-get -y install libreadline-dev libncurses5-dev libpcre3-dev libssl-dev
libpq-dev perl make  
RUN git clone https://github.com/ontouchstart/ngx_openresty.git  
RUN cd ngx_openresty && make  
RUN cd ngx_openresty/ngx_openresty-$(ngx_openresty/util/ver) && \  
./configure \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--without-http_redis2_module \  
\--with-http_iconv_module \  
\--with-http_postgres_module \  
-j2 && \  
make install  
RUN /usr/local/openresty/bin/resty -V  
RUN wget http://luarocks.org/releases/luarocks-2.2.0.tar.gz  
RUN tar -xzvf luarocks-2.2.0.tar.gz  
RUN cd luarocks-2.2.0/ && \  
./configure --prefix=/usr/local/openresty/luajit \  
\--with-lua=/usr/local/openresty/luajit/ \  
\--lua-suffix=jit-2.1.0-alpha \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 && \  
make && \  
make install  
RUN ln -s /usr/local/openresty/luajit/bin/luajit-2.1.0-alpha
/usr/local/bin/lua  
RUN ln -s /usr/local/openresty/luajit/bin/luarocks /usr/local/bin/luarocks  
RUN luarocks  
ADD work work  
CMD ["/work/server"]  

