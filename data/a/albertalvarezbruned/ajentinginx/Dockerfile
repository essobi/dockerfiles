FROM debian:latest  
MAINTAINER Albert Alvarez <albert@alvarezbruned.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y  
RUN apt-get install -y \  
sudo \  
nano \  
wget \  
curl \  
openssh-client  
  
RUN rm /var/lib/apt/lists/*gz  
RUN apt-get -o Acquire::GzipIndexes=false update  
  
RUN wget http://repo.ajenti.org/debian/key -O- | apt-key add -  
RUN echo "deb http://repo.ajenti.org/debian main main debian" >>
/etc/apt/sources.list  
  
RUN apt-get update -y  
RUN apt-get install -y -f ajenti  
RUN apt-get install -y ajenti-v ajenti-v-nginx ajenti-v-php-fpm php5-mysql
php5-memcached php5-mcrypt php5-gd php5-sqlite php5-pgsql php5-xdebug
php5-json  
RUN apt-get install -y php5-mysqlnd  
  
RUN echo "www-data ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
RUN wget https://getcomposer.org/download/1.1.1/composer.phar && mv
composer.phar /usr/local/bin/composer && chmod +x /usr/local/bin/composer  
RUN wget https://phar.phpunit.de/phpunit-library-5.3.5.phar && mv phpunit-
library-5.3.5.phar /usr/local/bin/phpunit && chmod +x /usr/local/bin/phpunit  
  
WORKDIR /srv  
  
RUN apt-get install -y php5-curl  
RUN rm /etc/ajenti/config.json  
COPY ./src/config.json /etc/ajenti/config.json  
COPY ./src/vh.json /etc/ajenti/vh.json  
RUN echo "xdebug.max_nesting_level=500" >> /etc/php5/mods-available/xdebug.ini  
  
RUN apt-get install -y git  
RUN wget
https://nodejs.org/download/release/v4.4.4/node-v4.4.4-linux-x64.tar.gz  
RUN tar -C /usr/local \--strip-components 1 -xzf node-v4.4.4-linux-x64.tar.gz  
RUN npm -g install npm  
RUN npm -g install gulp-cli  
RUN npm -g install coffee-script  
RUN npm -g install bower  
RUN php5dismod xdebug  
  
COPY ./src/startup.sh /root/startup.sh  
RUN chmod +x /root/startup.sh  
  
EXPOSE 80 8000 443  
CMD sh /root/startup.sh  

