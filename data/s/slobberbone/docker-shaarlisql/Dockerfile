FROM debian:jessie  
  
ENV SERVER_NAME localhost  
RUN apt-get update \  
&& apt-get install -y curl unzip nginx-light php5-fpm php5-mysql php5-gd
supervisor \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY supervised.conf /etc/supervisor/conf.d/supervised.conf  
  
WORKDIR /var/www/html/  
RUN curl -L
http://git.gorgones.net/daniel.douat/shaarliSQL/repository/archive.zip >
archive.zip && unzip archive.zip \  
&& mv shaarliSQL-master* shaarli \  
&& chown -R www-data:www-data shaarli  
RUN sed -i "s/$cookiedir,$_SERVER[\'HTTP_HOST\']/$cookiedir,$SERVER_NAME/g"
shaarli/index.php  
RUN sed -i
"s/.$_SERVER[\'HTTP_HOST\'].$serverport/.$SERVER_NAME.$serverport/g"
shaarli/index.php  
  
VOLUME /var/www/html  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  

