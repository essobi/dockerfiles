FROM php:7.1-cli  
  
ADD php/php.ini /usr/local/etc/php/php.ini  
  
# Add 10gen official apt source to the sources list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5  
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.6 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.6.list  
# Install MongoDB and dependencies for intl and zip extensions  
RUN apt-get update && apt-get upgrade -y && apt-get install -y mongodb-org
libicu-dev g++ sudo zlib1g-dev git libssl-dev wget apt-transport-https  
  
RUN echo "y\ny" | pecl install apcu  
ADD php/apcu.ini /usr/local/etc/php/conf.d/apcu.ini  
RUN docker-php-ext-install bcmath mbstring opcache intl pcntl zip  
RUN pecl install mongodb-1.4.3  
ADD php/mongodb.ini /usr/local/etc/php/conf.d/mongodb.ini  
  
# install composer  
RUN cd /usr/local/bin/ && curl -sS https://getcomposer.org/installer | php  
  
# This dockerfile is ugly with so many dependencies. Next time, we will use
docker compose  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-
key add - && \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | tee -a
/etc/apt/sources.list.d/elastic-5.x.list && \  
echo "deb http://http.debian.net/debian jessie-backports main" | tee --append
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && \  
apt-get install -y -t jessie-backports openjdk-8-jre-headless && \  
apt-get install --no-install-recommends -y elasticsearch && \  
/usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu && \  
/usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-stempel  
  
# Compact docker  
RUN apt-get clean -y && rm -rf /tmp/pear/* && rm -rf /var/lib/apt/lists/*  
  
ADD sudo/sudoers /etc/sudoers  
  
CMD /usr/bin/mongod --smallfiles --dbpath /var/lib/mongodb/ --replSet rs1
--logpath /var/log/mongodb/mongodb.log --fork && \  
/usr/bin/mongo --eval 'rs.initiate();' && \  
/data/bin/phpunit -c /data/app/  

