FROM debian:jessie  
  
RUN \  
echo "deb http://www.deb-multimedia.org jessie main non-free" >
/etc/apt/sources.list.d/deb-multimedia.list \  
&& apt-get -y -q update \  
&& echo "deb https://packagecloud.io/phalcon/stable/debian/ jessie main" >
/etc/apt/sources.list.d/phalcon.list \  
&& echo "deb http://deb.antage.name jessie main" >
/etc/apt/sources.list.d/antage.list \  
&& echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y -q --no-install-recommends
--force-yes install apt-transport-https deb-multimedia-keyring curl ca-
certificates \  
&& curl -s http://deb.antage.name/apt.key | apt-key add - \  
&& curl -s https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& curl -s https://packagecloud.io/gpg.key | apt-key add - \  
&& apt-get -y -q update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y -q --no-install-recommends
install \  
curl \  
imagemagick \  
msmtp-mta \  
build-essential \  
php5-cli \  
php5-fpm \  
php5-mysql \  
php5-gd \  
php5-mcrypt \  
php5-curl \  
php5-memcache \  
php5-xsl \  
php5-xdebug \  
php5-intl \  
php5-xmlrpc \  
php5-apcu \  
php5-phalcon \  
php5-mongo \  
php5-amqp \  
php5 \  
php5-dev \  
php-pear \  
php5-dbg \  
gdb \  
ffmpeg \  
flvtool2 \  
ghostscript \  
wget \  
pngquant \  
mplayer \  
mencoder \  
newrelic-php5 \  
git \  
&& curl -#L
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
-o /tmp/ioncube.tar.gz \  
&& tar xzf /tmp/ioncube.tar.gz -C /tmp/ \  
&& install -m 0644 \  
/tmp/ioncube/ioncube_loader_lin_$(php -r 'printf("%s.%s", PHP_MAJOR_VERSION,
PHP_MINOR_VERSION);').so \  
$(php -r 'printf("%s", PHP_EXTENSION_DIR);')/ioncube_loader.so \  
&& rm -rf /tmp/ioncube \  
&& rm /tmp/ioncube.tar.gz \  
&& echo "; configuration for php ionCube loader module\n;
priority=00\nzend_extension=ioncube_loader.so" > /etc/php5/mods-
available/ioncube_loader.ini \  
&& /usr/bin/pear channel-discover pear.geometria-lab.net \  
&& /usr/bin/pear install geometria-lab/Rediska-beta \  
&& curl -#L
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 -o /usr/local/bin/confd \  
&& chmod 755 /usr/local/bin/confd \  
&& mkdir -p /etc/confd/conf.d \  
&& mkdir -p /etc/confd/templates \  
&& touch /etc/confd/confd.toml \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& rm -r /root/.gnupg/ \  
&& chmod +x /usr/local/bin/gosu \  
&& curl -o /usr/local/bin/composer
https://getcomposer.org/download/1.4.2/composer.phar \  
&& chown root:root /usr/local/bin/composer \  
&& chmod 0755 /usr/local/bin/composer \  
&& /usr/bin/pecl install redis \  
&& echo 'extension=redis.so' > /etc/php5/mods-available/redis.ini \  
&& apt-get --yes purge build-essential \  
&& apt-get --purge --yes autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm /var/log/dpkg.log  
  
RUN \  
rm /etc/php5/cli/conf.d/* \  
&& rm /etc/php5/fpm/conf.d/* \  
&& php5enmod -s ALL opcache \  
&& rm /var/run/newrelic-daemon.pid \  
&& mkdir /var/www \  
&& mkdir /var/log/php5-fpm  
  
EXPOSE 9000  
ENV LANG=C  
ENV PHP_FPM_RUN_USER www-data  
ENV PHP_FPM_RUN_GROUP www-data  
ENV PHP_FPM_MAX_WORKERS 32  
ENV PHP_FPM_MAX_REQUESTS 1024  
ENV PHP_FPM_COREDUMP ""  
ENV PHP_TIMEZONE UTC  
ENV PHP_MBSTRING_FUNC_OVERLOAD 0  
ENV PHP_NEWRELIC_LICENSE_KEY ""  
ENV PHP_NEWRELIC_APPNAME ""  
COPY .gdbinit /root/.gdbinit  
  
COPY opcache_bitrix.blacklist /etc/php5/opcache_bitrix.blacklist  
  
COPY confd/php.cli.toml /etc/confd/conf.d/  
COPY confd/templates/php.cli.ini.tmpl /etc/confd/templates/  
COPY confd/php.fpm.toml /etc/confd/conf.d/  
COPY confd/templates/php.fpm.ini.tmpl /etc/confd/templates/  
COPY confd/newrelic.toml /etc/confd/conf.d/  
COPY confd/templates/newrelic.ini.tmpl /etc/confd/templates/  
COPY confd/www.conf.toml /etc/confd/conf.d/  
COPY confd/templates/www.conf.tmpl /etc/confd/templates/  
RUN /usr/local/bin/confd -onetime -backend env  
COPY confd/msmtprc.toml /etc/confd/conf.d/  
COPY confd/templates/msmtprc.tmpl /etc/confd/templates/  
  
COPY php-fpm.conf /etc/php5/fpm/php-fpm.conf  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["php5-fpm"]  

