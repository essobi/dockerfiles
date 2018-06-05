FROM php:latest  
# Install modules  
RUN apt-get update && apt-get install -y \  
libicu-dev libicu-dev zlib1g-dev git mysql-client lftp nodejs npm ruby  
RUN gem install sass  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
RUN docker-php-ext-install intl mbstring zip pdo_mysql pdo  
RUN pecl install xdebug  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
CMD ["php"]  

