FROM debian:jessie  
MAINTAINER Jack Over <jack@webcaret.nl>  
ENV DEBIAN_FRONTEND noninteractive  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install packages.  
RUN apt-get update  
RUN apt-get install -y \  
vim \  
git \  
apache2 \  
php5-cli \  
php5-mysql \  
php5-gd \  
php5-curl \  
php5-xdebug \  
libapache2-mod-php5 \  
curl \  
mysql-server \  
mysql-client \  
openssh-server \  
wget \  
unzip \  
cron \  
supervisor  
RUN apt-get clean  
  
# Install Composer.  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install Drush 7.  
RUN composer global require drush/drush:7.*  
RUN composer global update  
# Unfortunately, adding the composer vendor dir to the PATH doesn't seem to
work. So:  
RUN ln -s /root/.composer/vendor/bin/drush /usr/local/bin/drush  
  
# Setup PHP.  
RUN sed -i 's/display_errors = Off/display_errors = On/'
/etc/php5/apache2/php.ini  
RUN sed -i 's/display_errors = Off/display_errors = On/' /etc/php5/cli/php.ini  
  
# Setup Apache.  
# In order to run our Simpletest tests, we need to make Apache  
# listen on the same port as the one we forwarded. Because we use  
# 8080 by default, we set it up for that port.  
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www/'
/etc/apache2/sites-available/000-default.conf  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www/'
/etc/apache2/sites-available/default-ssl.conf  
RUN echo "Listen 8080" >> /etc/apache2/ports.conf  
RUN echo "Listen 8443" >> /etc/apache2/ports.conf  
RUN sed -i 's/VirtualHost \\*:80/VirtualHost \\*:\\*/' /etc/apache2/sites-
available/000-default.conf  
RUN sed -i 's/VirtualHost __default__:443/VirtualHost _default_:443
_default_:8443/' /etc/apache2/sites-available/default-ssl.conf  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN a2ensite default-ssl.conf  
  
# Setup MySQL, bind on all addresses.  
RUN sed -i -e 's/^bind-address\s*=\s*127.0.0.1/#bind-address = 127.0.0.1/'
/etc/mysql/my.cnf  
  
# Setup SSH.  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
RUN mkdir -p /root/.ssh/ && touch /root/.ssh/authorized_keys  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Setup Supervisor.  
RUN echo -e '[program:apache2]\ncommand=/bin/bash -c "source
/etc/apache2/envvars && exec /usr/sbin/apache2
-DFOREGROUND"\nautorestart=true\n\n' >> /etc/supervisor/supervisord.conf  
RUN echo -e '[program:mysql]\ncommand=/usr/bin/pidproxy
/var/run/mysqld/mysqld.pid /usr/sbin/mysqld\nautorestart=true\n\n' >>
/etc/supervisor/supervisord.conf  
RUN echo -e '[program:sshd]\ncommand=/usr/sbin/sshd -D\n\n' >>
/etc/supervisor/supervisord.conf  
RUN echo -e '[program:cron]\ncommand=cron -f\nautorestart=false \n\n' >>
/etc/supervisor/supervisord.conf  
  
# Setup XDebug.  
RUN echo "xdebug.max_nesting_level = 300" >>
/etc/php5/apache2/conf.d/20-xdebug.ini  
RUN echo "xdebug.max_nesting_level = 300" >>
/etc/php5/cli/conf.d/20-xdebug.ini  
  
RUN /etc/init.d/mysql start  
  
EXPOSE 80 3306 22 443  
CMD exec supervisord -n  

