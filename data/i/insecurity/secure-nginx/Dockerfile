FROM insecurity/debian:jessie  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
  
# Set variables (Choose version in:
http://nginx.org/packages/debian/pool/nginx/n/nginx/)  
ARG VERSION=1.14.0-1  
ARG NGINX_VERSION=$VERSION~jessie  
  
# Install packages  
#RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
RUN curl -O https://nginx.org/keys/nginx_signing.key && apt-key add
./nginx_signing.key && rm ./nginx_signing.key \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt=${NGINX_VERSION} \  
nginx-module-geoip=${NGINX_VERSION} \  
nginx-module-image-filter=${NGINX_VERSION} \  
nginx-module-perl=${NGINX_VERSION} \  
# nginx-module-njs=${NGINX_VERSION} \  
gettext-base \  
  
# Security \- Fix UID/GID of nginx user \  
&& usermod -u 3005 nginx \  
&& groupmod -g 3005 nginx \  
&& chown -R nginx:nginx /etc/nginx/ \  
&& chown -R nginx:nginx /var/cache/nginx/ \  
&& chown -R nginx:nginx /var/log/nginx/ \  
&& chmod -R 777 /var/log/nginx/ \  
  
# Security \- Edit default configuration file for non-root usage  
&& sed -i -e "s#\\(listen.*80\\)#listen 8080#" /etc/nginx/conf.d/default.conf
\  
&& sed -i -e "s#\\(/var/run\\)#/etc/nginx#" /etc/nginx/nginx.conf \  
  
# Persistence - Save a copy of default configuration/www files \  
&& mkdir -p /usr/local/bak/etc/ && mkdir -p /usr/local/bak/usr/ \  
&& cp -r /etc/nginx/ /usr/local/bak/etc/ \  
&& cp -r /usr/share/nginx/ /usr/local/bak/usr/nginx/ \  
&& chown -R nginx:nginx /usr/local/bak/ \  
  
# Persistence \- Add run script \  
&& echo '#!/bin/bash' > /run.sh \  
&& echo 'echo "Create configuration and content dir if missing in volumes..."'
>> /run.sh \  
&& echo 'cp -rn /usr/local/bak/etc/nginx/ /etc/' >> /run.sh \  
&& echo 'cp -rn /usr/local/bak/usr/nginx/ /usr/share/' >> /run.sh \  
&& echo 'echo "Reset permissions..."' >> /run.sh \  
&& echo 'chown -R nginx:nginx /var/cache/nginx/' >> /run.sh \  
&& echo 'exec /usr/sbin/nginx & tail -F /var/log/nginx/*' >> /run.sh \  
&& chmod 755 /run.sh \  
  
# Forward request and error logs to docker log collector \  
# && ln -sf /dev/stdout /var/log/nginx/access.log \  
# && ln -sf /dev/stderr /var/log/nginx/error.log \  
  
# APT Clean-up \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set listening ports inside container  
EXPOSE 8080 8443  
  
# Let's go !  
CMD ["/run.sh"]  
#CMD ["nginx", "-g", "daemon off;"]  

