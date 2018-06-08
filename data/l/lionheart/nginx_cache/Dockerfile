FROM ubuntu  
  
#set the environment arguments  
ENV NGINX_PATH=/nginx \  
NGINX_BASE_PATH=/data \  
NGINX_VERSION=1.8.1 \  
PCRE_VERSION=8.37 \  
ZLIB_VERSION=1.2.8 \  
OPENSSL_VERSION=1.0.2g \  
NGX_CACHE_PURGE=2.3  
#get all the dependences  
RUN apt-get update && apt-get install -y \  
g++ \  
gcc \  
make \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
#create the dir  
RUN mkdir -p ${NGINX_PATH}/nginx \  
&& mkdir -p ${NGINX_PATH}/download \  
&& mkdir ${NGINX_BASE_PATH}  
  
#compile the nginx  
WORKDIR ${NGINX_PATH}/nginx/nginx-${NGINX_VERSION}  
  
RUN wget "http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz" -P
${NGINX_PATH}/nginx \  
&& wget "http://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz" -P
${NGINX_PATH}/download \  
&& wget
"ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${PCRE_VERSION}.tar.gz"
-P ${NGINX_PATH}/download \  
&& wget "http://zlib.net/zlib-${ZLIB_VERSION}.tar.gz" -P
${NGINX_PATH}/download \  
&& wget
"http://labs.frickle.com/files/ngx_cache_purge-${NGX_CACHE_PURGE}.tar.gz" -P
${NGINX_PATH}/download \  
&& tar zxvf ${NGINX_PATH}/nginx/nginx-${NGINX_VERSION}.tar.gz -C
${NGINX_PATH}/nginx \  
&& tar zxvf ${NGINX_PATH}/download/openssl-${OPENSSL_VERSION}.tar.gz -C
${NGINX_PATH}/download \  
&& tar zxvf ${NGINX_PATH}/download/pcre-${PCRE_VERSION}.tar.gz -C
${NGINX_PATH}/download \  
&& tar zxvf ${NGINX_PATH}/download/zlib-${ZLIB_VERSION}.tar.gz -C
${NGINX_PATH}/download \  
&& tar zxvf ${NGINX_PATH}/download/ngx_cache_purge-${NGX_CACHE_PURGE}.tar.gz
-C ${NGINX_PATH}/download \  
&& ./configure --with-pcre=${NGINX_PATH}/download/pcre-${PCRE_VERSION} \  
\--with-zlib=${NGINX_PATH}/download/zlib-${ZLIB_VERSION} \  
\--with-openssl=${NGINX_PATH}/download/openssl-${OPENSSL_VERSION} \  
\--with-http_ssl_module \  
\--add-module=${NGINX_PATH}/download/ngx_cache_purge-${NGX_CACHE_PURGE} \  
&& make \  
&& make install \  
&& rm -rf ${NGINX_PATH}  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/nginx/sbin/nginx","-g","daemon off;"]  
  
MAINTAINER LionHeart <LionHeart_fxc@163.com>  

