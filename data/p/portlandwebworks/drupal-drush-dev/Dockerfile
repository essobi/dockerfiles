FROM php:5.6-cli  
MAINTAINER portlandwebworks  
  
ENTRYPOINT /root/entrypoint.sh  
  
# Change our shell  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
# Install pre-requisite software  
RUN apt-get update \  
&& apt-get install -y \  
mysql-client \  
openssh-server \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
libxml2-dev \  
&& apt-get clean  
  
# Install additional PHP extensions  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip soap xmlrpc
opcache \  
&& pecl install -o -f xdebug \  
&& pecl install -o -f redis-2.2.8 \  
&& rm -rf /tmp/pear  
  
# Install drush  
RUN php -r "readfile('http://files.drush.org/drush.phar');" > drush \  
&& chmod +x drush \  
&& mv drush /usr/local/bin  
  
# Configure ssh  
RUN mkdir /root/.ssh \  
&& touch /root/.ssh/authorized_keys \  
&& mkdir /var/run/sshd \  
&& chmod 0755 /var/run/sshd \  
&& chmod 700 /root/.ssh \  
&& chmod 600 /root/.ssh/* \  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Copy configs  
ADD conf/* $PHP_INI_DIR/conf.d/  
  
# Add entrypoint  
ADD entrypoint.sh /root  

