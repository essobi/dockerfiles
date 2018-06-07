FROM leandrosilva/php:7.1-apache  
  
MAINTAINER Leandro Silva <leandro@leandrosilva.info>  
  
COPY composer.json composer.lock /usr/local/ci/  
  
ENV COMPOSER_HOME /root/composer  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer  
VOLUME /root/composer/cache  
  
RUN apt-install libxslt-dev  
  
RUN docker-php-ext-install xsl  
  
RUN docker-php-ext-enable xdebug  
  
RUN rm -f /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini >/dev/null
2>/dev/null  
  
RUN composer install --prefer-dist -o -d /usr/local/ci  
  
RUN ln -s /usr/local/ci/vendor/bin/pdepend /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phpcbf /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phpcpd /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phpcs /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phpdox /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phploc /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phpmd /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phpunit /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phing /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/phpcb /usr/local/bin/ \  
&& ln -s /usr/local/ci/vendor/bin/codecept /usr/local/bin/  
  
RUN pdepend --version \  
&& phpcbf --version \  
&& phpcpd --version \  
&& phpcs --version \  
&& phpdox --version \  
&& phploc --version \  
&& phpmd --version \  
&& phpunit --version \  
&& phpcb --version \  
&& codecept --version \  
&& phing -v  
  

