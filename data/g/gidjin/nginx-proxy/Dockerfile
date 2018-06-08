FROM gidjin/nginx:latest  
MAINTAINER John Gedeon <js1@gedeons.com>  
  
RUN ln -sf /dev/stdout /var/log/confd.log  
  
COPY nginx.toml /etc/confd/conf.d/  
COPY nginx.conf.tmpl /etc/confd/templates/  
COPY start-up.sh /usr/local/bin/start-up.sh  
RUN chmod 755 /usr/local/bin/start-up.sh  

