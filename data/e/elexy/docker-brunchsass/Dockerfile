  
# use the nodejs base image provided by docker  
FROM dockerfile/nodejs  
MAINTAINER Alex Knol, alexknol@gmail.com  
  
# make sure the package repo is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get upgrade  
RUN apt-get update  
  
RUN apt-get install git ruby1.9.3 -y  
RUN gem install sass  
  
# Update npm and install node packages  
RUN npm -g update npm  
RUN npm install -g brunch  
  
RUN mkdir /var/www

