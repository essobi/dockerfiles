###  
# vkucukcakar/nginx  
# NGINX Docker image with automatic configuration file creation and export  
# Copyright (c) 2017 Volkan Kucukcakar  
#  
# This file is part of vkucukcakar/nginx.  
#  
# vkucukcakar/nginx is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 2 of the License, or  
# (at your option) any later version.  
#  
# vkucukcakar/nginx is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
# This copyright notice and license must be retained in all files and
derivative works.  
###  
FROM nginx:1.12.2-alpine  
  
LABEL maintainer "Volkan Kucukcakar"  
  
ENV NGINX_V 1.12.2  
ENV NAXSI_V 0.55.3  
EXPOSE 80 443  
VOLUME [ "/configurations" ]  
  
# Delete default nginx /conf.d/default.conf configuration file  
RUN rm /etc/nginx/conf.d/default.conf  
  
# Build dynamic modules for nginx  
RUN apk add --update \  
# Install build tools, wget and openssl (for Alpine)  
pcre-dev \  
build-base \  
openssl-dev \  
zlib-dev \  
wget \  
openssl \  
  
# Download nginx source to build dynamic modules  
&& wget --no-check-certificate
https://nginx.org/download/nginx-${NGINX_V}.tar.gz \  
&& tar -xzvf nginx-${NGINX_V}.tar.gz \  
  
# Download and build naxsi dynamic module for nginx  
# Note: \--with-compat here is required even on community version (tested on
1.11) as it seems to be fixing "nginx: [emerg] module
"/etc/nginx/modules/ngx_http_naxsi_module.so" is not binary compatible" error.  
&& wget --no-check-certificate https://github.com/nbs-
system/naxsi/archive/${NAXSI_V}.tar.gz \  
&& tar -xzvf ${NAXSI_V}.tar.gz \  
&& cd nginx-${NGINX_V} \  
&& ./configure --with-compat --add-dynamic-
module=../naxsi-${NAXSI_V}/naxsi_src \  
&& make modules \  
&& cp objs/ngx_http_naxsi_module.so /etc/nginx/modules/ \  
&& mkdir /etc/nginx/naxsi \  
&& cp -rf ../naxsi-${NAXSI_V}/naxsi_config/* /etc/nginx/naxsi/ \  
&& cd .. \  
&& rm -r ${NAXSI_V}.tar.gz naxsi-${NAXSI_V} \  
  
# Download and build other dynamic modules here...  
# Remove nginx source  
&& rm -r nginx-${NGINX_V} nginx-${NGINX_V}.tar.gz \  
  
# Download naxsi-rules, community provided rules for Wordpress, Drupal, etc...  
&& wget --no-check-certificate https://github.com/nbs-system/naxsi-
rules/archive/master.tar.gz \  
&& tar -xzvf master.tar.gz \  
&& mv -f naxsi-rules-master /etc/nginx/naxsi-rules \  
&& rm -r master.tar.gz \  
  
# Remove unnecessary packages  
&& apk del build-base wget \  
  
# Clean up the apk cache  
&& rm -rf /var/cache/apk/*  
  
# Note: gettext (for envsubst command) already installed on base image  
# Install bash (for basic level of shell compatibility) that will be required
by entrypoint later  
RUN apk add --update bash \  
&& rm -rf /var/cache/apk/*  
  
# Make ssl directory, common  
RUN mkdir /etc/nginx/ssl  
  
# Setup proxy cache directory  
RUN mkdir -p /data/nginx/cache \  
&& chown -R nginx:nginx /data/nginx \  
&& chmod -R 774 /data/nginx/cache  
  
# Setup server document root  
RUN mkdir -p /var/www/html  
  
# Disable default configuration files of the parent image  
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak  
#&& mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak; exit
0  
# Copy template configuration files  
COPY templates /templates  
  
# Setup entrypoint  
COPY common/entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
# Set CMD again, CMD is not inherited from parent if ENTRYPOINT is set  
CMD ["nginx", "-g", "daemon off;"]  
  

