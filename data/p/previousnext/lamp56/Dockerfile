# This is a docker Drupal environment.  
FROM previousnext/base:latest  
MAINTAINER Peter Lieverdink <peter.lieverdink@previousnext.com.au>  
  
RUN apt-get update -y  
  
##  
# Apache.  
##  
# We add the stable PHP 5.6 repository.  
RUN add-apt-repository ppa:ondrej/php5-5.6  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 php5
libapache2-mod-php5 php5-curl php5-mcrypt php5-mysql php5-gd php-apc php-pear
php5-dev php5-pspell php5-memcached nullmailer libssl-dev  
  
# This will need a port and an updated ppa.  
# We add our own php5-twig repository.  
# RUN apt-add-repository ppa:previousnext/ppa  
# RUN apt-get update  
# RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5-twig  
ADD ./scripts/foreground.sh /etc/apache2/foreground.sh  
RUN rm -rf /var/www/  
RUN chmod 755 /etc/apache2/foreground.sh  
  
# This fixes missing file errors.  
RUN touch /etc/apache2/httpd.conf  
RUN mkdir /etc/apache2/conf.d  
  
# Mods.  
RUN cd /etc/apache2/mods-enabled && ln -s ../mods-available/rewrite.load .  
RUN cd /etc/apache2/mods-enabled && ln -s ../mods-available/headers.load .  
  
# We are removing this because we deal with it in our own custom apache2.conf.  
RUN rm /etc/apache2/mods-enabled/mpm_prefork.conf  
  
# vHost.  
RUN rm -f /etc/apache2/sites-enabled/*  
ADD ./conf/apache2/vhost.conf /etc/apache2/sites-available/drupal.conf  
RUN ln -s /etc/apache2/sites-available/drupal.conf /etc/apache2/sites-
enabled/drupal.conf  
  
# Perms.  
RUN adduser deployer www-data  
  
# Environment.  
ADD ./conf/environment/environment /etc/environment  
  
##  
# PHP.  
##  
ADD ./conf/php/php.ini /etc/php5/apache2/php.ini  
ADD ./conf/php/php.ini /etc/php5/cli/php.ini  
  
# Composer.  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer && chmod +x
/usr/local/bin/composer  
  
# Bundler.  
RUN apt-get install -y ruby1.9.1 ruby1.9.1-dev  
RUN gem install bundler -v 1.6.3  
  
# Phing.  
RUN pear channel-discover pear.phing.info  
RUN pear install phing/phing-2.6.1  
  
# Drush.  
RUN mkdir -p /opt/drush-7  
RUN cd /opt/drush-7 && COMPOSER_HOME=/opt/drush-7 composer require drush/drush
7  
RUN ln -s /opt/drush-7/vendor/bin/drush /usr/local/bin/drush7  
  
RUN mkdir -p /opt/drush-8  
RUN cd /opt/drush-8 && COMPOSER_HOME=/opt/drush-8 composer require drush/drush
8  
RUN ln -s /opt/drush-8/vendor/bin/drush /usr/local/bin/drush8  
  
# Drush 7 is default here.  
RUN ln -s /opt/drush/drush /usr/local/bin/drush  
  
# Xdebug.  
RUN apt-get install -y php5-xdebug  
  
##  
# Mysql.  
##  
# Bumping MariaDB to 10.1.  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN add-apt-repository 'deb
http://mirror.aarnet.edu.au/pub/MariaDB/repo/10.1/ubuntu precise main'  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mariadb-server  
ADD ./conf/mysql/my.cnf /etc/mysql/my.cnf  
  
##  
## Memcached.  
##  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install memcached  
  
##  
# wkhtmltopdf.  
# We'll probably want a PPA for this at some stage.  
##  
RUN apt-get -y install fontconfig libfontconfig1 libfreetype6 libpng12-0
zlib1g libjpeg-turbo8 libssl1.0.0 libx11-6 libxext6 libxrender1 xfonts-base
xfonts-75dpi libstdc++6 libc6  
RUN wget -q -O /tmp/wkhtmltox.deb
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb  
RUN dpkg -i /tmp/wkhtmltox.deb  
  
##  
# Cron.  
##  
ADD ./conf/cron/drupal /etc/cron.d/drupal  
  
##  
# Scripts.  
# This is where we add all our utlitiy scripts.  
##  
ADD ./scripts/permissions.sh /root/permissions.sh  
  
##  
# Supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
EXPOSE 22 80  
CMD ["/root/start.sh"]  

