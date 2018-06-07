FROM ubuntu:15.10  
MAINTAINER Cristiano Baptista "cristiano.baptista@ponticlaro.com"  
# Install required packages  
RUN apt-get dist-upgrade; \  
apt-get update; \  
apt-get install -y \  
openssh-server \  
supervisor \  
git \  
zsh \  
vim \  
htop \  
wget \  
curl \  
imagemagick \  
graphicsmagick \  
nodejs \  
npm \  
ruby \  
mysql-client \  
apache2 \  
php5-fpm \  
php5-mysql \  
php5-pgsql \  
php5-xdebug \  
php5-memcached \  
php5-redis \  
php5-gd \  
php5-imagick \  
php5-curl  
  
# Symlink NodeJS  
RUN ln -s "$(which nodejs)" /usr/bin/node  
  
# Install node packages  
# - Grunt CLI  
RUN npm install -g \  
grunt-cli  
  
# Add blackfire repo to sources list  
RUN wget -O - https://packagecloud.io/gpg.key | apt-key add -  
RUN echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list  
  
# Add elastic.co repo to sources list  
RUN wget -O - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add -  
RUN echo "deb http://packages.elastic.co/beats/apt stable main" | tee -a
/etc/apt/sources.list.d/beats.list  
  
# Install:  
# - Elastic Filebeat: https://www.elastic.co/downloads/beats/filebeat/  
# - Elastic Topbeat: https://www.elastic.co/downloads/beats/topbeat/  
# - Elastic Packetbeat: https://www.elastic.co/downloads/beats/packetbeat/  
RUN apt-get update; \  
apt-get install -y \  
filebeat \  
topbeat \  
packetbeat  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
RUN chmod +x /usr/bin/composer  
  
# Copy placeholder code  
ADD app /app  
  
# Apache: copy config files to container  
ADD .docker/apache/config/000-default.conf /etc/apache2/sites-
available/000-default.conf  
  
# Tweak Apache configuration  
RUN a2enmod headers rewrite actions proxy_fcgi alias ssl  
  
# PHP-FPM: copy config files to container  
ADD .docker/php-fpm/v0/config/php.ini /etc/php5/fpm/php.ini  
ADD .docker/php-fpm/v0/config/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD .docker/php-fpm/v0/config/pool.d /etc/php5/fpm/pool.d  
ADD .docker/php-fpm/v0/config/conf.d/9999-blackfire.ini
/etc/php5/fpm/conf.d/9999-blackfire.ini  
  
# Elastic Beats: copy config files to container  
ADD .docker/filebeat/filebeat.yml /etc/filebeat/filebeat.yml  
ADD .docker/topbeat/topbeat.yml /etc/topbeat/topbeat.yml  
ADD .docker/packetbeat/packetbeat.yml /etc/packetbeat/packetbeat.yml  
  
# Supervisord: copy config file to container  
ADD .docker/supervisor/v0/supervisord-lap-stack.conf
/etc/supervisor/supervisord.conf  
  
# Custom Tools:  
# - Mysql Import  
ADD .docker/custom-tools/mysql-import.sh /usr/bin/mysql-import  
RUN chmod +x /usr/bin/mysql-import  
  
# Expose container ports  
EXPOSE 80 443  
# Use supervisord to keep processes alive  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

