FROM nginx:latest  
MAINTAINER Danny Dörfel <danny.dorfel@gmail.com>  
  
ENV PHP_FPM_SOCKET "php:9000"  
ENV SERVER_NAME project.dev  
ENV DOCUMENT_ROOT /var/www/app/web  
  
COPY nginx.conf /etc/nginx/  
COPY default.conf /etc/nginx/sites-available/  
  
RUN mkdir /etc/nginx/sites-enabled && \  
ln -sf /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf && \  
usermod -u 501 www-data && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
COPY run.sh run.sh  
  
RUN chmod +x run.sh  
  
CMD ["/run.sh"]  

