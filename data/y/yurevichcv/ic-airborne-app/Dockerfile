FROM maxexcloo/nginx-php:latest  
  
MAINTAINER Constantine Yurevich <constantine.yurevich@designtech.se>  
  
# Remove root directive from /etc/nginx/host.d/default.conf  
RUN sed -i '/root/d' /etc/nginx/host.d/default.conf  
  
# Remove unnecessary config file  
RUN rm /etc/nginx/conf.d/02cache.conf  
  
# Install PHP extensions  
RUN apt-get update  
RUN apt-get install -y php5-apcu  
  
# Intall MySQL client  
RUN apt-get install -y mysql-client  
  
# Install NodeJS & Grunt  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g grunt-cli  
  
# Install Git  
RUN apt-get install -y git  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
WORKDIR /data/http  
  
ENV HOME /root  
  
# Deploy iCoordinator App  
CMD npm install && grunt deploy && /config/loop

