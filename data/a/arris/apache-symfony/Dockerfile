FROM debian:squeeze  
MAINTAINER Arris Ray <arris.ray@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# http://dino.ciuffetti.info/2013/03/how-to-install-php-52-on-squeeze/  
ADD lenny /etc/apt/preferences.d/lenny  
RUN echo "deb http://archive.debian.org/debian lenny main contrib non-free" >>
/etc/apt/sources.list  
RUN apt-get update \  
&& apt-get remove --purge php5\\* \  
&& apt-get update \  
&& apt-get clean \  
&& apt-get -yq install \  
supervisor \  
mysql-server \  
libapache2-mod-php5 \  
php5-curl \  
php5-mysql \  
php5-xsl \  
php-pear \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure PHP (CLI and Apache)  
# RUN sed -i "s/magic_quotes_gpc = On/magic_quotes_gpc = false/"
/etc/php5/apache2/php.ini  
# RUN sed -i "s/post_max_size =/post_max_size = 16MB/"
/etc/php5/apache2/php.ini  
# RUN sed -i "s/upload_max_filesize =/upload_max_filesize = 8MB/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/;date.timezone =/date.timezone = UTC/" /etc/php5/cli/php.ini \  
&& sed -i "s/;date.timezone =/date.timezone = UTC/" /etc/php5/apache2/php.ini  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php5/apache2/php.ini  
RUN chown -R www-data:www-data /usr/share/php/data  
  
# Configure Apache vhost  
RUN rm -rf /var/www/*  
RUN rm -rf /etc/apache2/sites-enabled/*  
RUN a2enmod rewrite  
RUN a2enmod php5  
ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Add main start script for when image launches  
ADD start_apache2.sh /opt/start_apache2.sh  
ADD start_mysqld.sh /opt/start_mysqld.sh  
ADD start.sh /opt/start.sh  
RUN chmod 0755 /opt/*.sh  
ADD supervisord_apache2.conf /etc/supervisor/conf.d/supervisord_apache2.conf  
ADD supervisord_mysqld.conf /etc/supervisor/conf.d/supervisord_mysqld.conf  
  
# Install Symfony  
RUN pear upgrade -f PEAR  
RUN pear channel-discover pear.symfony-project.com  
RUN pear install symfony/symfony-1.0.0  
# HACK!  
RUN sed -i "/check:/d" /usr/share/php/data/symfony/config/php.yml  
RUN sed -i "/zend.ze1_compatibility_mode: off/d"
/usr/share/php/data/symfony/config/php.yml  
# http://www.alexfilatov.com/2009/12/09/symfony-unable-to-return-affix-for-
unknown-creoletype  
RUN sed -i "s/const TEXT = 17/const TEXT = 30/"
/usr/share/php/symfony/vendor/creole/CreoleTypes.php  
  
# Setup shared volume for application code  
# See:
https://github.com/boot2docker/boot2docker/issues/581#issuecomment-114804894  
ADD . /var/www/askeet  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
# Setup MySQL  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
RUN rm -rf /var/lib/mysql/*  
ADD create_mysql_admin_user.sh /opt/create_mysql_admin_user.sh  
RUN chmod 0755 /opt/*.sh  
RUN chown -R mysql:mysql /etc/mysql  
RUN chown -R mysql:mysql /var/lib/mysql  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
# Setup Vim  
ADD .vimrc /root/.vimrc  
  
EXPOSE 80  
EXPOSE 3306  
CMD ["/opt/start.sh"]  
  

