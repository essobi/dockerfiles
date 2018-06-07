FROM buildpack-deps:jessie  
  
MAINTAINER EngageNExecute <code@engagenexecute.com>  
  
ENV NPS_VERSION 1.9.32.10  
ENV NGINX_VERSION 1.9.9  
  
  
# Install packages.  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
python-dev \  
build-essential \  
zlib1g-dev \  
libpcre3 \  
libpcre3-dev \  
unzip \  
wget  
  
RUN cd && \  
wget
https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}-beta.zip
&& \  
unzip release-${NPS_VERSION}-beta.zip && \  
cd ngx_pagespeed-release-${NPS_VERSION}-beta/ && \  
wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz && \  
tar -xzvf ${NPS_VERSION}.tar.gz  
  
RUN cd && \  
wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar -xvzf nginx-${NGINX_VERSION}.tar.gz && \  
cd nginx-${NGINX_VERSION}/ && \  
./configure --add-module=$HOME/ngx_pagespeed-release-${NPS_VERSION}-beta \  
\--user=www-data \  
\--group=www-data \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module && \  
make && \  
make install  
  
RUN mkdir -p /var/pagespeed/cache && \  
chown -R www-data:www-data /var/pagespeed/cache  

