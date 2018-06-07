FROM openresty/openresty:1.11.2.1-centos  
RUN yum install -y openssl-devel  
RUN /usr/local/openresty/luajit/bin/luarocks install luaossl && \  
/usr/local/openresty/luajit/bin/luarocks install lapis  
ENV
PATH=$PATH:/usr/local/openresty/luajit/bin:/usr/local/openresty/nginx/sbin:/usr/local/openresty/bin

