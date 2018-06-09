FROM ubuntu:xenial  
SHELL ["/bin/bash", "-c"]  
  
## Config  
ENV NGINX_VER=1.12  
  
## Set Versions  
ENV PACKAGES_BUILD="\  
ca-certificates \  
git-core \  
build-essential \  
zlib1g-dev \  
libpcre3 \  
libpcre3-dev \  
unzip \  
wget \  
libssl-dev \  
automake \  
autoconf \  
libtool \  
libgeoip-dev \  
libxml2-dev \  
libcurl4-openssl-dev \  
libyajl-dev \  
liblmdb-dev"  
ENV PACKAGES_REQUIRED="\  
libssl1.0.0 \  
libcurl3 \  
libgeoip1 \  
libyajl2 \  
liblmdb0 \  
pkg-config \  
libxml2"  
ENV NGINX_CONFIG="\  
\--prefix=/usr \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--lock-path=/var/lock/nginx.lock \  
\--pid-path=/run/nginx.pid \  
\--modules-path=/usr/lib/nginx/modules \  
\--http-client-body-temp-path=/var/lib/nginx/body \  
\--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \  
\--http-proxy-temp-path=/var/lib/nginx/proxy \  
\--http-scgi-temp-path=/var/lib/nginx/scgi \  
\--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \  
\--with-pcre-jit \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--with-http_v2_module \  
\--with-http_dav_module \  
\--with-http_slice_module \  
\--with-threads \  
\--with-http_gzip_static_module \  
\--without-http_split_clients_module \  
\--without-http_userid_module \  
\--add-module=modules/ngx_testcookie \  
\--add-module=modules/ngx_pagespeed \  
\--add-module=modules/ngx_modsecurity \  
\--user=www-data \  
\--group=www-data"  
  
RUN mkdir -p /docker/build  
WORKDIR /docker/build  
RUN apt-get update && apt-get -y install --no-install-recommends \  
$PACKAGES_BUILD \  
$PACKAGES_REQUIRED \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo "$!/bin/bash" > /docker/env \  
&& git clone https://github.com/SpiderLabs/ModSecurity \  
&& cd ModSecurity \  
&& git checkout v3/master \  
&& git submodule init \  
&& git submodule update \  
&& ./build.sh \  
&& ./configure --prefix=/usr \  
&& make -j$(nproc) \  
&& make install \  
&& cd /docker/build \  
&& wget http://nginx.org/download/nginx-$(wget -q -O -
http://nginx.org/download/ | sed -n
's/.*href="nginx-\([^"]*\)\.tar\.gz.*/\1/p' | sort -V | grep -i ${NGINX_VER}.
| tail -n1).tar.gz \  
&& tar xf nginx-*.tar.gz && rm nginx-*.tar.gz && mv nginx-* nginx \  
&& mkdir -p /docker/build/nginx/modules \  
&& cd /docker/build/nginx/modules \  
&& git clone https://github.com/kyprizel/testcookie-nginx-module.git
ngx_testcookie \  
&& git clone https://github.com/pagespeed/ngx_pagespeed.git \  
&& cd /docker/build/nginx/modules/ngx_pagespeed \  
&& echo "export PAGESPEED_VER=$(git tag -l --sort=-version:refname 'v*' | head
-n1 | cut -c 2- )" >> /docker/env \  
&& source /docker/env && git checkout v${PAGESPEED_VER} \  
&& source /docker/env && wget $(scripts/format_binary_url.sh PSOL_BINARY_URL)
\  
&& source /docker/env && tar -zxvf $(echo ${PAGESPEED_VER} | awk -f '-'
'{print $1}')*.tar.gz \  
&& cd /docker/build/nginx/modules \  
&& git clone https://github.com/SpiderLabs/ModSecurity-nginx.git
ngx_modsecurity \  
&& cd /docker/build/nginx \  
&& ./configure $NGINX_CONFIG \  
&& make -j$(nproc) \  
&& make install \  
&& mkdir -p /var/lib/nginx/body && chown -R www-data:www-data /var/lib/nginx \  
&& rm -r /docker/build \  
&& apt-get -y purge $PACKAGES_BUILD \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
## Reset workdir  
WORKDIR /srv  
  
## Expose ports  
EXPOSE 80 443  
  
## Set options  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  

