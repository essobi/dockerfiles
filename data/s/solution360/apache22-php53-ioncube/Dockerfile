FROM ubuntu:12.04  
# install wget, curl, unzip, apache2 and old php  
RUN apt-get update && \  
apt-get install -y \  
wget \  
curl \  
unzip \  
apache2 \  
php5 \  
php5-cli \  
libapache2-mod-php5 \  
php5-gd \  
php5-ldap \  
php5-mysql \  
php5-pgsql \  
php5-curl \  
php5-xdebug  
  
#configure php execution time, memory limit and upload size  
RUN ["bin/bash", "-c", "sed -i
's/max_execution_time\\\s*=.*/max_execution_time=180/g'
/etc/php5/apache2/php.ini"]  
RUN ["bin/bash", "-c", "sed -i
's/upload_max_filesize\\\s*=.*/upload_max_filesize=2G/g'
/etc/php5/apache2/php.ini"]  
RUN ["bin/bash", "-c", "sed -i 's/memory_limit\\\s*=.*/memory_limit=512M/g'
/etc/php5/apache2/php.ini"]  
  
RUN echo always_populate_raw_post_data=-1 >> /etc/php5/apache2/php.ini  
  
#set timezone  
RUN apt-get -y install tzdata && ln -sf /usr/share/zoneinfo/Europe/Berlin
/etc/localtime  
  
#configure apache vhost default  
RUN ["bin/bash", "-c", "sed -i 's/AllowOverride None/AllowOverride
All\\\nSetEnvIf X-Forwarded-Proto https HTTPS=on/g' /etc/apache2/sites-
available/default"]  
  
# Override Default web root  
RUN ["bin/bash", "-c", "sed -i 's/DocumentRoot \\\/var\\\/www/DocumentRoot
\\\/var\\\/www\\\/html/g' /etc/apache2/sites-available/default"]  
RUN ["bin/bash", "-c", "sed -i 's/Directory \\\/var\\\/www/Directory
\\\/var\\\/www\\\/html/g' /etc/apache2/sites-available/default"]  
RUN ["bin/bash", "-c", "sed -i 's/DocumentRoot \\\/var\\\/www/DocumentRoot
\\\/var\\\/www\\\/html/g' /etc/apache2/sites-available/default-ssl"]  
RUN ["bin/bash", "-c", "sed -i 's/Directory \\\/var\\\/www/Directory
\\\/var\\\/www\\\/html/g' /etc/apache2/sites-available/default-ssl"]  
  
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
RUN echo zend_extension = /usr/lib/php5/2*/ioncube_loader_lin_5.3.so >
/etc/php5/apache2/conf.d/00-ioncube.ini  
RUN service apache2 restart  
  
# Configure apache  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN a2enmod proxy  
RUN a2enmod headers  
RUN a2ensite default-ssl  
RUN chown -R www-data:www-data /var/www  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN service apache2 restart  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

