FROM centos:7  
MAINTAINER Cloud Mario <smcz@qq.com>  
  
# Base  
RUN yum -y update  
RUN yum clean all  
  
# 安装依赖  
RUN yum -y --nogpgcheck install readline-devel pcre-devel openssl-devel gcc
uuid-devel wget perl make  
  
# OpenSSL  
RUN cd /usr/local/src && \  
wget https://www.openssl.org/source/openssl-1.0.2-latest.tar.gz && \  
tar -zxf openssl-1.0.2-latest.tar.gz -C /usr/local/ && \  
cd /usr/local/openssl-1.0.2n && \  
./config && \  
make depend && \  
make && \  
make test && \  
make install && \  
(mv /usr/bin/openssl /usr/bin/openssl_1.0.1e || true) && \  
ln -s /usr/local/ssl/bin/openssl /usr/bin/openssl && \  
openssl version  
  
# OpenResty  
RUN cd /usr/local/src && \  
wget "https://openresty.org/download/openresty-1.11.2.5.tar.gz" && \  
tar -xzvf openresty-1.11.2.5.tar.gz && \  
cd openresty-1.11.2.5 && \  
./configure --prefix=/opt/openresty \  
\--with-luajit \  
\--without-http_redis2_module \  
\--with-http_iconv_module \  
\--with-http_ssl_module --with-openssl=/usr/local/openssl-1.0.2n/ \  
\--with-luajit-xcflags=-DLUAJIT_ENABLE_LUA52COMPAT \  
\--with-http_gunzip_module && \  
gmake && \  
gmake install && \  
mkdir -p /data0/logs/  
  
COPY ./nginx/conf /opt/openresty/nginx/conf  
COPY ./nginx/src /opt/openresty/nginx/src  
COPY ./nginx/html /opt/openresty/nginx/html  
COPY ./boot /opt/openresty/boot  
  
RUN chmod +x /opt/openresty/boot  
  
EXPOSE 80 443  
ENV TZ "Asia/Shanghai"  
WORKDIR /opt/openresty  
  
CMD ["./boot"]  

