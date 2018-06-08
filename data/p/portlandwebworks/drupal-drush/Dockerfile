FROM php:5.6-cli  
MAINTAINER portlandwebworks  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
  
# Change our shell  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
# Install pre-requisite software  
RUN apt-get update \  
&& apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
libxml2-dev \  
mysql-client \  
openssh-server \  
curl \  
&& apt-get clean  
  
# Install additional PHP extensions  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip soap xmlrpc
opcache \  
&& pecl install -o -f xdebug \  
&& rm -rf /tmp/pear  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install Drush  
RUN composer global require drush/drush \  
&& composer global update \  
&& ln -s /root/.composer/vendor/bin/drush /usr/local/bin/drush  
  
# Install Drupal Console  
RUN curl https://drupalconsole.com/installer -L -o drupal.phar \  
&& mv drupal.phar /usr/local/bin/drupal \  
&& chmod +x /usr/local/bin/drupal \  
&& drupal init --override  
  
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

