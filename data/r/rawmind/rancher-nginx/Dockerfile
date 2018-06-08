FROM rawmind/rancher-base:0.0.2-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Install and configure kafka  
RUN apk add --update nginx && rm -rf /var/cache/apk/* \  
&& mkdir -p /tmp/nginx/client-body  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
COPY conf/favicon.ico /usr/share/nginx/html/  
COPY conf/favicon.ico /www/  
COPY conf/registry.conf /etc/nginx/conf.d/  
  
# Add monit conf for services  
ADD monit/*.conf /etc/monit/conf.d/  
  
# Add start  
ADD start.sh /usr/bin/  
ADD nginx.sh /usr/bin/  
RUN chmod +x /usr/bin/*.sh  
  
ENTRYPOINT ["/usr/bin/start.sh"]  

