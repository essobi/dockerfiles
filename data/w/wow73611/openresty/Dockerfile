FROM wow73611/ubuntu  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
ENV OPENRESTY_VERSION 1.7.7.2  
ENV NGINX_WORKDIR /usr/local/openresty/nginx  
  
RUN \  
apt-get update -y && \  
apt-get install -y libreadline-dev libncurses5-dev libpcre3-dev libssl-dev &&
\  
apt-get install -y perl make unzip luarocks lua5.1 liblua5.1-dev  
  
RUN \  
wget http://openresty.org/download/ngx_openresty-$OPENRESTY_VERSION.tar.gz &&
\  
tar -zxf ngx_openresty-*.tar.gz && \  
cd ngx_openresty-* && \  
./configure --with-luajit --with-pcre-jit && \  
make && \  
make install && \  
cd .. && \  
rm -f ngx_openresty-*.tar.gz && \  
rm -rf ngx_openresty-* && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR $NGINX_WORKDIR  
ADD nginx.conf $NGINX_WORKDIR/conf/nginx.conf  
ENV PATH $NGINX_WORKDIR/sbin:$PATH  
  
EXPOSE 80  
CMD ["nginx","-c","$NGINX_WORKDIR/conf/nginx.conf"]  

