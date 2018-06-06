FROM busybox  
  
ADD conf.d/ /etc/nginx/conf.d/  
ADD vhost.d/ /etc/nginx/vhost.d/  
ADD templates/ /etc/docker-gen/templates/  
ADD wwwroot/ /usr/share/nginx/html/  
  
VOLUME /etc/nginx/conf.d  
VOLUME /etc/nginx/vhost.d  
VOLUME /etc/docker-gen/templates  
VOLUME /usr/share/nginx/html  
  

