FROM ubuntu:latest  
  
# Update Ubuntu  
RUN apt-get -y update --fix-missing  
  
# Install Required Libraries  
RUN apt-get -y install \  
software-properties-common \  
language-pack-en-base  
  
# Install PHP 5.6 and NodeJS  
RUN apt-get -y install \  
php7.0 \  
php7.0-cli \  
nodejs \  
nodejs-legacy \  
npm  
  
# Install Testing Frameworks  
RUN npm -g install jshint  
  
# Show Environment Setup  
RUN cat /etc/lsb-release  
RUN php -v  
RUN npm -v  
  
CMD ["/run.sh"]  

