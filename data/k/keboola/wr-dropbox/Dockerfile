# VERSION 1.1.3  
FROM php:7.1  
MAINTAINER Ondrej Vana <ondrej.vana@keboola.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Dependencies  
RUN apt-get update \  
&& apt-get install unzip git unixODBC-dev libpq-dev -y  
  
# install composer  
RUN cd \  
&& curl -sS https://getcomposer.org/installer | php \  
&& ln -s /root/composer.phar /usr/local/bin/composer  
  
WORKDIR /home  
  
# Initialize  
RUN git clone -b 0.2.1 --depth 1 https://github.com/keboola/dropbox-writer.git
./  
RUN composer self-update  
RUN composer install --no-interaction  
  
ENTRYPOINT php ./src/run.php --data=/data  

