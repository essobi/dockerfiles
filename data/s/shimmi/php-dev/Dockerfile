FROM shimmi/php:7.2-zts  
  
LABEL maintainer="Jiří Šimeček <jirka@simecek.org>"  
  
RUN pecl install xdebug \  
&& apt-get install -y libxslt-dev \  
&& docker-php-ext-install xsl  
  
RUN composer global require \  
"squizlabs/php_codesniffer=*" \  
"pdepend/pdepend=*" \  
"phpmd/phpmd=@stable" \  
'behat/behat=*' \  
"phpunit/phpunit=*" \  
"phploc/phploc=*" \  
"sebastian/phpcpd=*" \  
"theseer/phpdox=*"  
  
# Make Composer binaries/tools reachable  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/conf.d /usr/local/etc/php/conf.d  

