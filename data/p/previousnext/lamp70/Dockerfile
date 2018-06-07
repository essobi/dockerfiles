# This is a docker Drupal environment.  
FROM ubuntu:14.04  
MAINTAINER Peter Lieverdink <peter.lieverdink@previousnext.com.au>  
  
##  
# Perform the steps our base image would do for other containers.  
##  
##  
# APT.  
##  
RUN apt-get -y update  
RUN apt-get -y dist-upgrade  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -fs /bin/true /sbin/initctl  
  
##  
# Base.  
##  
# APT.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install fail2ban vim git curl
wget pwgen python-setuptools vim-tiny sudo python-software-properties cron
unzip  
  
# Ensure that locale files are regenerated.  
RUN locale-gen en_AU en_AU.UTF-8  
RUN dpkg-reconfigure locales  
  
##  
# Users.  
##  
RUN useradd --create-home --shell /bin/bash --user-group deployer  
  
##  
# SSHD.  
##  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
  
##  
# Fix ssh.  
# See https://github.com/docker/docker/issues/5663  
##  
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/sshd  
  
##  
# Fail2ban.  
##  
RUN mkdir /var/run/fail2ban  
  
##  
# Rsyslog.  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install rsyslog rsyslog-doc  
RUN sed -i 's/xconsole/console/g' /etc/rsyslog.d/*  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
##  
# Supervisord.  
##  
RUN easy_install supervisor  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
RUN mkdir /var/log/supervisor/  
  
##  
# Need this for apt-add-repository.  
##  
RUN apt-get install -y software-properties-common language-pack-en-base  
  
##  
# Fix UTF-8 language issue with the PPA.  
##  
RUN locale-gen en_AU.UTF-8  
  
##  
# Apache.  
##  
# We add the now-stable PHP 7.0 repository.  
RUN LC_ALL=en_AU.UTF-8 apt-add-repository ppa:ondrej/php  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 php7.0
libapache2-mod-php7.0 php7.0-bcmath php7.0-curl php7.0-gd php7.0-json
php7.0-mbstring php7.0-mcrypt php7.0-mysql php7.0-opcache php7.0-pspell
php7.0-readline php7.0-xml php-apcu php-apcu-bc nullmailer libssl-dev  
  
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
RUN a2enmod rewrite  
RUN a2enmod headers  
  
# We are removing this because we deal with it in our own custom apache2.conf.  
RUN rm /etc/apache2/mods-enabled/mpm_prefork.conf  
  
# vHost.  
RUN rm -f /etc/apache2/sites-enabled/*  
ADD ./conf/apache2/vhost.conf /etc/apache2/sites-available/drupal.conf  
RUN a2ensite drupal  
  
# Perms.  
RUN adduser deployer www-data  
  
# Environment.  
ADD ./conf/environment/environment /etc/environment  
  
##  
# PHP.  
##  
# ADD ./conf/php/php.ini /etc/php/7.0/apache2/php.ini  
# ADD ./conf/php/php.ini /etc/php/7.0/cli/php.ini  
ADD ./conf/php/apcu.ini /etc/php/7.0/mods-available/apcu.ini  
  
# Composer.  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer && chmod +x
/usr/local/bin/composer  
  
# Bundler.  
RUN apt-get install -y ruby1.9.1 ruby1.9.1-dev  
RUN gem install bundler -v 1.6.3  
  
# Phing.  
RUN mkdir -p /opt/phing-2.6.1  
RUN cd /opt/phing-2.6.1 && COMPOSER_HOME=/opt/phing-2.6.1 composer --prefer-
dist require phing/phing 2.6.1  
RUN ln -s /opt/phing-2.6.1/vendor/bin/phing /usr/local/bin/phing  
  
# Drush.  
RUN mkdir -p /opt/drush-7  
RUN cd /opt/drush-7 && COMPOSER_HOME=/opt/drush-7 composer --prefer-dist
require drush/drush 7  
RUN ln -s /opt/drush-7/vendor/bin/drush /usr/local/bin/drush7  
  
RUN mkdir -p /opt/drush-8  
RUN cd /opt/drush-8 && COMPOSER_HOME=/opt/drush-8 composer --prefer-dist
require drush/drush 8.0.5  
RUN ln -s /opt/drush-8/vendor/bin/drush /usr/local/bin/drush8  
RUN ln -s /opt/drush-8/vendor/bin/drush /usr/local/bin/drush  
  
##  
# Mysql.  
##  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN add-apt-repository 'deb
http://mirror.aarnet.edu.au/pub/MariaDB/repo/5.5/ubuntu trusty main'  
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
# RUN apt-get -y install fontconfig libfontconfig1 libfreetype6 libpng12-0
zlib1g libjpeg-turbo8 libssl1.0.0 libx11-6 libxext6 libxrender1 xfonts-base
xfonts-75dpi libstdc++6 libc6  
# RUN wget -q -O /tmp/wkhtmltox.deb
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb  
# RUN dpkg -i /tmp/wkhtmltox.deb  
##  
# Cleanup  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y autoremove  
  
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

