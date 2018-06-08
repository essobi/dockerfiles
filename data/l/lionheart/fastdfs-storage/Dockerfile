FROM ubuntu  
  
#set the environment arguments  
ENV FASTDFS_PATH=/fastDFS \  
FASTDFS_BASE_PATH=/data \  
NGINX_VERSION=1.8.1 \  
PCRE_VERSION=8.37 \  
ZLIB_VERSION=1.2.8 \  
OPENSSL_VERSION=1.0.2g  
  
#get all the dependences except nginx's service  
RUN apt-get update && apt-get install -y \  
g++ \  
gcc \  
git \  
make \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
#create the dir  
RUN mkdir -p ${FASTDFS_PATH}/libfastcommon \  
&& mkdir -p ${FASTDFS_PATH}/fastdfs \  
&& mkdir -p ${FASTDFS_PATH}/nginx \  
&& mkdir -p ${FASTDFS_PATH}/download \  
&& mkdir -p ${FASTDFS_PATH}/download/nginx_module \  
&& mkdir ${FASTDFS_BASE_PATH}  
  
#compile the libfastcommon  
WORKDIR ${FASTDFS_PATH}/libfastcommon  
  
RUN git clone https://github.com/happyfish100/libfastcommon.git
${FASTDFS_PATH}/libfastcommon \  
&& ./make.sh \  
&& ./make.sh install \  
&& rm -rf ${FASTDFS_PATH}/libfastcommon  
  
#compile the fastdfs  
WORKDIR ${FASTDFS_PATH}/fastdfs  
  
RUN git clone https://github.com/happyfish100/fastdfs.git
${FASTDFS_PATH}/fastdfs \  
&& ./make.sh \  
&& ./make.sh install \  
&& rm -rf ${FASTDFS_PATH}/fastdfs  
  
#compile the nginx  
WORKDIR ${FASTDFS_PATH}/nginx/nginx-${NGINX_VERSION}  
  
RUN git clone https://github.com/happyfish100/fastdfs-nginx-module.git
${FASTDFS_PATH}/download/nginx_module \  
&& wget "http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz" -P
${FASTDFS_PATH}/nginx \  
&& wget "http://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz" -P
${FASTDFS_PATH}/download \  
&& wget
"ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${PCRE_VERSION}.tar.gz"
-P ${FASTDFS_PATH}/download \  
&& wget "http://zlib.net/zlib-${ZLIB_VERSION}.tar.gz" -P
${FASTDFS_PATH}/download \  
&& tar zxvf ${FASTDFS_PATH}/nginx/nginx-${NGINX_VERSION}.tar.gz -C
${FASTDFS_PATH}/nginx \  
&& tar zxvf ${FASTDFS_PATH}/download/openssl-${OPENSSL_VERSION}.tar.gz -C
${FASTDFS_PATH}/download \  
&& tar zxvf ${FASTDFS_PATH}/download/pcre-${PCRE_VERSION}.tar.gz -C
${FASTDFS_PATH}/download \  
&& tar zxvf ${FASTDFS_PATH}/download/zlib-${ZLIB_VERSION}.tar.gz -C
${FASTDFS_PATH}/download \  
&& ./configure --with-pcre=${FASTDFS_PATH}/download/pcre-${PCRE_VERSION} \  
\--with-zlib=${FASTDFS_PATH}/download/zlib-${ZLIB_VERSION} \  
\--with-openssl=${FASTDFS_PATH}/download/openssl-${OPENSSL_VERSION} \  
\--with-http_ssl_module \  
\--add-module=${FASTDFS_PATH}/download/nginx_module/src \  
&& make \  
&& make install \  
&& rm -rf ${FASTDFS_PATH}  
  
EXPOSE 23000 80  
ADD start.sh /usr/bin/  
  
#make the start.sh executable  
RUN chmod 777 /usr/bin/start.sh  
  
ENTRYPOINT ["/usr/bin/start.sh"]  
  
MAINTAINER LionHeart <LionHeart_fxc@163.com>  

