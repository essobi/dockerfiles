FROM ubuntu:14.04  
MAINTAINER Joey Hallie <joey@fixico.nl>  
  
RUN apt-key update -y  
RUN apt-get install software-properties-common curl -y  
RUN add-apt-repository ppa:ondrej/php5-5.6  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
  
RUN apt-get update -y  
RUN apt-get install nodejs -y  
RUN apt-get install php5 curl php5-curl php5-mcrypt git ssh -y --force-yes  
  
RUN npm install gulp grunt-cli bower -g  
RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-
dir=/usr/local/bin --filename=composer  

