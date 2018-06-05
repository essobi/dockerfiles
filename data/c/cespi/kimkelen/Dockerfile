FROM php:5.4-apache  
MAINTAINER chrodriguez <chrodriguez@gmail.com>  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
&& docker-php-ext-install iconv mcrypt xsl mysqli \  
&& docker-php-ext-configure mysqli --with-mysqli=mysqlnd --with-pdo-
mysql=mysqlnd --with-mysql=mysqlnd \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd mysqli pdo_mysql  
  
# git cli  
RUN apt-get update && apt-get install -y git-core && rm -rf
/var/lib/apt/lists/*  
  
# mysql-client  
RUN apt-get update && apt-get install -y mysql-client && rm -rf
/var/lib/apt/lists/*  
  
# Default GIT information  
ENV GIT_REPO https://github.com/Desarrollo-CeSPI/kimkelen.git  
ENV GIT_REVISION master  
  
# Upload default configurations  
RUN mkdir /default_configs  
  
COPY sample-app.yml /default_configs/app.yml  
COPY sample-php.ini /default_configs/php.ini  
COPY sample-databases.yml /default_configs/databases.yml  
COPY sample-propel.ini /default_configs/propel.ini  
  
# Enable apache rewrite module  
RUN a2enmod rewrite  
  
VOLUME ["/code", "/data"]  
  
COPY kimkelen-start /usr/local/bin/  
  
EXPOSE 80  
ENTRYPOINT ["kimkelen-start"]  

