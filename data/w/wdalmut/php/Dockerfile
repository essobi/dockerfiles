FROM php:5.6  
WORKDIR /tmp  
  
RUN apt-get update && apt-get install -y socat build-essential libicu-dev git
curl \  
libcurl4-openssl-dev zlib1g-dev libxslt1-dev libxml2-dev && rm -rf
/var/lib/apt/lists/*  
RUN curl https://pecl.php.net/get/mongo-1.5.8.tgz > /tmp/mongo.tgz  
RUN tar -xpzf mongo.tgz  
RUN mv /tmp/mongo-1.5.8 /usr/src/php/ext  
  
RUN docker-php-ext-install sockets  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install xmlrpc  
RUN docker-php-ext-install xsl  
RUN docker-php-ext-install mongo-1.5.8  
RUN docker-php-ext-install mysql  
RUN docker-php-ext-install pdo_mysql  
  
WORKDIR /usr/local/bin  
RUN curl -sS https://getcomposer.org/installer | php  
RUN chmod a+x composer.phar  
RUN mv composer.phar composer  
  
RUN sed -i -e 's/# StrictHostKeyChecking ask/StrictHostKeyChecking no/g'
/etc/ssh/ssh_config  
  
CMD ["php", "-v"]  

