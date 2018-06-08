FROM debian:jessie  
  
MAINTAINER Nitra  
  
ENV NGINX_VERSION=1.11.5  
ENV NPS_VERSION=1.11.33.4  
ENV OPENSSL_VERSION=1.0.2g  
ENV SUBSTITUTIONS_VERSION=0.6.4  
ENV SSL_ENABLED true  
# INSTALL DEPENDENCIES  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
automake \  
autoconf \  
libtool \  
openssl \  
zlib1g-dev \  
libpcre3 \  
libpcre3-dev \  
unzip \  
wget \  
git \  
curl  
  
# INSTALL OPENSSL  
RUN wget -qO -
https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \  
| tar xzf - -C /tmp  
# INSTALL PAGESPEED MODULE  
RUN cd /tmp \  
# && NPS_VERSION=1.11.33.2 \  
&& wget
https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}-beta.zip
-O release-${NPS_VERSION}-beta.zip \  
&& unzip release-${NPS_VERSION}-beta.zip \  
&& cd ngx_pagespeed-release-${NPS_VERSION}-beta \  
&& wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz \  
&& tar -xzvf ${NPS_VERSION}.tar.gz \  
&& wget -qO -
https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/v${SUBSTITUTIONS_VERSION}.tar.gz
\  
| tar zxf - -C /tmp \--owner root \--group root \--no-same-owner  
# INSTALL BROTLI  
RUN cd /tmp \  
&& git clone https://github.com/bagder/libbrotli \  
&& cd libbrotli \  
&& ./autogen.sh \  
&& ./configure \  
&& make && make install \  
&& cd /tmp \  
&& git clone https://github.com/google/ngx_brotli  
# INSTALL NGINX  
RUN mkdir -p /var/cache/nginx/client_temp \  
&& cd /tmp \  
&& wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar -xvzf nginx-${NGINX_VERSION}.tar.gz \  
&& cd nginx-${NGINX_VERSION} \  
&& ./configure \--add-module=/tmp/ngx_pagespeed-release-${NPS_VERSION}-beta \  
\--prefix=/usr/share/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/lock/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/access.log \  
\--user=www-data \  
\--group=www-data \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_auth_request_module \  
\--without-http_autoindex_module \  
\--without-http_ssi_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-ipv6 \  
\--with-cc-opt='-Wno-deprecated-declarations' \  
\--with-openssl=/tmp/openssl-${OPENSSL_VERSION} \  
\--add-
module=/tmp/ngx_http_substitutions_filter_module-${SUBSTITUTIONS_VERSION} \  
\--add-module=/tmp/ngx_brotli \  
&& make \  
&& make install  
  
# REMOVE UNUSED FILES  
RUN apt-get remove -y build-essential zlib1g-dev libpcre3-dev unzip \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/ngx_pagespeed-release-${NPS_VERSION}-beta \  
&& rm -rf /tmp/release-${NPS_VERSION}-beta.zip \  
&& rm -rf /tmp/nginx-${NGINX_VERSION}.tar.gz \  
&& rm -rf /tmp/nginx-${NGINX_VERSION} \  
&& rm -rf /tmp/ngx_brotli \  
&& rm -rf /tmp/ngx_http_substitutions_filter_module-${SUBSTITUTIONS_VERSION} \  
&& rm -rf /var/lib/apt/lists/* -vf  
  
# DOCKER LOG  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

