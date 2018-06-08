FROM google/cloud-sdk:latest  
  
# Fix frontend not set error  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Install deploy tools and PHP  
RUN apt-get -y update && apt-get -y install curl git gettext apt-utils build-
essential php5-cli  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin  
RUN mv /usr/local/bin/composer.phar /usr/local/bin/composer  

