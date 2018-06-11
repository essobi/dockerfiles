FROM buildpack-deps:stretch  
  
# Versions of Nginx and nginx-rtmp-module to use  
ENV DEBIAN_FRONTEND=noninteractive  
ENV NGINX_VERSION nginx-1.12.2  
ENV NGINX_RTMP_MODULE_VERSION 1.2.1  
ENV NGINX_FANCYINDEX_MODULE_VERSION 0.4.2  
ENV PCRE_VERSION 8.40  
ENV ZLIB_VERSION 1.2.11  
ENV OPENSSL_VERSION 1.1.0g  
ENV GO_HEALTH_CHECK_VERSION 1.1  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y ca-certificates openssl libssl-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Download and decompress Nginx  
RUN mkdir -p /tmp/build/nginx && \  
cd /tmp/build/nginx && \  
wget -O ${NGINX_VERSION}.tar.gz
https://nginx.org/download/${NGINX_VERSION}.tar.gz && \  
tar -zxf ${NGINX_VERSION}.tar.gz  
  
# Download and decompress RTMP module  
RUN mkdir -p /tmp/build/nginx-rtmp-module && \  
cd /tmp/build/nginx-rtmp-module && \  
wget -O nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}.tar.gz
https://github.com/arut/nginx-rtmp-
module/archive/v${NGINX_RTMP_MODULE_VERSION}.tar.gz && \  
tar -zxf nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}.tar.gz && \  
cd nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}  
  
# Download and decompress FancyIndex module  
RUN mkdir -p /tmp/build/nginx-fancyindex-module && \  
cd /tmp/build/nginx-fancyindex-module && \  
wget -O ngx-fancyindex-${NGINX_FANCYINDEX_MODULE_VERSION}.tar.gz
https://github.com/aperezdc/ngx-
fancyindex/archive/v${NGINX_FANCYINDEX_MODULE_VERSION}.tar.gz && \  
tar -xzf ngx-fancyindex-${NGINX_FANCYINDEX_MODULE_VERSION}.tar.gz && \  
cd ngx-fancyindex-${NGINX_FANCYINDEX_MODULE_VERSION}  
  
# Download and decompress PCRE lib  
RUN mkdir -p /tmp/build/pcre/ && \  
cd /tmp/build/pcre &&\  
wget -O pcre-${PCRE_VERSION}.tar.gz
https://ftp.pcre.org/pub/pcre/pcre-${PCRE_VERSION}.tar.gz && \  
tar -xzf pcre-${PCRE_VERSION}.tar.gz && \  
cd pcre-${PCRE_VERSION}  
  
# Download and decompress zlib  
RUN mkdir -p /tmp/build/zlib/ && \  
cd /tmp/build/zlib &&\  
wget -O zlib-${ZLIB_VERSION}.tar.gz
http://www.zlib.net/zlib-${ZLIB_VERSION}.tar.gz && \  
tar -xzf zlib-${ZLIB_VERSION}.tar.gz && \  
cd zlib-${ZLIB_VERSION}  
  
# Download and decompress OpenSSL lib  
RUN mkdir -p /tmp/build/openssl/ && \  
cd /tmp/build/openssl &&\  
wget -O openssl-${OPENSSL_VERSION}.tar.gz
https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz && \  
tar -xzf openssl-${OPENSSL_VERSION}.tar.gz && \  
cd openssl-${OPENSSL_VERSION}  
  
# Download and decompress go-health-check  
RUN mkdir -p /tmp/build/go-health-check/ && \  
cd /tmp/build/go-health-check &&\  
wget -O go-health-check_${GO_HEALTH_CHECK_VERSION}_linux_amd64.tar.gz
https://github.com/UnAfraid/go-health-
check/releases/download/v${GO_HEALTH_CHECK_VERSION}/go-health-
check_${GO_HEALTH_CHECK_VERSION}_linux_amd64.tar.gz && \  
tar -xzf go-health-check_${GO_HEALTH_CHECK_VERSION}_linux_amd64.tar.gz  
  
# Build and install Nginx  
# The default puts everything under /usr/local/nginx, so it's needed to change  
# it explicitly. Not just for order but to have it in the PATH  
RUN cd /tmp/build/nginx/${NGINX_VERSION} && \  
./configure \  
\--prefix=/usr/share/nginx \  
\--sbin-path=/usr/local/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/run/nginx.pid \  
\--lock-path=/var/lock/nginx.lock \  
\--with-openssl=/tmp/build/openssl/openssl-${OPENSSL_VERSION} \  
\--with-openssl-opt=enable-ec_nistp_64_gcc_128 \  
\--with-openssl-opt=no-nextprotoneg \  
\--with-openssl-opt=no-weak-ssl-ciphers \  
\--with-openssl-opt=no-ssl3 \  
\--with-pcre=/tmp/build/pcre/pcre-${PCRE_VERSION} \  
\--with-pcre-jit \  
\--with-zlib=/tmp/build/zlib/zlib-${ZLIB_VERSION} \  
\--with-compat \  
\--with-file-aio \  
\--with-threads \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_sub_module \  
\--with-http_stub_status_module \  
\--with-http_v2_module \  
\--with-http_secure_link_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-stream \  
\--with-stream_realip_module \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--add-module=/tmp/build/nginx-rtmp-module/nginx-rtmp-
module-${NGINX_RTMP_MODULE_VERSION} \  
\--add-module=/tmp/build/nginx-fancyindex-module/ngx-
fancyindex-${NGINX_FANCYINDEX_MODULE_VERSION} && \  
make -j $(getconf _NPROCESSORS_ONLN) && \  
make install && \  
mkdir /var/lock/nginx ls && \  
mv /tmp/build/go-health-check/go-health-check /usr/local/bin/go-health-check
&& \  
rm -rf /tmp/build  
  
# Forward logs to Docker  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Set up config file  
COPY nginx/conf/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/conf/default.conf /etc/nginx/sites-enabled/default.conf  
  
# Create directories  
RUN mkdir -p /var/www/rtmp && \  
mkdir -p /var/www/rtmp/hls && \  
mkdir -p /var/www/rtmp/streaming  
  
# Copy assets  
COPY nginx/web/stat.xsl /var/www/rtmp/stat.xsl  
COPY nginx/web/index.html /var/www/rtmp/index.html  
COPY nginx/web/dash.html /var/www/rtmp/dash.html  
COPY nginx/web/hls.html /var/www/rtmp/hls.html  
COPY nginx/web/js /var/www/rtmp/js  
COPY nginx/web/css /var/www/rtmp/css  
COPY nginx/bin/entry-point.sh /usr/local/bin/entry-point.sh  
RUN chown -R www-data: /var/www/  
  
# Setup default working directory  
WORKDIR /etc/nginx  
  
# Run Nginx  
CMD ["/usr/local/bin/entry-point.sh"]  
  
# Expose ports  
EXPOSE 80  
EXPOSE 1935  

