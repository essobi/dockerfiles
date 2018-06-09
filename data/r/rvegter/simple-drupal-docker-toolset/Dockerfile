FROM debian:wheezy  
MAINTAINER Reinier Vegter <hr.vegter@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install packages.  
# Dummy number to increase.  
# Makes sure apt cache is refreshed on a new container build.  
# Only needed if this package list is changed.  
RUN number=6  
RUN apt-get update  
RUN apt-get install -y \  
vim \  
git \  
wget \  
apache2 \  
php5-cli \  
php5-mysql \  
php5-gd \  
php5-curl \  
php5-ldap \  
php5-mcrypt \  
php-services-json \  
php-soap \  
php5-intl \  
libapache2-mod-php5 \  
curl \  
openssh-server \  
net-tools \  
memcached \  
php5-memcache \  
make \  
php5-dev \  
mongodb \  
php5-xdebug \  
mysql-client \  
libpcre3-dev pkg-config libssl-dev libsslcommon2-dev # for xhgui / xhprof  
  
# install xhprof  
RUN pecl config-set preferred_state beta  
RUN pecl install mongodb  
RUN pecl install xhprof  
  
# Varnish installation.  
RUN apt-get install -y apt-transport-https  
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -  
RUN echo "deb https://repo.varnish-cache.org/debian/ wheezy varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list  
RUN apt-get update  
RUN apt-get install -y varnish  
# Make varnish able to start, since using 'ulimit' is usually forbidden from
container.  
RUN sed -i 's/^ulimit/#ulimit/g' /etc/init.d/varnish  
# Put varnish on port 80, instead of 6081  
RUN sed -i 's/DAEMON_OPTS="-a :6081/DAEMON_OPTS="-a :80/' /etc/default/varnish  
  
RUN apt-get purge -y php5-dev make  
# Cleanup apt cache.  
RUN apt-get clean  
# RUN apt-get autoremove  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install Composer.  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Setup PHP.  
RUN sed -i 's/display_errors = Off/display_errors = On/'
/etc/php5/apache2/php.ini  
RUN sed -i 's/display_errors = Off/display_errors = On/' /etc/php5/cli/php.ini  
  
# Setup Apache.  
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/sites-
available/default  
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/sites-
available/default-ssl  
RUN sed -ri 's/MaxClients\s+[0-9]+/MaxClients 300/g' /etc/apache2/apache2.conf  
RUN sed -ri 's/MaxRequestsPerChild\s+[0-9]+/MaxRequestsPerChild 400/g'
/etc/apache2/apache2.conf  
  
## Add solr proxy to apache  
RUN echo "Listen 8983" >> /etc/apache2/ports.conf  
RUN echo "NameVirtualHost *:8983" >> /etc/apache2/ports.conf  
  
# enable mod  
RUN a2enmod rewrite  
RUN a2enmod proxy  
RUN a2enmod proxy_http  
RUN a2enmod ssl  
  
# Setup SSH.  
RUN echo 'root:root' | chpasswd  
## RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
## RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
## RUN mkdir -p /root/.ssh/ && touch /root/.ssh/authorized_keys  
## RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
# Enable mysql/apache on boot.  
RUN update-rc.d apache2 defaults  
RUN mkdir /var/run/sshd  
  
# Setup Supervisor.  
## RUN echo -e '[program:apache2]\ncommand=/bin/bash -c "source
/etc/apache2/envvars && exec /usr/sbin/apache2
-DFOREGROUND"\nautorestart=true\n\n' >> /etc/supervisor/supervisord.conf  
## RUN echo -e '[program:mysql]\ncommand=/usr/bin/pidproxy
/var/run/mysqld/mysqld.pid /usr/sbin/mysqld\nautorestart=true\n\n' >>
/etc/supervisor/supervisord.conf  
## RUN echo -e '[program:sshd]\ncommand=/usr/sbin/sshd -D\n\n' >>
/etc/supervisor/supervisord.conf  
## RUN echo -e '[program:blackfire]\ncommand=/usr/local/bin/launch-
blackfire\n\n' >> /etc/supervisor/supervisord.conf  
# Let memcached listen on any IP, so it's connectable from outside the
container.  
RUN sed -i 's/-l 127.0.0.1/-l 0.0.0.0/' /etc/memcached.conf  
# Disable memcached by default.  
RUN update-rc.d memcached disable  
  
# Install Drush 7, firephp.  
RUN composer global require drush/drush:7.*  
RUN composer global require firephp/firephp-core  
RUN composer global update  
  
# Set composer folder, so that non-privileged users (www-data) can use it's
content.ADD  
RUN mv /root/.composer /opt/composer  
RUN ln -s /opt/composer /root/.composer  
  
# Unfortunately, adding the composer vendor dir to the PATH doesn't seem to
work. So:  
RUN ln -s /opt/composer/vendor/bin/drush /usr/local/bin/drush  
  
EXPOSE 80 443 22 11211  

