FROM ubuntu  
  
MAINTAINER LionHeart <LionHeart_fxc@163.com>  
  
ENV FASTDFS_PATH=/fastDFS \  
FASTDFS_BASE_PATH=/data \  
FASTDHT_BASE_PATH=/dht_data \  
NGINX_VERSION=1.8.1 \  
PCRE_VERSION=8.37 \  
ZLIB_VERSION=1.2.8 \  
OPENSSL_VERSION=1.0.2f \  
BERKELEY_DB_VERSION=6.1.26  
RUN apt-get update && apt-get install -y \  
build-essential \  
gcc \  
git \  
make \  
wget  
  
RUN mkdir -p ${FASTDFS_PATH}/libfastcommon \  
&& mkdir -p ${FASTDFS_PATH}/fastdfs \  
&& mkdir -p ${FASTDFS_PATH}/nginx \  
&& mkdir -p ${FASTDFS_PATH}/nginx_module \  
&& mkdir -p ${FASTDFS_PATH}/download \  
&& mkdir -p ${FASTDFS_BASE_PATH} \  
&& mkdir -p ${FASTDFS_PATH}/fastdht \  
&& mkdir ${FASTDHT_BASE_PATH} \  
&& ln -s ${FASTDFS_BASE_PATH} ${FASTDFS_BASE_PATH}/M00  
  
RUN git clone https://github.com/happyfish100/libfastcommon.git
${FASTDFS_PATH}/libfastcommon \  
&& git clone https://github.com/happyfish100/fastdfs.git
${FASTDFS_PATH}/fastdfs \  
&& git clone https://github.com/happyfish100/fastdfs-nginx-module.git
${FASTDFS_PATH}/nginx_module \  
&& git clone https://github.com/happyfish100/fastdht.git
${FASTDFS_PATH}/fastdht \  
&& wget "http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz" -P
${FASTDFS_PATH}/nginx \  
&& wget "http://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz" -P
${FASTDFS_PATH}/download \  
&& wget
"ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${PCRE_VERSION}.tar.gz"
-P ${FASTDFS_PATH}/download \  
&& wget "http://zlib.net/zlib-${ZLIB_VERSION}.tar.gz" -P
${FASTDFS_PATH}/download \  
&& wget "http://download.oracle.com/berkeley-
db/db-${BERKELEY_DB_VERSION}.tar.gz" -P ${FASTDFS_PATH}/download \  
&& tar zxvf /fastDFS/nginx/nginx-${NGINX_VERSION}.tar.gz -C /fastDFS/nginx \  
&& tar zxvf /fastDFS/download/openssl-${OPENSSL_VERSION}.tar.gz -C
/fastDFS/download \  
&& tar zxvf /fastDFS/download/pcre-${PCRE_VERSION}.tar.gz -C /fastDFS/download
\  
&& tar zxvf /fastDFS/download/zlib-${ZLIB_VERSION}.tar.gz -C /fastDFS/download
\  
&& tar zxvf /fastDFS/download/db-${BERKELEY_DB_VERSION}.tar.gz -C
/fastDFS/download  
  
WORKDIR ${FASTDFS_PATH}/libfastcommon  
  
RUN ["/bin/bash", "-c", "./make.sh && ./make.sh install"]  
  
WORKDIR ${FASTDFS_PATH}/fastdfs  
  
RUN ["/bin/bash", "-c", "./make.sh && ./make.sh install"]  
  
WORKDIR ${FASTDFS_PATH}/nginx/nginx-${NGINX_VERSION}  
  
RUN ./configure --with-pcre=${FASTDFS_PATH}/download/pcre-${PCRE_VERSION} \  
\--with-zlib=${FASTDFS_PATH}/download/zlib-${ZLIB_VERSION} \  
\--with-openssl=${FASTDFS_PATH}/download/openssl-${OPENSSL_VERSION} \  
\--with-http_ssl_module \  
\--add-module=${FASTDFS_PATH}/nginx_module/src \  
&& make \  
&& make install  
  
WORKDIR ${FASTDFS_PATH}/download/db-${BERKELEY_DB_VERSION}/build_unix  
  
RUN ../dist/configure --prefix=/usr \  
&& make \  
&& make install  
  
WORKDIR ${FASTDFS_PATH}/fastdht  
  
RUN ["/bin/bash", "-c", "./make.sh && ./make.sh install"]  
  
RUN rm -rf /var/lib/apt/lists/* \  
&& rm -rf /fastDFS/*  
  
EXPOSE 23000 11411 80

