FROM drupal:7  
MAINTAINER Paolo Mazzoni <ing.paolo.mazzoni@gmail.com>  
  
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y mysql-client
git  
# Other packages???: libssh2-php openssh-server net-tools (netstat)  
# Install zip (PHP Extension)  
RUN echo "extension=zip.so" > /usr/local/etc/php/conf.d/docker-php-ext-zip.ini  
RUN pecl install zip  
  
# Install Xdebug (PHP Extension)  
RUN pecl install xdebug  
RUN echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/xdebug.so" > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN echo "xdebug.remote_enable=On" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
RUN echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
## Install ssh2 (PHP Extension)  
#printf "\n" | pecl install ssh2-0.12  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install Drush 6  
RUN composer global require drush/drush:6.*  
RUN ln -s /root/.composer/vendor/bin/drush /usr/local/bin/drush  
RUN mkdir /root/drush.dbdumps  
  
# Setup SSH  
#RUN echo 'root:root' | chpasswd  
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
#RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
#RUN mkdir -p /root/.ssh/ && touch /root/.ssh/authorized_keys  
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
# Exposed ports  
#EXPOSE 22 9000  
EXPOSE 9000

