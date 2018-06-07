FROM php:7.2-cli  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV BUILD_DEPS="autoconf file g++ gcc libc-dev make pkg-config re2c"  
ENV LIB_DEPS="zlib1g-dev"  
ENV ICU_RELEASE=61.1  
ENV CXXFLAGS "--std=c++0x"  
RUN apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS
$LIB_DEPS && rm -rf /var/lib/apt/lists/* \  
&& echo "date.timezone=Europe/Warsaw" >> $PHP_INI_DIR/php.ini \  
&& docker-php-ext-install zip \  
&& cd /tmp && curl -Ls http://download.icu-
project.org/files/icu4c/$ICU_RELEASE/icu4c-$(echo $ICU_RELEASE | tr '.'
'_')-src.tgz > icu4c-src.tgz \  
&& cd /tmp && tar xzf icu4c-src.tgz && cd /tmp/icu/source && sed -i''
's/define U_USING_ICU_NAMESPACE 0/define U_USING_ICU_NAMESPACE 1/g'
common/unicode/uversion.h && ./configure && make && make install && rm -rf
/tmp/icu /tmp/icu4c-src.tgz \  
&& docker-php-ext-configure intl && docker-php-ext-install intl \  
&& curl -Ls https://getcomposer.org/composer.phar > /usr/local/bin/composer &&
chmod +x /usr/local/bin/composer \  
&& apt-get purge -y --auto-remove $BUILD_DEPS  
  
CMD icu-config --version && php -i | grep 'ICU version'  

