FROM ubuntu:xenial  
  
ENV NGINX_STICKY_MODULE_VER=08a395c66e42  
ENV STICKY_MODULE_FOLDER=nginx-goodies-nginx-sticky-module-ng-08a395c66e42  
ENV NGINX_VER=1.11.4  
ENV OPENSSL_VER=1_1_0b  
ENV ZLIB_VER=1.2.8  
ENV PATH=$PATH:/usr/local/nginx/sbin  
  
RUN apt-get update && \  
apt-get -y install wget gcc g++ make libpcre3-dev libgnutls-dev libssl-dev
libxslt1-dev libgd-dev libgeoip-dev libgoogle-perftools-dev libatomic-ops-dev
libperl-dev curl && \  
useradd -m \--uid 1000 nginx  
  
RUN cd /tmp && \  
wget http://nginx.org/download/nginx-${NGINX_VER}.tar.gz && \  
tar -xvf nginx-${NGINX_VER}.tar.gz && \  
wget http://zlib.net/zlib-${ZLIB_VER}.tar.gz && \  
tar -xvf zlib-${ZLIB_VER}.tar.gz && \  
wget https://github.com/openssl/openssl/archive/OpenSSL_${OPENSSL_VER}.tar.gz
&& \  
tar -xvf OpenSSL_${OPENSSL_VER}.tar.gz && \  
wget https://bitbucket.org/nginx-goodies/nginx-sticky-module-
ng/get/${NGINX_STICKY_MODULE_VER}.tar.gz && \  
tar -xvf ${NGINX_STICKY_MODULE_VER}.tar.gz && \  
cd nginx-${NGINX_VER} && \  
./configure \--conf-path=/etc/nginx/nginx.conf \--with-select_module \--with-
poll_module \--with-threads \--with-file-aio \--with-ipv6 \--with-
http_ssl_module \--with-http_v2_module \--with-http_realip_module \--with-
http_addition_module \--with-http_xslt_module \--with-http_image_filter_module
\--with-http_geoip_module \--with-http_sub_module \--with-http_dav_module
\--with-http_flv_module \--with-http_mp4_module \--with-http_gunzip_module
\--with-http_gzip_static_module \--with-http_auth_request_module \--with-
http_random_index_module \--with-http_secure_link_module \--with-
http_degradation_module \--with-http_slice_module \--with-
http_stub_status_module \--with-http_perl_module \--with-stream \--with-
stream_ssl_module \--with-stream_realip_module \--with-stream_geoip_module
\--with-google_perftools_module \--with-cpp_test_module \--with-libatomic
\--with-pcre \--with-pcre-jit \--with-mail \--with-mail_ssl_module \--with-
zlib=../zlib-${ZLIB_VER} \--with-openssl=../openssl-OpenSSL_${OPENSSL_VER}
\--add-module=../${STICKY_MODULE_FOLDER} && \  
make -j 8 && \  
make install  
  
RUN ln -sf /dev/stdout /usr/local/nginx/logs/access.log && \  
ln -sf /dev/stderr /usr/local/nginx/logs/error.log  
  
COPY nginx.conf /usr/local/nginx/conf/nginx.conf  
  
CMD ["nginx", "-g", "daemon off;"]  

