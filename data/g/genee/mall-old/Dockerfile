FROM debian:8  
MAINTAINER maintain@geneegroup.com  
  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM="xterm-color" \  
MAIL_HOST="172.17.0.1" \  
MAIL_FROM="sender@gini" \  
COMPOSER_PROCESS_TIMEOUT=40000 \  
COMPOSER_HOME="/usr/local/share/composer"  
# Install cURL  
# Install PHP 5.6  
# Install Friso  
# Install git  
# Install composer  
# Install msmtp-mta  
RUN apt-get update \  
&& apt-get install -y curl apt-utils bash vim \  
&& apt-get install -y locales gettext \  
&& sed -i 's/# en_US.UTF-8/en_US.UTF-8/' /etc/locale.gen \  
&& sed -i 's/# zh_CN.UTF-8/zh_CN.UTF-8/' /etc/locale.gen \  
&& locale-gen && /usr/sbin/update-locale LANG="en_US.UTF-8"
LANGUAGE="en_US:en" \  
&& apt-get install -y php5-fpm php5-cli php5-intl php5-gd \  
php5-mcrypt php5-mysqlnd php5-redis php5-sqlite php5-curl php5-ldap
libyaml-0-2 \  
php5-zmq php5-redis \  
&& sed -i 's/^listen\s*=.*$/listen = 0.0.0.0:9000/'
/etc/php5/fpm/pool.d/www.conf \  
&& sed -i 's/^error_log\s*=.*$/error_log = syslog/' /etc/php5/fpm/php-fpm.conf
\  
&& sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = syslog/'
/etc/php5/fpm/php.ini \  
&& sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = syslog/'
/etc/php5/cli/php.ini \  
&& PHP_EXTENSION_DIR=$(echo '<?= PHP_EXTENSION_DIR ?>'|php5) \  
&& PHP_MODULE_DIR=php-$(echo '<?= basename(PHP_EXTENSION_DIR) ?>'|php5) \  
&& curl -sLo "${PHP_EXTENSION_DIR}/yaml.so"
"http://files.docker.genee.in/debian/${PHP_MODULE_DIR}/yaml.so" \  
&& echo "extension=yaml.so" > /etc/php5/mods-available/yaml.ini \  
&& php5enmod yaml \  
&& curl -sLo /usr/lib/libfriso.so
"http://files.docker.genee.in/debian/libfriso.so" \  
&& curl -sLo "${PHP_EXTENSION_DIR}/friso.so"
"http://files.docker.genee.in/debian/${PHP_MODULE_DIR}/friso.so" \  
&& curl -sL http://files.docker.genee.in/friso-etc.tgz | tar -zxf - -C /etc \  
&& printf
"extension=friso.so\n\n[friso]\nfriso.ini_file=/etc/friso/friso.ini\n" >
/etc/php5/mods-available/friso.ini \  
&& php5enmod friso \  
&& apt-get install -y alien libaio1 \  
&& curl -sLo oracle.rpm \  
http://files.docker.genee.in/oracle-
instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm \  
&& alien -i oracle.rpm && rm oracle.rpm \  
&& apt-get autoremove --purge -y alien \  
&& curl -sLo "${PHP_EXTENSION_DIR}/oci8.so"
"http://files.docker.genee.in/debian/${PHP_MODULE_DIR}/oci8.so" \  
&& echo "extension=oci8.so" > /etc/php5/mods-available/oci8.ini \  
&& php5enmod oci8 \  
&& mkdir -p /usr/local/bin && (curl -sL https://getcomposer.org/installer |
php) \  
&& mv composer.phar /usr/local/bin/composer \  
&& echo 'export PATH="/usr/local/share/composer/vendor/bin:$PATH"' >>
/etc/profile.d/composer.sh \  
&& apt-get install -y python-setuptools && easy_install xlsx2csv \  
&& apt-get install -y msmtp-mta git  
  
ADD msmtprc /etc/msmtprc  
  
EXPOSE 9000  
# Add interactive shell  
ADD interactive.sh /interactive.sh  
  
ADD start /start  
CMD ["/start"]  

