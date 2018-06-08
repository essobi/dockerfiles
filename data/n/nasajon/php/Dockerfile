FROM nasajon/php:7.1-fpm-dev  
MAINTAINER Nasajon Sistemas <devops@nasajon.com.br>  
  
RUN apk add -U file && rm -rf /var/cache/apk/*  
  
COPY conf/default.conf /etc/nginx/conf.d/  
CMD /entrypoint.sh  

