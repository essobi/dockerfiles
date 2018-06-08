FROM debian:jessie  
  
MAINTAINER Michael Mauracher "michael@websr.eu"  
LABEL Description="This image is used to start a nginx-lb" Vendor="Soop"
Version="1.0"  
  
ENV NGINX_VERSION 1.10.1-1~jessie  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 /usr/local/bin/confd  
ADD create-config /usr/local/bin/create-config  
ADD confd-watch /usr/local/bin/confd-watch  
RUN chmod +x /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd-watch  
RUN chmod +x /usr/local/bin/create-config  
RUN rm -rf /etc/nginx/sites-enabled  
RUN mkdir /etc/nginx/sites-enabled  
RUN mkdir -p /etc/confd/conf.d  
RUN mkdir -p /etc/confd/templates  
  
EXPOSE 80 443  
CMD /usr/local/bin/confd-watch  

