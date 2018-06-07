FROM ubuntu:16.04  
MAINTAINER Cristiano Baptista "cristiano.baptista@ponticlaro.com"  
# Initial update  
RUN apt-get dist-upgrade; \  
apt-get update  
  
# Install utilities  
RUN apt-get install -y --allow-unauthenticated \  
software-properties-common \  
python-software-properties \  
build-essential \  
openssl \  
openssh-server \  
git \  
zsh \  
vim \  
htop \  
wget \  
curl \  
nodejs \  
npm \  
ruby \  
python-pip  
  
# Add PHP repository  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
  
# Add NGINX mainline repository  
RUN add-apt-repository ppa:nginx/stable  
  
# Update  
RUN apt-get update  
  
# Install required packages  
RUN apt-get install -y --allow-unauthenticated \  
supervisor \  
imagemagick \  
graphicsmagick \  
mysql-client \  
nginx-extras \  
php7.1-fpm \  
php7.1-curl \  
php7.1-gd \  
php7.1-mbstring \  
php7.1-mysql \  
php7.1-pgsql \  
php7.1-xml \  
php7.1-soap \  
php-imagick \  
php-memcached \  
php-redis  
  
# Install supervisor-stdout  
RUN pip install supervisor-stdout  
  
# Symlink NodeJS  
RUN ln -s "$(which nodejs)" /usr/bin/node  
  
# Install node packages  
# - Grunt CLI  
RUN npm install -g \  
grunt-cli  
  
# Install SASS gem  
RUN apt-get install -y ruby-dev autogen autoconf libtool; \  
gem install sass  
  
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
  
# NGINX: copy config files to container  
ADD .docker/nginx/v1/config/nginx.conf /etc/nginx/nginx.conf  
ADD .docker/nginx/v1/config/wordpress.conf /etc/nginx/sites-available/default  
  
# PHP-FPM: copy config files to container  
ADD .docker/php-fpm/v1/config/php.ini /etc/php/7.1/fpm/php.ini  
ADD .docker/php-fpm/v1/config/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
ADD .docker/php-fpm/v1/config/pool.d /etc/php/7.1/fpm/pool.d  
ADD .docker/php-fpm/v1/config/conf.d/9999-blackfire.ini
/etc/php/7.1/fpm/conf.d/9999-blackfire.ini  
  
# Elastic Beats: copy config files to container  
ADD .docker/filebeat/filebeat.yml /etc/filebeat/filebeat.yml  
ADD .docker/topbeat/topbeat.yml /etc/topbeat/topbeat.yml  
ADD .docker/packetbeat/packetbeat.yml /etc/packetbeat/packetbeat.yml  
  
# Supervisord: copy config file to container  
ADD .docker/supervisor/v1/supervisord-lep-stack.conf
/etc/supervisor/supervisord.conf  
  
# Custom Tools:  
# - Mysql Import  
ADD .docker/custom-tools/mysql-import.sh /usr/bin/mysql-import  
RUN chmod +x /usr/bin/mysql-import  
  
# Expose container ports  
EXPOSE 80 443  
# Use supervisord to keep processes alive  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

