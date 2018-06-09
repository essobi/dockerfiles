FROM buildpack-deps:jessie  
  
MAINTAINER Thoufeeq <thoufeeq@humblepaper.com>  
  
ENV NPS_VERSION 1.10.33.6  
ENV NGINX_VERSION 1.8.1  
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
  
#RUN cd && echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN mkdir -p /var/pagespeed/cache && \  
chown -R www-data:www-data /var/pagespeed/cache  
  
COPY pagespeed.conf /etc/nginx/conf.d/pagespeed.conf  
  
# Configure Nginx and apply pagespeed  
RUN sed -i 's/^ server {/&\n include \/etc\/nginx\/conf.d\/pagespeed.conf;/g'
/etc/nginx/nginx.conf  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
#CMD ["nginx"]  
CMD ["nginx", "-g", "daemon off;"]  
  
EXPOSE 80  
EXPOSE 443  
#FROM google/debian:wheezy  
#MAINTAINER David Gageot <david@gageot.net>  
#  
#ENV DEBIAN_FRONTEND noninteractive  
#  
## From instructions here: https://github.com/pagespeed/ngx_pagespeed  
#  
## Install dependencies  
## Download ngx_pagespeed  
## Download nginx  
## Build nginx  
## Cleanup  
##  
#RUN apt-get update -qq \  
#&& apt-get install -yqq build-essential zlib1g-dev libpcre3 libpcre3-dev
openssl libssl-dev libperl-dev wget ca-certificates logrotate \  
#&& (wget -qO -
https://github.com/pagespeed/ngx_pagespeed/archive/v1.9.32.3-beta.tar.gz | tar
zxf - -C /tmp) \  
#&& (wget -qO - https://dl.google.com/dl/page-speed/psol/1.9.32.3.tar.gz | tar
zxf - -C /tmp/ngx_pagespeed-1.9.32.3-beta/) \  
#&& (wget -qO - http://nginx.org/download/nginx-1.7.11.tar.gz | tar zxf - -C
/tmp) \  
#&& cd /tmp/nginx-1.7.11 \  
#&& ./configure --prefix=/etc/nginx/ --sbin-path=/usr/sbin/nginx --add-
module=/tmp/ngx_pagespeed-1.9.32.3-beta --with-http_ssl_module --with-
http_spdy_module --with-http_stub_status_module \  
#&& make install \  
#&& rm -Rf /tmp/* \  
#&& apt-get purge -yqq wget build-essential \  
#&& apt-get autoremove -yqq \  
#&& apt-get clean  
#EXPOSE 80 443  
#  
#VOLUME ["/etc/nginx/sites-enabled"]  
#WORKDIR /etc/nginx/  
#ENTRYPOINT ["/usr/sbin/nginx"]  
#  
## Configure nginx  
#RUN mkdir /var/ngx_pagespeed_cache  
#RUN chmod 777 /var/ngx_pagespeed_cache  
#COPY nginx.conf /etc/nginx/conf/nginx.conf  
#COPY sites-enabled /etc/nginx/sites-enabled#  

