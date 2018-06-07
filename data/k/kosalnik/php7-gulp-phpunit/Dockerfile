# PHPUnit Docker Container.  
FROM ubuntu:16.04  
MAINTAINER Alexandr Kosygin <kosalnik@gmail.com>  
  
# Run some Debian packages installation.  
ENV PACKAGES="php7.0 php7.0-curl php7.0-mcrypt php7.0-mbstring php7.0-mysql
php7.0-xml php7.0-zip curl git apt-utils ca-certificates"  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends $PACKAGES \  
&& update-ca-certificates \  
&& curl -L https://deb.nodesource.com/setup_6.x -o /tmp/setup \  
&& chmod o+x /tmp/setup \  
&& /tmp/setup \  
&& apt-get install -y nodejs \  
&& npm install -g gulp-cli \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Goto temporary directory.  
WORKDIR /tmp  
  
# Run php composer installation  
RUN curl -sL https://getcomposer.org/installer | php \  
&& mv ./composer.phar /usr/local/bin/composer  
  
# Run PHPUnit installation  
# Возможно PHPUnit тут вообще не нужен. Т.к. он есть в зависимостях проекта
vendor/bin/phpunit  
#RUN composer selfupdate \  
# && composer require "phpunit/phpunit:~5.4.2" --prefer-source --no-
interaction \  
# && ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit  
# Set up the application directory.  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set up the command arguments.  
#ENTRYPOINT ["/usr/local/bin/phpunit"]  
#CMD ["--help"]  

