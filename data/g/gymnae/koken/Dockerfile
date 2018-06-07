FROM gymnae/webserverbase:latest  
  
#install packages  
RUN apk-install \  
imagemagick \  
php7-json@community \  
php7-mysqli@community \  
php7-exif@community \  
php7-iconv@community \  
php7-bz2@community \  
php7-ctype@community \  
php7-posix@community \  
php7-xml@community \  
php7-zip@community \  
php7-opcache@community \  
libzip@community \  
ffmpeg  
  
# Data volumes  
VOLUME ["/media/koken"]  
  
# temp folders for webserver  
RUN mkdir -p /tmp/nginx/ && \  
chown nginx:www-data /tmp/nginx  
  
# nginx site conf  
COPY config/nginx.conf /etc/nginx/  
COPY config/default.conf /etc/nginx/sites-available/  
COPY config/php-fpm.conf /etc/php7/  
COPY config/interfaces /etc/network/  
  
EXPOSE 80 443  
# Prepare the script that starts it all  
ADD init.sh /  
RUN chmod +x /init.sh && chmod 777 /init.sh  
  
ENTRYPOINT ["/init.sh"]  

