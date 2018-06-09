FROM ywfwj2008/php:7.1  
MAINTAINER ywfwj2008 <ywfwj2008@163.com>  
  
ENV WEBSERVER_INSTALL_DIR=/usr/local/tengine \  
TENGINE_VERSION=2.2.0 \  
PCRE_VERSION=8.39 \  
OPENSSL_VERSION=1.0.2j \  
RUN_USER=www \  
WWWROOT_DIR=/home/wwwroot \  
WWWLOGS_DIR=/home/wwwlogs \  
REMOTE_PATH=https://github.com/ywfwj2008/docker-php-nginx/raw/master  
  
WORKDIR /tmp  
  
# install tengine  
RUN wget -c --no-check-certificate
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${PCRE_VERSION}.tar.gz
&& \  
wget -c --no-check-certificate
https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz && \  
wget -c --no-check-certificate
https://github.com/alibaba/tengine/archive/tengine-${TENGINE_VERSION}.tar.gz
&& \  
tar xzf pcre-${PCRE_VERSION}.tar.gz && \  
tar xzf openssl-${OPENSSL_VERSION}.tar.gz && \  
tar xzf tengine-${TENGINE_VERSION}.tar.gz && \  
cd tengine-tengine-${TENGINE_VERSION} && \  
# Modify Tengine version  
#sed -i 's@TENGINE "/" TENGINE_VERSION@"nginx/unknown"@' src/core/nginx.h && \  
# close debug  
sed -i 's@CFLAGS="$CFLAGS -g"@#CFLAGS="$CFLAGS -g"@' auto/cc/gcc && \  
./configure \  
\--prefix=${WEBSERVER_INSTALL_DIR} \  
\--user=${RUN_USER} --group=${RUN_USER} \  
\--with-http_v2_module \  
\--with-http_ssl_module \  
\--with-ipv6 \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_concat_module=shared \  
\--with-http_sysguard_module=shared \  
\--with-openssl=/tmp/openssl-${OPENSSL_VERSION} \  
\--with-pcre=/tmp/pcre-${PCRE_VERSION} \  
\--with-pcre-jit \  
\--with-jemalloc && \  
make && make install && \  
mkdir -p ${WEBSERVER_INSTALL_DIR}/conf/rewrite && \  
touch ${WEBSERVER_INSTALL_DIR}/conf/rewrite/none.conf && \  
rm -rf /tmp/*  
  
ADD ${REMOTE_PATH}/nginx.conf ${WEBSERVER_INSTALL_DIR}/conf/nginx.conf  
ADD ${REMOTE_PATH}/nginx-init /etc/init.d/nginx  
RUN sed -i "s@worker_connections 51200;@worker_connections 51200;\n reuse_port
on;@" ${WEBSERVER_INSTALL_DIR}/conf/nginx.conf && \  
sed -i "s@^worker_processes.*@worker_processes auto;\nworker_cpu_affinity
auto;\ndso {\n\tload ngx_http_concat_module.so;\n\tload
ngx_http_sysguard_module.so;\n}@" ${WEBSERVER_INSTALL_DIR}/conf/nginx.conf  
  
# run install script  
ADD ${REMOTE_PATH}/install.sh /tmp/install.sh  
RUN chmod 777 install.sh && \  
bash install.sh && \  
rm -rf /tmp/*  
  
# ending  
WORKDIR ${WWWROOT_DIR}  
RUN mkdir -p ${WWWLOGS_DIR} && \  
mkdir -p ${WWWROOT_DIR}/default && \  
echo "Hello World!" > /${WWWROOT_DIR}/default/index.html && \  
echo "<?php phpinfo();" > /${WWWROOT_DIR}/default/phpinfo.php  
  
# expose port  
EXPOSE 80 443  
# Set the entrypoint script.  
ADD ${REMOTE_PATH}/entrypoint.sh /entrypoint.sh  
RUN chmod 777 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Define the default command.  
CMD ["nginx", "-g", "daemon off;"]  

