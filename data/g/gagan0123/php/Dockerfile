FROM tetraweb/php:7.1  
MAINTAINER Gagan Deep Singh <me@gagan.pro>  
  
RUN apt-get clean  
RUN apt-get -yqq update  
RUN apt-get -yqqf install zip unzip subversion mysql-client libmysqlclient-dev
--fix-missing  
RUN docker-php-ext-enable mbstring mcrypt mysqli pdo_mysql intl gd zip bz2  
RUN curl -sSLo phpunit.phar https://phar.phpunit.de/phpunit-5.7.phar && chmod
755 phpunit.phar && mv phpunit.phar /usr/local/bin/ && rm
/usr/local/bin/phpunit && ln -s /usr/local/bin/phpunit.phar
/usr/local/bin/phpunit  
RUN composer global require "wp-coding-standards/wpcs"  
RUN phpcs --config-set installed_paths $HOME/.composer/vendor/wp-coding-
standards/wpcs  

