FROM drupal:7  
MAINTAINER Thom Toogood <thomtoogood@gmail.com>  
ENV REFRESHED_AT 2015-10-09  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && apt-get install -y \  
libbz2-dev \  
unzip \  
git-core \  
curl \  
wget \  
mysql-client \  
mysql-server \  
php5-mysql \  
php5-gd \  
php5-curl \  
openssh-server \  
supervisor \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install bz2 pcntl zip \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get -y autoremove  
  
# Disable sendmail.  
ENV PHP_OPTIONS '-d sendmail_path=/bin/true -d phar.readonly=0'  
# Install Composer.  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
ENV PATH $PATH:/root/.composer/vendor/bin  
  
# Install Drush.  
RUN composer global require drush/drush:7.x  
  
WORKDIR /var/www/html  
  
# Install Drupal.  
RUN /etc/init.d/mysql start \  
&& drush si -y -q standard \  
\--db-url="mysql://root:@127.0.0.1:3306/drupal" \  
\--account-name="drupal" \  
\--account-pass="drupal" \  
\--site-name="Drupal 7" \  
&& mkdir -p sites/default/files \  
&& chown -R www-data:www-data .  
  
RUN wget https://raw.githubusercontent.com/thom8/drupal-
kitematic/master/includes/start.sh -O /start.sh \  
&& chmod +x /start.sh  
RUN wget https://raw.githubusercontent.com/thom8/drupal-
kitematic/master/includes/supervisord.conf -O
/etc/supervisor/conf.d/supervisord.conf  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
EXPOSE 22 80  
ENV SHELL /bin/bash  
CMD ["/bin/bash", "/start.sh"]

