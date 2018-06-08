FROM ubuntu:trusty  
  
MAINTAINER Christoph (Sheogorath) Kern <sheogorath@shivering-isles.com>  
  
# Version  
#ENV NGINX_VERSION 1.11.9  
ENV NGINX_VERSION 1.10.2  
ENV NPS_VERSION 1.11.33.4  
  
# Setup Environment  
ENV MODULE_DIR /usr/src/nginx-modules  
ENV NGINX_TEMPLATE_DIR /usr/src/nginx  
ENV NGINX_RUNTIME_DIR /usr/src/runtime  
# Set some required defaults  
ENV NPSC_FILE_CACHE_PATH=/var/cache/ngx_pagespeed  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Build Tools & Dependence  
RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty main restricted" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-updates main
restricted" >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install wget -y && \  
apt-get build-dep nginx -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
# Create Module Directory  
mkdir ${MODULE_DIR} && \  
# Download Source  
cd /usr/src && \  
wget -q http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar xzf nginx-${NGINX_VERSION}.tar.gz && \  
rm -rf nginx-${NGINX_VERSION}.tar.gz && \  
# Download pagespeed ressources  
cd ${MODULE_DIR} && \  
wget -q
https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}-beta.tar.gz
&& \  
tar zxf release-${NPS_VERSION}-beta.tar.gz && \  
rm -rf release-${NPS_VERSION}-beta.tar.gz && \  
cd ngx_pagespeed-release-${NPS_VERSION}-beta/ && \  
wget -q https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz && \  
tar zxf ${NPS_VERSION}.tar.gz && \  
rm -rf ${NPS_VERSION}.tar.gz && \  
# Compile Nginx  
cd /usr/src/nginx-${NGINX_VERSION} && \  
./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--with-http_realip_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_secure_link_module \  
\--with-http_v2_module \  
#--with-threads \  
\--with-file-aio \  
\--with-ipv6 \  
\--add-module=${MODULE_DIR}/ngx_pagespeed-release-${NPS_VERSION}-beta \  
# Build nginx  
&& cd /usr/src/nginx-${NGINX_VERSION} \  
&& make -j`nproc` && make install \  
&& mkdir -p /var/cache/nginx \  
&& mkdir -p $NPSC_FILE_CACHE_PATH \  
# remove sources  
&& rm -rf /usr/src/*  
  
# Forward requests and errors to docker logs  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
# Provide config and entrypoint  
COPY conf/*.conf /etc/nginx/  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 80  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  
  

