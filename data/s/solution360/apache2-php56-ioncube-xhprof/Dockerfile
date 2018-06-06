FROM debian:8  
RUN apt-get update  
RUN apt-get install -y wget curl apache2 php5 php5-imagick php5-mcrypt
php5-curl php5-xsl php5-intl php5-gd php5-mysql php5-xdebug unzip  
  
# XHPROF  
RUN apt-get install -y php-pear  
RUN apt-get install -y php5-dev  
RUN apt-get install -y pkg-config  
RUN apt-get install -y mongodb  
RUN apt-get install -y git  
RUN service apache2 restart  
RUN php5enmod mcrypt  
  
RUN yes '' | pecl install xhprof-beta  
RUN echo extension=xhprof.so > /etc/php5/mods-available/xhprof.ini  
RUN php5enmod xhprof  
RUN service apache2 restart  
  
RUN yes '' | pecl install mongodb  
RUN echo extension=mongodb.so > /etc/php5/mods-available/mongodb.ini  
RUN php5enmod mongodb  
RUN service apache2 restart  
  
# XHGUI  
RUN mkdir -p /var/www/xhgui  
RUN chmod -R 777 /var/www/xhgui  
RUN git clone https://github.com/perftools/xhgui.git /var/www/xhgui  
RUN cd /var/www/xhgui && php install.php  
COPY xhgui.conf /etc/apache2/sites-available/xhgui.conf  
RUN a2ensite xhgui  
RUN service apache2 restart  
  
#configure php  
RUN ["bin/bash", "-c", "sed -i
's/max_execution_time\\\s*=.*/max_execution_time=180/g'
/etc/php5/apache2/php.ini"]  
RUN ["bin/bash", "-c", "sed -i
's/upload_max_filesize\\\s*=.*/upload_max_filesize=16M/g'
/etc/php5/apache2/php.ini"]  
RUN ["bin/bash", "-c", "sed -i 's/memory_limit\\\s*=.*/memory_limit=512M/g'
/etc/php5/apache2/php.ini"]  
  
# override xhprof only running 1% of the time  
RUN ["bin/bash", "-c", "sed -i 's/return rand(1, 100) === 42;/return true;/g'
/var/www/xhgui/config/config.default.php"]  
  
RUN echo "always_populate_raw_post_data=-1" >> /etc/php5/apache2/php.ini  
RUN echo "auto_prepend_file=/var/www/xhgui/external/header.php" >>
/etc/php5/apache2/php.ini  
  
#configure apache  
RUN ["bin/bash", "-c", "sed -i 's/AllowOverride None/AllowOverride
All\\\nSetEnvIf X-Forwarded-Proto https HTTPS=on/g'
/etc/apache2/apache2.conf"]  
  
#configure XDebug  
RUN echo [XDebug] >> /etc/php5/apache2/php.ini  
RUN echo xdebug.remote_enable=1 >> /etc/php5/apache2/php.ini  
RUN echo xdebug.remote_connect_back=1 >> /etc/php5/apache2/php.ini  
RUN echo xdebug.idekey=netbeans-xdebug >> /etc/php5/apache2/php.ini  
RUN echo xdebug.max_nesting_level=200 >> /etc/php5/apache2/php.ini  
  
#install ioncube  
RUN wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz  
RUN tar xvfz ioncube_loaders_lin_x86-64.tar.gz  
RUN cp ioncube/*.so /usr/lib/php5/2*/  
RUN echo zend_extension = /usr/lib/php5/2*/ioncube_loader_lin_5.6.so >
/etc/php5/apache2/conf.d/00-ioncube.ini  
# RUN service apache2 restart  
# Configure apache  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN a2enmod proxy  
RUN a2enmod headers  
# enable ssl on apache  
RUN a2ensite default-ssl  
RUN chown -R www-data:www-data /var/www  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN service apache2 restart  
RUN touch /var/log/mongodb.log  
RUN chmod 777 /var/log/mongodb.log  
RUN mkdir -p /data/db  
RUN chmod 777 /data/db  
RUN mongod --smallfiles --fork --logpath /var/log/mongodb.log  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 9090  
CMD service mongodb start && /usr/sbin/apache2ctl -D FOREGROUND  

