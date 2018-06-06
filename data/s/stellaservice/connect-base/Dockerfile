FROM ruby:2.3.1  
MAINTAINER Greg Taschuk  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq  
RUN apt-get install -qq -y software-properties-common build-essential libpq-
dev g++ zip less  
  
#### PhantomJS & Capybara-webkit dependencies needed for testing ####  
RUN apt-get install -qq -y qt5-default libqt5webkit5-dev gstreamer1.0-plugins-
base gstreamer1.0-tools gstreamer1.0-x xvfb default-jre default-jdk  
RUN mkdir -p phantomjs-2.0.0-ubuntu-14.04  
ADD https://s3.amazonaws.com/travis-
phantomjs/phantomjs-2.0.0-ubuntu-14.04.tar.bz2 /  
RUN tar jxvf phantomjs-2.0.0-ubuntu-14.04.tar.bz2  
RUN cp phantomjs /usr/local/bin/.  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
-qq -y nodejs  
RUN npm install -g bower  
RUN npm install -g yarn  

