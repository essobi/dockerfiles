FROM java:8-jre  
  
# install plugin dependencies  
ENV NGINX_VERSION 1.11.0-1~jessie  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt=${NGINX_VERSION} \  
nginx-module-geoip=${NGINX_VERSION} \  
nginx-module-image-filter=${NGINX_VERSION} \  
gettext-base \  
apache2-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY opt/ /opt/  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

