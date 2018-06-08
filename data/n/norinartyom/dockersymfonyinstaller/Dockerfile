FROM ubuntu:16.04  
MAINTAINER artyom.norin@gmail.com  
  
WORKDIR /home  
  
#install curl  
RUN apt-get -qq update  
RUN apt-get -qq -y install curl  
  
#install php cli  
RUN apt-get -qq -y install php7.0-cli  
  
#install symfony installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony  
RUN chmod a+x /usr/local/bin/symfony  

