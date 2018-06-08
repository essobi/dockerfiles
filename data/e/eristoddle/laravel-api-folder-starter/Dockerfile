FROM ubuntu:14.04  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Add php 5.6  
RUN sudo apt-get update  
RUN sudo apt-get install software-properties-common -y  
RUN sudo add-apt-repository ppa:ondrej/php -y  
RUN sudo apt-get update  
RUN sudo apt-get upgrade -y --force-yes  
RUN sudo apt-get install -y --force-yes php5.6  
  
# Basic Requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y --force-yes
install\  
apache2\  
curl\  
zip\  
unzip\  
git\  
libapache2-mod-php5.6\  
php5.6-mysql php-apc  
  
# Laravel Requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install\  
php5.6-curl\  
php5.6-gd\  
php5.6-intl\  
php-pear\  
php5.6-imagick\  
php5.6-imap\  
php5.6-mbstring\  
php5.6-mcrypt\  
php5.6-memcache\  
php5-ming\  
php5.6-ps\  
php5.6-pspell\  
php5.6-recode\  
php5.6-sqlite\  
php5.6-tidy\  
php5.6-xmlrpc\  
php5.6-xsl  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
# apache config  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2
/var/run/apache2 /var/log/apache2 /var/www/html  
# copy the config file  
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf  
#Set the ENV vars  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
#Turn mod_rewrite on  
RUN /usr/sbin/a2enmod rewrite  
#Set the file perms correctly on the web root  
RUN chown -R www-data:www-data /var/www/  
  
# php config  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/5.6/apache2/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/5.6/apache2/php.ini  
RUN sed -i -e "s/short_open_tag\s*=\s*Off/short_open_tag = On/g"
/etc/php/5.6/apache2/php.ini  
  
# fix for php5-mcrypt  
RUN /usr/sbin/php5enmod mcrypt  
  
#MySQL setup  
COPY laravel_init.sh /laravel_init.sh  
RUN chmod 777 /laravel_init.sh  
  
WORKDIR /var/www/html  
  
EXPOSE 80  
#Add the directory to the web root  
ONBUILD ADD . /var/www/html  
  
#Make sure apache can access it  
ONBUILD RUN chown -R www-data:www-data /var/www  
  
#Bootstrap the DB and site  
ENTRYPOINT ["/laravel_init.sh"]  

