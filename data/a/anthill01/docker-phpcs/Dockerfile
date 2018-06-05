FROM php:7.1  
  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
libicu-dev \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install zip intl  
  
COPY files/symfony-coding-standard /opt/symfony-coding-standard  
  
# COMPOSER #  
  
WORKDIR /usr/local/bin  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \--filename=composer \  
&& rm composer-setup.php \  
&& curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& mv phpcs.phar /usr/local/bin/phpcs \  
&& chmod a+x /usr/local/bin/phpcs \  
&& curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& mv phpcbf.phar /usr/local/bin/phpcbf \  
&& chmod a+x /usr/local/bin/phpcbf \  
&& phpcs \--config-set installed_paths /opt/symfony-coding-standard \  
&& curl -OL http://static.phpmd.org/php/latest/phpmd.phar \  
&& mv phpmd.phar /usr/local/bin/phpmd \  
&& chmod a+x /usr/local/bin/phpmd \  
&& curl -L http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar -o php-cs-
fixer.phar \  
&& mv php-cs-fixer.phar /usr/local/bin/php-cs-fixer \  
&& chmod a+x /usr/local/bin/php-cs-fixer  
  
# OTHER #  
  
WORKDIR /var/www/  

