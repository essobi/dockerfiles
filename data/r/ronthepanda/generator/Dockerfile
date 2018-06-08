# Base  
FROM phusion/baseimage  
  
# Maintainer  
MAINTAINER Ron Hoffmann <ronhoffmannn@gmail.com>  
  
# Update source list and install dependencies  
RUN apt-get update && apt-get install -y curl  
  
# Install NodeJS and NPM  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash - \  
&& apt-get install -y nodejs  
  
# Install MeteorJS  
RUN curl https://install.meteor.com/ | sh  
  
VOLUME /app  
WORKDIR /app  
  
ADD . /app  
  
EXPOSE 3000

