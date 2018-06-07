FROM phusion/baseimage:0.9.19  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
php php-curl php-zip php-pdo php-gd php-xml php-apcu php-mysql php-intl php-
mbstring  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN composer global require "phpunit/phpunit=5.6.3" && \  
ln -s ~/.composer/vendor/bin/phpunit /usr/bin/  
  
RUN mkdir /run/php /opt/tmp && \  
chown www-data /opt/tmp  
  
ADD misc/bashrc /root/bashrc  
  
RUN echo "source /root/bashrc" >> ~/.bashrc  
  
RUN mkdir -p /opt/ktv/fs/cache /var/lib/php/session && \  
chown www-data:www-data -R /opt/ktv/fs /var/lib/php/session  
  
RUN rm -rf /etc/service/{sshd,syslog-forwarder,syslog-ng,cron} && \  
rm -rf /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
EXPOSE 80  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV STAGE_ENV=test  
  
WORKDIR /var/www

