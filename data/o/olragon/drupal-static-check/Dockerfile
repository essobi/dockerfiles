FROM php:7-cli  
MAINTAINER Long Nguyen <olragon@gmail.com>  
  
RUN apt-get update && apt-get install -y git curl zip unzip  
RUN echo "date.timezone = UTC" >> /usr/local/etc/php/php.ini  
RUN echo "memory_limit = -1" >> /usr/local/etc/php/php.ini  
  
RUN php -r "readfile('https://getcomposer.org/installer');" | php  
RUN chmod +x composer.phar  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar  
RUN chmod +x phpcs.phar  
RUN mv phpcs.phar /usr/local/bin/phpcs  
  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar  
RUN chmod +x phpcbf.phar  
RUN mv phpcbf.phar /usr/local/bin/phpcbf  
  
RUN composer global require drupal/coder  
RUN phpcs --config-set installed_paths
~/.composer/vendor/drupal/coder/coder_sniffer  

