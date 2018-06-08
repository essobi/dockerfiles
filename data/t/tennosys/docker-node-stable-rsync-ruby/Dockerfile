FROM node:8.9  
MAINTAINER abdulfattahikhsan "ikhsannetwork@gmail.com"  
RUN apt-get update && apt-get -y install \  
rsync \  
apt-utils \  
ruby-dev \  
rubygems  
RUN gem update --system  
RUN gem install sass --version "=3.3.7"  
RUN npm install -g gulp bower --quiet  

