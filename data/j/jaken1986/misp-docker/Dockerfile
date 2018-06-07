FROM ubuntu:16.04  
  
COPY ["supervisord.conf", "/etc/supervisor/conf.d/supervisord.conf"]  
COPY ["run.sh", "/run.sh"]  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y postfix curl gcc git gnupg-agent make python openssl
redis-server sudo vim zip \  
apache2 apache2-doc apache2-utils libapache2-mod-php php php-cli mysql-client
\  
php-crypt-gpg php-dev php-json php-mysql php-opcache php-readline php-redis
php-xml \  
python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev python-setuptools
python3 python3-pip \  
libjpeg-dev cron logrotate supervisor syslog-ng-core locales libfuzzy-dev
libpq5 \  
&& pip install --upgrade pip \  
&& pip3 install --upgrade pip \  
&& cp /usr/share/postfix/main.cf.debian /etc/postfix/main.cf \  
&& echo LANG=en_US.UTF-8 >> /etc/default/locale \  
&& locale-gen en_US.UTF-8 \  
&& export LANG=en_US.UTF-8 \  
&& a2dismod status\  
&& a2dissite 000-default \  
&& a2enmod ssl \  
&& sed -i "s/max_execution_time = 30/max_execution_time = 300/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/memory_limit = 128M/memory_limit = 512M/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 50M/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/post_max_size = 8M/post_max_size = 50M/"
/etc/php/7.0/apache2/php.ini \  
&& cd /var/www \  
&& chown www-data:www-data /var/www \  
&& sudo -u www-data git clone https://github.com/MISP/MISP.git \  
&& cd /var/www/MISP \  
&& sudo -u www-data git checkout tags/$(git describe --tags `git rev-list
--tags --max-count=1`) \  
&& sudo -u www-data git config core.filemode false \  
&& cd /var/www/MISP/app/files/scripts \  
&& sudo -u www-data git clone https://github.com/CybOXProject/python-cybox.git
\  
&& sudo -u www-data git clone https://github.com/STIXProject/python-stix.git \  
&& sudo -u www-data git clone https://github.com/CybOXProject/mixbox.git \  
&& cd /var/www/MISP/app/files/scripts/python-cybox \  
&& sudo -u www-data git checkout v2.1.0.12 \  
&& python setup.py install \  
&& cd /var/www/MISP/app/files/scripts/python-stix \  
&& sudo -u www-data git checkout v1.1.1.4 \  
&& python setup.py install \  
&& cd /var/www/MISP/app/files/scripts/mixbox \  
&& sudo -u www-data git checkout v1.0.2 \  
&& python setup.py install \  
&& pip3 install stix2 \  
&& pip install pymisp \  
&& pip install python-magic \  
&& pip install pydeep \  
&& pip install lief \  
&& cd /var/www/MISP \  
&& sudo -u www-data git submodule init \  
&& sudo -u www-data git submodule update \  
&& cd /var/www/MISP/app \  
&& sudo -u www-data php composer.phar config vendor-dir Vendor \  
&& sudo -u www-data php composer.phar install \  
&& phpenmod redis \  
&& sudo -u www-data cp -fa /var/www/MISP/INSTALL/setup/config.php
/var/www/MISP/app/Plugin/CakeResque/Config/config.php \  
&& chown -R www-data:www-data /var/www/MISP \  
&& chmod -R 750 /var/www/MISP \  
&& chmod -R g+ws /var/www/MISP/app/tmp \  
&& chmod -R g+ws /var/www/MISP/app/files \  
&& chmod -R g+ws /var/www/MISP/app/files/scripts/tmp \  
&& cp /var/www/MISP/INSTALL/misp.logrotate /etc/logrotate.d/misp \  
&& echo "postfix postfix/main_mailer_type string Local only" | debconf-set-
selections \  
&& echo "postfix postfix/mailname string localhost.localdomain" | debconf-set-
selections \  
&& sed -i 's/^\\(daemonize\s*\\)yes\s*$/\1no/g' /etc/redis/redis.conf \  
&& pear install Crypt_GPG >>/tmp/install.log \  
&& pear install Net_GeoIP \  
&& cp /var/www/MISP/INSTALL/apache.misp.ubuntu /etc/apache2/sites-
available/misp.conf \  
&& cp /var/www/MISP/INSTALL/apache.24.misp.ssl /etc/apache2/sites-
available/misp-ssl.conf \  
&& a2dissite 000-default \  
&& a2ensite misp-ssl \  
&& a2enmod headers \  
&& a2enmod rewrite \  
&& sudo -u www-data cp -a /var/www/MISP/app/Config/bootstrap.default.php
/var/www/MISP/app/Config/bootstrap.php \  
&& sudo -u www-data cp -a /var/www/MISP/app/Config/database.default.php
/var/www/MISP/app/Config/database.php \  
&& sudo -u www-data cp -a /var/www/MISP/app/Config/core.default.php
/var/www/MISP/app/Config/core.php \  
&& sudo -u www-data cp -a /var/www/MISP/app/Config/config.default.php
/var/www/MISP/app/Config/config.php \  
&& chown -R www-data:www-data /var/www/MISP/app/Config \  
&& chmod -R 750 /var/www/MISP/app/Config \  
&& sed -i -E "s/'salt'\s=>\s'(\S+)'/'salt' => '`openssl rand -base64 32|tr "/"
"-"`'/" /var/www/MISP/app/Config/config.php \  
&& chmod a+x /var/www/MISP/app/Console/worker/start.sh \  
&& sed -i -E 's/^(\s*)system\\(\\);/\1unix-stream("\/dev\/log");/'
/etc/syslog-ng/syslog-ng.conf \  
&& cd /usr/local/src/ \  
&& sudo git clone https://github.com/MISP/misp-modules.git \  
&& cd misp-modules \  
&& pip3 install -I -r REQUIREMENTS \  
&& pip3 install -I . \  
&& chmod 0755 /run.sh \  
&& touch /.firstboot.tmp \  
&& pip install pyzmq \  
&& pip install redis \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
VOLUME /var/www/MISP  
EXPOSE 443  
ENTRYPOINT ["/run.sh"]  

