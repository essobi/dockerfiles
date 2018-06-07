FROM php:7.1-cli  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
openjdk-7-jdk \  
libpng12-dev \  
libjpeg-dev \  
mysql-client \  
vim \  
ant \  
git \  
rsync \  
unzip \  
python \  
wget \  
curl \  
netcat-openbsd \  
libfreetype6-dev \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure gd --with-jpeg-dir=/usr/lib --with-freetype-
dir=/usr/include \  
&& docker-php-ext-install pdo pdo_mysql mbstring gd zip  
  
COPY shopware.ini /usr/local/etc/php/conf.d/shopware.ini  
  
COPY login_shopware.cnf /tmp/login_shopware.cnf  
COPY wait_with_login_shopware.sh /tmp/wait_with_login_shopware.sh  
COPY wait.sh /tmp/wait.sh  
RUN chmod +x /tmp/wait.sh && chmod +x /tmp/wait_with_login_shopware.sh  
  
COPY wait-elasticsearch.sh /tmp/wait-elasticsearch.sh  
RUN chmod +x /tmp/wait-elasticsearch.sh  
  
WORKDIR /var/www/html  

