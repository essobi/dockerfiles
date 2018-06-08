FROM ubuntu:16.04  
LABEL maintainer="jipeng.huang@geneegroup.com"  
  
ENV LANG='en_US.utf8' \  
TERM="xterm-color" \  
MAIL_HOST="172.17.42.1" \  
MAIL_FROM="sender@gini" \  
GINI_ENV="production" \  
COMPOSER_PROCESS_TIMEOUT=40000 \  
COMPOSER_HOME="/usr/local/share/composer"  
# Install cURL  
RUN apt-get -q update && apt-get install -yq curl bash vim supervisor && apt-
get -y autoclean && apt-get -y clean  
  
# Install PHP  
RUN apt-get install -yq php7.0-cli php7.0-dev && \  
apt-get -y autoclean && apt-get -y clean && \  
echo "error_log = /var/log/php7/cli.log" >> /etc/php/7.0/cli/php.ini && \  
echo "session.save_handler = redis" >> /etc/php/7.0/cli/php.ini && \  
echo "session.save_path = \"tcp://172.17.42.1:6379\"" >>
/etc/php/7.0/cli/php.ini  
  
RUN mkdir -p /var/log/php7 && \  
touch /var/log/php7/cli.log && \  
chown -R www-data:www-data /var/log/php7  
  
RUN apt-get install -yq php7.0-mbstring php7.0-gd php7.0-mcrypt php7.0-mysql
php7.0-sqlite3 php7.0-curl php7.0-ldap php7.0-intl php7.0-zip php-redis  
  
RUN pecl install swoole-2.1.2 && \  
echo "extension=swoole.so" > /etc/php/7.0/mods-available/swoole.ini && \  
phpenmod swoole  
  
RUN apt-get -y install libyaml-dev && \  
printf '\n' | pecl install yaml-2.0.2 && \  
echo "extension=yaml.so" > /etc/php/7.0/mods-available/yaml.ini && \  
phpenmod yaml  
  
# Install msmtp-mta  
RUN apt-get install -yq msmtp-mta && apt-get -y autoclean && apt-get -y clean  
ADD msmtprc /etc/msmtprc  
  
# Install Development Tools  
RUN apt-get install -yq git  
  
# Install Composer  
RUN mkdir -p /usr/local/bin && (curl -sL https://getcomposer.org/installer |
php) && \  
mv composer.phar /usr/local/bin/composer && \  
echo 'export PATH="/usr/local/share/composer/vendor/bin:$PATH"' >>
/etc/profile.d/composer.sh  
  
# Install Gini  
RUN mkdir -p /usr/local/share && git clone https://github.com/iamfat/gini
/usr/local/share/gini \  
&& cd /usr/local/share/gini && bin/gini composer init -f \  
&& /usr/local/bin/composer update --prefer-dist --no-dev \  
&& mkdir -p /data/gini-modules  
  
ENV
PATH="/usr/local/share/gini/bin:/usr/local/share/composer/vendor/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
\  
GINI_MODULE_BASE_PATH="/data/gini-modules"  
ADD start /start  
WORKDIR /data/gini-modules  
CMD ["/usr/bin/supervisord", "--nodaemon", "-c",
"/etc/supervisor/supervisord.conf"]  

