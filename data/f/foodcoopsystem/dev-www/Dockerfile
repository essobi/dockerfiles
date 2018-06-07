FROM ubuntu:trusty  
MAINTAINER Jarek Sobiecki <jsobiecki@baddrop.com>  
  
# Install packages (this is generic version with all required extensions).  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server
php5-mysql pwgen php-apc php5-mcrypt php5-curl php5-xhprof php5-xdebug
php5-memcache php5-gd curl unzip  
  
# Configure open ssh  
# See: http://docs.docker.com/examples/running_ssh_service/ for more details  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> /etc/profile  
  
# Add image configuration and scripts  
ADD scripts/start-apache2.sh /start-apache2.sh  
ADD scripts/start-selenium.sh /start-selenium.sh  
ADD scripts/run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD configs/php/php.ini /etc/php5/apache2/conf.d/40_custom.ini  
ADD configs/php/php.ini /etc/php5/cli/conf.d/40_custom.ini  
ADD configs/supervisor/supervisord-apache2.conf
/etc/supervisor/conf.d/supervisord-apache2.conf  
ADD configs/supervisor/supervisord-sshd.conf
/etc/supervisor/conf.d/supervisord-sshd.conf  
ADD configs/supervisor/supervisord-selenium.conf
/etc/supervisor/conf.d/supervisord-selenium.conf  
  
# config to enable .htaccess  
ADD configs/apache/apache_default /etc/apache2/sites-
available/000-default.conf  
ADD configs/apache/apache_default_ssl /etc/apache2/sites-
available/000-default-ssl.conf  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
# Install composer and newest stable drush  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
RUN git clone https://github.com/drush-ops/drush.git /usr/local/src/drush && \  
cd /usr/local/src/drush && \  
git checkout 7.x && \  
ln -s /usr/local/src/drush/drush /usr/bin/drush && \  
composer install  
  
# Install tools required for behat testings  
# Firefox  
# Selenium  
# Xvfb and x11vnc  
RUN apt-get -y install xvfb x11vnc firefox openjdk-7-jre openbox  
RUN mkdir /usr/local/lib/selenium && curl http://selenium-
release.storage.googleapis.com/2.46/selenium-server-standalone-2.46.0.jar -o
/usr/local/lib/selenium/selenium.jar  
  
# Install helper tools  
RUN apt-get -y install vim  
  
#Enviornment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
EXPOSE 80 22  
# Add volumes for Apache logs  
VOLUME ["/var/log/apache2" ]  
  
CMD ["/run.sh"]  

