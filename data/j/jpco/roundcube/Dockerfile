FROM codingwell/rpi-raspbian-qemu  
  
MAINTAINER J.P.C. Oudeman  
  
COPY assets/bin /usr/local/bin  
RUN [ "cross-build-start" ]  
  
RUN \  
echo "deb http://mirrordirector.raspbian.org/raspbian/ stretch main" >>
/etc/apt/sources.list.d/mirrordirector.list && \  
apt-key adv \--fetch-keys
http://mirrordirector.raspbian.org/raspbian.public.key && \  
echo "APT::Default-Release "jessie";" > /etc/apt/apt.conf.d/default-release \  
&& apt-get update \  
&& apt-get install -y \  
curl \  
git \  
&& apt-get install -y -t stretch \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-sqlite \  
php7.0-xsl \  
php7.0-opcache \  
php-xml \  
php-mail \  
php-mail-mime \  
php-net-smtp \  
php-pear \  
&& \  
set -ex \  
&& cd /etc/php/7.0/fpm \  
&& { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo; \  
echo '[www]'; \  
echo '; if we send this to /proc/self/fd/1, it never appears'; \  
echo 'access.log = /proc/self/fd/2'; \  
echo; \  
echo 'clear_env = no'; \  
echo; \  
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee pool.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = [::]:9000'; \  
} | tee pool.d/zz-docker.conf \  
&& \  
\  
# Install Roundcube + plugins  
VERSION=`latestversion roundcube/roundcubemail` \  
&& mkdir -p /usr/src/roundcube \  
&& cd /usr/src/roundcube \  
&& git clone \--branch ${VERSION} \--depth 1
https://github.com/roundcube/roundcubemail.git . \  
&& rm -rf .git installer \  
&& \  
# Configuration of Roundcube  
{ \  
echo "<?php"; \  
echo "\$config = array();"; \  
echo "\$config['db_dsnw'] = 'sqlite:////var/mail/roundcube/sqlite.db';"; \  
echo "\$config['imap_conn_options'] ="; \  
echo "\$config['smtp_conn_options'] ="; \  
echo "\$config['managesieve_conn_options'] = ["; \  
echo " 'ssl' => ["; \  
echo " 'verify_peer' => false,"; \  
echo " 'verify_peer_name' => false,"; \  
echo " 'allow_self_signed' => true,"; \  
echo " ],"; \  
echo "];"; \  
echo "\$config['default_port'] = 143;"; \  
echo "\$config['smtp_port'] = 587;"; \  
echo "\$config['smtp_user'] = '%u';"; \  
echo "\$config['smtp_pass'] = '%p';"; \  
} | tee /usr/src/roundcube/config/config.inc.php \  
&& tar czf /usr/src/roundcube.tar.gz -C /usr/src/roundcube . \  
&& rm -r /usr/src/roundcube \  
&& mkdir /var/run/php \  
&& \  
  
# Cleanup  
apt-get -y purge git \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN [ "cross-build-end" ]  
  
VOLUME ["/var/www/html", "/var/mail"]  
WORKDIR /var/www/html  
EXPOSE 9000  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["php-fpm7.0"]

