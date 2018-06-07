FROM php:7.1-fpm  
MAINTAINER Craig Johnston <cjimti@gmail.com>  
  
# utils, dev libs and node  
RUN apt-get update \  
&& apt-get install -y git net-tools wget \  
autoconf libssl-dev zlib1g-dev libicu-dev g++ make cmake libuv-dev libgmp-dev
uuid-dev \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
-y nodejs  
  
# node packages and gems  
RUN apt-get install -y ruby-full \  
&& npm install -g bower webpack newman create-react-app \  
&& curl -o- -L https://yarnpkg.com/install.sh | bash \  
&& gem install sass \  
&& /root/.yarn/bin/yarn global add @angular/cli  
  
# datastax php-driver fox cassandra  
RUN git clone https://github.com/datastax/php-driver.git /usr/src/datastax-
php-driver \  
&& cd /usr/src/datastax-php-driver \  
&& git checkout --detach v1.2.2 \  
&& git submodule update --init \  
&& cd ext \  
&& ./install.sh \  
&& echo "extension=cassandra.so" > /usr/local/etc/php/conf.d/cassandra.ini  
  
## PHP extensions  
RUN docker-php-ext-install zip mbstring intl opcache bcmath \  
&& echo extension=bcmath.so > /usr/local/etc/php/conf.d/docker-php-ext-
bcmath.ini \  
&& pecl install xdebug \  
&& echo zend_extension=xdebug.so > /usr/local/etc/php/conf.d/xdebug.ini \  
&& pecl install apcu-5.1.5 \  
&& echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini \  
&& pecl install uuid \  
&& echo extension=uuid.so > /usr/local/etc/php/conf.d/uuid.ini  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer  
  
RUN wget https://github.com/Behat/Behat/releases/download/v3.3.0/behat.phar \  
&& mv behat.phar /usr/bin/behat \  
&& chmod ug+x /usr/bin/behat  
  
RUN wget https://phar.phpunit.de/phpunit-6.2.phar \  
&& mv phpunit-6.2.phar /usr/bin/phpunit \  
&& chmod ug+x /usr/bin/phpunit  
  
# python, pip and cqlsh  
RUN apt-get install gcc libev4 libev-dev build-essential python-dev python-
setuptools python-pip python-wheel -y  
  
# cqlsh  
RUN pip install cqlsh  
  
COPY ./files/MOTD.txt /root/MOTD.txt  
  
COPY ./files/bashrc /root/.bashrc  
  
WORKDIR /app  

