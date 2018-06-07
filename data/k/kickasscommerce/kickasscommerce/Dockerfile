FROM nginx:1.9  
MAINTAINER Adam Paterson <hello@adampaterson.co.uk>  
  
ADD etc/vhost.conf /etc/nginx/conf.d/default.conf  
ADD bin/* /usr/local/bin/  
  
ENV FPM_HOST fpm  
ENV FPM_PORT 9000  
ENV APP_ROOT /var/www/kickass  
  
ENTRYPOINT ["/usr/local/bin/docker-environment"]  
CMD ["nginx", "-g", "daemon off;"]

