FROM ridibooks/php:7.1-base  
MAINTAINER Koong Kyungmi <kyungmi@ridi.com>  
  
# Install packages  
RUN apt-get update && \  
  
# Common  
apt-get install -y git wget software-properties-common python python-dev
psmisc netcat && \  
  
# For PHP zip extension  
apt-get install -y zlib1g-dev && \  
  
# For Cassandra php-driver  
apt-get install -y g++ make cmake libssl-dev libgmp-dev openssl libpcre3-dev
&& \  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/dependencies/libuv/v1.18.0/libuv_1.18.0-1_amd64.deb && \  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/dependencies/libuv/v1.18.0/libuv-dev_1.18.0-1_amd64.deb &&
\  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/cassandra/v2.8.1/cassandra-cpp-driver_2.8.1-1_amd64.deb &&
\  
wget http://downloads.datastax.com/cpp-
driver/ubuntu/16.04/cassandra/v2.8.1/cassandra-cpp-driver-
dev_2.8.1-1_amd64.deb && \  
dpkg -i libuv_1.18.0-1_amd64.deb && \  
dpkg -i libuv-dev_1.18.0-1_amd64.deb && \  
dpkg -i cassandra-cpp-driver_2.8.1-1_amd64.deb && \  
dpkg -i cassandra-cpp-driver-dev_2.8.1-1_amd64.deb && \  
  
apt-get autoclean -y && \  
apt-get clean -y  
  
# Install pip  
RUN wget https://bootstrap.pypa.io/get-pip.py && chmod +x get-pip.py && python
get-pip.py  
  
# Install Cassandra client  
RUN pip install cqlsh  
  
# PHP zip extension is required so Composer can use packages from dist  
RUN docker-php-ext-install zip  
  
# Install xDebug for coverage  
RUN pecl install xdebug && \  
docker-php-ext-enable xdebug  
  
# Install mysql driver  
RUN docker-php-ext-install pdo_mysql  
  
# Install datastax php-driver for Cassandra  
RUN pecl install cassandra && \  
docker-php-ext-enable cassandra  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer  
  
# Install Node  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
# Install newman (Postman test runner)  
RUN npm install newman --global  

