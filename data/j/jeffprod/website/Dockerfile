FROM debian  
  
MAINTAINER Jean-François GAZET <ceo@jeffprod.com>  
  
LABEL version="1"  
LABEL description="WebApp Apache 2 / PHP / MySQL"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get install -y \  
supervisor \  
apache2 \  
mysql-server \  
php5 \  
libapache2-mod-php5 \  
php5-mysql \  
nano  
  
# for nano  
ENV TERM xterm  
  
# Apache  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
RUN rm /var/www/html/index.html  
COPY ["www","/var/www/html"]  
RUN chgrp -R www-data /var/www  
RUN find /var/www -type d -exec chmod 775 {} +  
RUN find /var/www -type f -exec chmod 664 {} +  
  
# PHP  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/apache2/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/apache2/php.ini  
  
# MySQL  
# to open MySQL server out of localhost : RUN sed -i -e "s/^bind-
address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf  
COPY ["database.sql","/tmp/database.sql"]  
COPY ["mysql.sh","/tmp/mysql.sh"]  
RUN chmod +x /tmp/mysql.sh  
RUN /tmp/mysql.sh  
RUN rm /tmp/mysql.sh  
RUN rm /tmp/database.sql  
  
# ports  
EXPOSE 80  
# EXPOSE 80 3306 (to open MySQL server out of localhost)  
# Start services when Docker image runs  
COPY ["supervisord.conf","/etc/supervisor/conf.d/supervisord.conf"]  
CMD ["/usr/bin/supervisord"]  

