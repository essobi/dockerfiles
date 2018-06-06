FROM nginx  
  
MAINTAINER "Kota Matsumoto" <kota1861@gmail.com>  
  
  
COPY config/nginx_run.sh /run/nginx_run.sh  
RUN chmod +x /run/nginx_run.sh  
COPY config/nginx.conf /etc/nginx/nginx.conf  
COPY config/laravel.conf /etc/nginx/conf.d/laravel.conf  
RUN rm /etc/nginx/conf.d/default.conf  
  
RUN mkdir -p /data  
VOLUME ["/data"]  
  
#CMD ["/run/nginx_run.sh"]  

