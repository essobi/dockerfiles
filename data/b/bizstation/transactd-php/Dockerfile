FROM php:7.1  
  
ENV PHP_VERSION 7.1  
ENV TRANSACTD_VERSION 3.7.2  
ENV TRANSACTD_MD5 2589bfe9759504733dfed75ebbd158b9  
ENV PHPUNIT_VERSION 5.7.13  
ENV PHPUNIT_SHA256
97082bd398e34c5886550f01059a9b522286d905dd5b00c26e680560fac04632  
  
ENV INSTALL_PREFIX /usr/lib/  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y wget \  
&& wget -O tdclphp.tar.gz
http://www.bizstation.jp/al/transactd/download/docker/transactd_client_${TRANSACTD_VERSION}_php.tar.gz
\  
&& echo "${TRANSACTD_MD5} tdclphp.tar.gz" | md5sum -c - \  
&& tar xfz tdclphp.tar.gz \  
&& rm -f tdclphp.tar.gz \  
\  
&& cp
transactd_client_${TRANSACTD_VERSION}_php/bin/${PHP_VERSION}/libtdclc_64.so.3.7
${INSTALL_PREFIX}/ \  
&& cp
transactd_client_${TRANSACTD_VERSION}_php/bin/${PHP_VERSION}/libtdclcpp_64m.so.3.7
${INSTALL_PREFIX}/ \  
\  
&& PHP_EXTENSION_DIR=`php -i | grep extension_dir | grep -v
sqlite3.extension_dir | sed "s/.* => //g"` \  
&& echo ${PHP_EXTENSION_DIR}/php_transactd.so \  
&& cp
transactd_client_${TRANSACTD_VERSION}_php/bin/${PHP_VERSION}/php_transactd.so
${PHP_EXTENSION_DIR}/ \  
\  
&& PHP_INCLUDE_PATH=`php -i | grep include_path | sed "s/.* => //g" | sed
"s/.*://g"` \  
&& echo ${PHP_INCLUDE_PATH}/transactd.php \  
&& cp
transactd_client_${TRANSACTD_VERSION}_php/bin/${PHP_VERSION}/transactd.php
${PHP_INCLUDE_PATH}/ \  
\  
&& PHP_INI_DIR=`php -i | grep "Scan this dir for additional .ini files" | sed
"s/.* => //g"` \  
&& echo ${PHP_INI_DIR}/php_transactd.ini \  
&& echo "extension=php_transactd.so" > ${PHP_INI_DIR}/php_transactd.ini \  
\  
&& cd transactd_client_${TRANSACTD_VERSION}_php/tests \  
&& wget -O phpunit.phar
https://phar.phpunit.de/phpunit-${PHPUNIT_VERSION}.phar \  
&& echo "${PHPUNIT_SHA256} phpunit.phar" | sha256sum -c - \  
&& chmod +x phpunit.phar \  
\  
&& apt-get purge -y --auto-remove wget \  
&& rm -rf /var/lib/apt/lists/*  

