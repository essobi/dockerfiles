FROM kmelkez/php-base:latest  
MAINTAINER Matthieu Keromen <sharoomsorg@gmail.com>  
ENV REFRESHED_AT 2015-05-21  
RUN apt-get update && apt-get install -y \  
php5-fpm \  
php5-mysqlnd \  
php5-intl \  
locales && \  
rm -rf /var/lib/apt/lists/*  
  
ENV UPLOAD_MAX_FILESIZE 5M  
ENV POST_MAX_SIZE 10M  
  
RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
&& \  
sed -e 's/;listen\\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf && \  
sed -e 's/;listen\\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf && \  
sed -e 's/listen = .*/listen = 9000/' -i /etc/php5/fpm/pool.d/www.conf && \  
sed -e 's/upload_max_filesize\s*=\s*2M/upload_max_filesize =
'"$UPLOAD_MAX_FILESIZE"'/' -i /etc/php5/fpm/php.ini && \  
sed -e 's/post_max_size\s*=\s*8M/post_max_size = '"$POST_MAX_SIZE"'/' -i
/etc/php5/fpm/php.ini && \  
echo "date.timezone = $TIMEZONE;" >> /etc/php5/fpm/php.ini  
  
EXPOSE 9000  
ENTRYPOINT ["/usr/sbin/php5-fpm"]  

