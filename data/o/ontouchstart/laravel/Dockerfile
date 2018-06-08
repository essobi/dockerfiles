From php:7  
RUN apt-get update  
RUN apt-get install -y git -y zlib1g-dev && docker-php-ext-install zip  
RUN cd /usr/local/bin && curl -sS
https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer
| php -- --filename=composer && chmod +x composer  
RUN composer global require "laravel/installer"  
RUN /root/.composer/vendor/bin/laravel --version  

