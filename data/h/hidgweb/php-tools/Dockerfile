FROM alpine:3.7  
  
ENV PHPUNIT_VERSION 6.5.0  
ENV PHPUNIT_CODE_COVERAGE_VERSION ~5  
ENV DRUSH_VERSION 8.0.0  
ENV TERMINUS_PLUGINS_DIR /tools/terminus/plugins  
ENV TERMINUS_CACHE_DIR /tools/terminus/cache  
ENV SIMPLETEST_DB sqlite://tmp/site.sqlite  
  
RUN apk add --no-cache wget ca-certificates \  
&& wget -O /etc/apk/keys/phpearth.rsa.pub
https://repos.php.earth/alpine/phpearth.rsa.pub \  
&& echo "https://repos.php.earth/alpine/v3.7" >> /etc/apk/repositories \  
&& apk add --no-cache build-base autoconf --virtual .build-deps \  
&& apk add --no-cache \  
curl \  
git \  
openssh-client \  
php7.2 \  
php7.2-fpm \  
php7.2-opcache \  
php7.2-curl \  
php7.2-bcmath \  
php7.2-bz2 \  
php7.2-calendar \  
php7.2-ctype \  
php7.2-dba \  
php7.2-dom \  
php7.2-exif \  
php7.2-gd \  
php7.2-gettext \  
php7.2-gmp \  
php7.2-iconv \  
php7.2-json \  
php7.2-ldap \  
php7.2-mbstring \  
php7.2-mcrypt \  
php7.2-memcached \  
php7.2-mysqli \  
php7.2-mysqlnd \  
php7.2-openssl \  
php7.2-pcntl \  
php7.2-pdo \  
php7.2-pdo_mysql \  
php7.2-pdo_sqlite \  
php7.2-pear \  
php7.2-phar \  
php7.2-posix \  
php7.2-session \  
php7.2-shmop \  
php7.2-simplexml \  
php7.2-soap \  
php7.2-sockets \  
php7.2-sqlite3 \  
php7.2-sysvmsg \  
php7.2-sysvsem \  
php7.2-sysvshm \  
php7.2-tokenizer \  
php7.2-wddx \  
php7.2-xdebug \  
php7.2-xml \  
php7.2-xmlreader \  
php7.2-xmlwriter \  
php7.2-xsl \  
php7.2-zip \  
php7.2-zlib \  
rsync \  
&& mkdir /composer \  
&& curl --silent --show-error https://getcomposer.org/installer | php --
--install-dir=/usr/local/bin --filename=composer  
  
COPY ./build-tools-ci.sh /scripts/  
  
RUN mkdir -p ${TERMINUS_PLUGINS_DIR} ${TERMINUS_CACHE_DIR} \  
&& composer -n global require -n hirak/prestissimo:^0.3 \  
&& mkdir -p /tools/drupal \  
&& cd /tools/drupal \  
&& composer -n require drush/drush ^${DRUSH_VERSION} \  
&& composer -n require drupal/coder \  
&& /tools/drupal/vendor/bin/phpcs --config-set installed_paths
/tools/drupal/vendor/drupal/coder/coder_sniffer \  
&& mkdir -p /tools/drupalconsole \  
&& cd /tools/drupalconsole \  
&& composer require drupal/console \  
&& mkdir -p /tools/php \  
&& cd /tools/php \  
&& composer -n require phpmd/phpmd \  
&& composer -n require sebastian/phpcpd \  
&& composer -n require phing/phing \  
&& mkdir -p /tools/phpunit \  
&& cd /tools/phpunit \  
&& composer -n require phpunit/php-code-coverage
${PHPUNIT_CODE_COVERAGE_VERSION} \  
&& composer -n require phpunit/phpunit ^${PHPUNIT_VERSION} \  
&& mkdir -p /tools/terminus \  
&& cd /tools/terminus \  
&& composer -n require pantheon-systems/terminus \  
&& composer create-project -n -d ${TERMINUS_PLUGINS_DIR} pantheon-
systems/terminus-build-tools-plugin:~1 \  
&& ls /tools/ | while read tool; do \  
ls /tools/$tool/vendor/bin/ | while read binary; do \  
rm -f /usr/local/bin/$binary; \  
ln -s /tools/$tool/vendor/bin/$binary /usr/local/bin; \  
done; \  
done \  
&& touch ${HOME}/.bash_profile \  
&& curl --silent --show-error https://platform.sh/cli/installer | php \  
&& mv ${HOME}/.platformsh /tools/platformsh \  
&& ln -s /tools/platformsh/bin/platform /usr/local/bin \  
&& chmod +x /scripts/build-tools-ci.sh \  
&& mkdir -p /tools/phpdocumentor \  
&& cd /tools/phpdocumentor \  
&& composer require phpdocumentor/phpdocumentor \  
&& mkdir -p /tools/codeception \  
&& cd /tools/codeception \  
&& composer require codeception/codeception \  
&& apk del .build-deps \  
&& mkdir -p /tools/drupal/vendor/drupal/coder/coder_sniffer/DrupalAll  
  
COPY phpcs-rules/DrupalAll-ruleset.xml
/tools/drupal/vendor/drupal/coder/coder_sniffer/DrupalAll/ruleset.xml  
  
RUN logfile="/version.txt" \  
&& > $logfile \  
&& php --version | sed -ne 's/^\(PHP [^ ]\+\) .*/\1/gp' >> $logfile \  
&& pecl list | tail -n +4 >> $logfile \  
&& composer --version >> $logfile \  
&& /tools/drupal/vendor/bin/drush --version >> $logfile \  
&& /tools/drupal/vendor/bin/phpcs --version >> $logfile \  
&& /tools/drupal/vendor/bin/phpcs -i >> $logfile \  
&& composer -d/tools/drupalconsole show | grep drupal | head -n 1 >> $logfile
\  
&& /tools/php/vendor/bin/phpmd --version >> $logfile \  
&& /tools/php/vendor/bin/phing -v >> $logfile \  
&& /tools/php/vendor/bin/phpcpd --version >> $logfile \  
&& /tools/phpunit/vendor/bin/phpunit --version >> $logfile \  
&& /tools/phpdocumentor/vendor/bin/phpdoc --version >> $logfile \  
&& /tools/codeception/vendor/bin/codecept --version >> $logfile \  
&& terminus --version >> $logfile \  
&& platform --version >> $logfile  
  
WORKDIR /app  
  
CMD ["phpcs", "--standard=Drupal,DrupalPractice", "."]  

