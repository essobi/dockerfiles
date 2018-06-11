FROM openjdk:8-jdk  
MAINTAINER Lucas <lg@wb7.eu>  
  
# update package lists  
RUN apt-get update && apt-get upgrade -y  
  
# install curl  
RUN apt-get install -y curl wget  
  
# add nodejs repo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# install nodejs  
RUN apt-get install -y nodejs  
  
# maybe you need this for building something  
RUN apt-get install -y build-essential  

