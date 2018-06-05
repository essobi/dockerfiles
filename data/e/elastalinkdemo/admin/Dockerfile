FROM ubuntu:16.10  
RUN apt-get update \  
&& apt-get install -y php7.0-xml nginx php7.0-fpm php7.0-mysql supervisor php-
mongodb composer nginx-extras \  
&& apt-get clean \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir /run/php  
  
COPY ./nginx /etc/nginx  
COPY ./supervisord.conf /supervisord.conf  
WORKDIR /app  
VOLUME /app/wp-content/uploads  
  
EXPOSE 80  
CMD ["supervisord", "-c", "/supervisord.conf"]  

