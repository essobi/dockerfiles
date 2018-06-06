FROM damienlagae/debian-base  
MAINTAINER Damien Lagae <damien@lagae.info>  
  
# Set the nviroment variable for setting the Username and Password of MySQL  
ENV MYSQL_USER root  
ENV MYSQL_PASS toor  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /etc/apache2  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_RUN_USER www-data  
  
# Install required packages & cleanup  
RUN apt-get clean all && \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install mysql-server apache2 php5 libapache2-mod-php5 php5-mysql
php5-ldap php5-gd php-pear php-apc php5-curl php5-xdebug ruby ruby-dev
libsqlite3-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install mailcatcher  
RUN gem install mailcatcher --no-rdoc --no-ri  
  
# Install Adminer & Composer  
RUN mkdir -p /opt/adminer/ && \  
wget http://www.adminer.org/latest.php -O /opt/adminer/index.php && \  
chown www-data:www-data -R /opt/adminer && \  
curl -sS https://getcomposer.org/installer | php && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer  
  
ENV COMPOSER_HOME /opt/composer  
  
# Add shell scripts for starting mailcatcher  
ADD shell/mailcatcher-start.sh /mailcatcher-start.sh  
  
# Add shell scripts for starting apache2  
ADD shell/apache2-start.sh /apache2-start.sh  
  
# Add shell scripts for starting mysql  
ADD shell/mysql-start.sh /mysql-start.sh  
ADD shell/run.sh /run.sh  
  
# Add MySQL utils  
ADD shell/mysql_user.sh /mysql_user.sh  
  
# Give the execution permissions  
RUN chmod 755 /*.sh  
  
# Add the Configurations files  
ADD conf/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
ADD conf/my.cnf /etc/mysql/conf.d/my.cnf  
ADD conf/lamp.conf /etc/supervisor/conf.d/lamp.conf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Enable apache mods.  
RUN a2enmod php5 && \  
a2enmod rewrite  
  
# Setup PHP timezone  
# Setup PHP to use mailcatcher to send mails  
# Setup PHP to display all errors  
# Setup PHP: Increase size file  
# Configure Xdebug  
RUN echo "date.timezone=Europe/Brussels" >
/etc/php5/apache2/conf.d/01-timezone.ini && \  
echo "date.timezone=Europe/Brussels" > /etc/php5/cli/conf.d/01-timezone.ini &&
\  
sed -i -e "s/.*sendmail_path =.*/sendmail_path = \/usr\/bin\/env
\/usr\/local\/bin\/catchmail/" /etc/php5/apache2/php.ini && \  
sed -i -e "s/.*sendmail_path =.*/sendmail_path = \/usr\/bin\/env catchmail/"
/etc/php5/cli/php.ini && \  
echo "error_reporting = E_ALL\ndisplay_startup_errors = 1\ndisplay_errors = 1"
> /etc/php5/apache2/conf.d/01-errors.ini && \  
echo "error_reporting = E_ALL\ndisplay_startup_errors = 1\ndisplay_errors = 1"
> /etc/php5/cli/conf.d/01-errors.ini && \  
sed -i "s/upload_max_filesize = .*/upload_max_filesize = 20M/g"
/etc/php5/apache2/php.ini && \  
sed -i "s/post_max_size = .*/post_max_size = 80M/g" /etc/php5/apache2/php.ini
&& \  
echo "xdebug.default_enable=1" >> /etc/php5/apache2/conf.d/20-xdebug.ini &&\  
echo "xdebug.idekey=docker" >> /etc/php5/apache2/conf.d/20-xdebug.ini &&\  
echo "xdebug.remote_enable=1" >> /etc/php5/apache2/conf.d/20-xdebug.ini &&\  
echo "xdebug.remote_autostart=1" >> /etc/php5/apache2/conf.d/20-xdebug.ini &&\  
echo "xdebug.remote_port=9000" >> /etc/php5/apache2/conf.d/20-xdebug.ini &&\  
echo "xdebug.remote_handler=dbgp" >> /etc/php5/apache2/conf.d/20-xdebug.ini
&&\  
echo "xdebug.profiler_enable_trigger=1" >>
/etc/php5/apache2/conf.d/20-xdebug.ini &&\  
echo "xdebug.max_nesting_level=250" >> /etc/php5/apache2/conf.d/20-xdebug.ini  
  
# Add volumes for MySQL & Apache  
VOLUME ["/etc/mysql", "/var/lib/mysql" , "/var/www/"]  
  
# Set the port  
EXPOSE 1025 1080 80 3306 9000  
# Set working directory  
WORKDIR /var/www/html  
  
# Run  
CMD ["/run.sh"]  

