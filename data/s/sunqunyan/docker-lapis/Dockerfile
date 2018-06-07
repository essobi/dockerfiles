# Dockerfile for lapis in centos  
FROM centos:7  
MAINTAINER Qunyan Sun <sunqunyan@gmail.com>  
  
RUN yum install -y gcc pcre-devel openssl openssl-devel libreadline-dev
libncurses5-dev libpcre3-dev libssl-dev perl make curl git-core lua-devel
unzip wget  
  
ENV SRC_DIR /usr/local  
ENV OPENRESTY_VERSION 1.11.2.4  
ENV OPENRESTY_PREFIX /usr/local/openresty  
ENV LAPIS_VERSION 1.6.0  
RUN cd $SRC_DIR && curl -LOs
https://openresty.org/download/openresty-$OPENRESTY_VERSION.tar.gz \  
&& tar xzf openresty-$OPENRESTY_VERSION.tar.gz && cd
openresty-$OPENRESTY_VERSION \  
&& ./configure --prefix=$OPENRESTY_PREFIX \  
\--with-luajit \  
\--with-http_realip_module \  
\--with-http_stub_status_module \  
&& make && make install && rm -rf openresty-$OPENRESTY_VERSION*  
  
RUN cd $SRC_DIR && wget
https://keplerproject.github.io/luarocks/releases/luarocks-2.4.1.tar.gz \  
&& tar xzf luarocks-2.4.1.tar.gz && cd luarocks-2.4.1 \  
&& ./configure \  
&& make build && make install && rm -rf luarocks-2.4.1*  
  
RUN luarocks install --server=http://rocks.moonscript.org/manifests/leafo
lapis $LAPIS_VERSION  
RUN luarocks install moonscript  
RUN luarocks install lapis-console  
  
WORKDIR $OPENRESTY_PREFIX/nginx/conf  
  
ENV LAPIS_OPENRESTY $OPENRESTY_PREFIX/nginx/sbin/nginx  
  
EXPOSE 8080  
EXPOSE 80  
EXPOSE 9090  
RUN mv nginx.conf nginx.conf.bk && lapis new && moonc *.moon  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
ENTRYPOINT ["lapis"]  
CMD ["server", "production"]  

