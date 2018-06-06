FROM phusion/baseimage:0.9.15  
MAINTAINER Peter Yates <peter.yates@capita.co.uk>  
  
# Set the locale and timezone  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE en_GB:en  
ENV LC_ALL en_GB.UTF-8  
RUN echo Europe/London > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN apt-get update  
RUN apt-get install -y build-essential libpq-dev libssl-dev curl git libssl-
dev libgeos-3.4.2 libgeos-dev nodejs-legacy imagemagick libreadline-dev
libxml2-dev npm libmagickwand-dev libsqlite3-dev ruby2.3 ruby2.3-dev  
  
# Create a generic libgeos.so symlink pointing at our installed version  
RUN ln -s /usr/lib/libgeos-3.4.2.so /usr/lib/libgeos.so  
  
# Install bundler gem  
RUN gem install bundler  
  
# Install the bower javascript package manager  
RUN npm -g install bower phantomjs-prebuilt  
  
ENV APP_HOME /lbs  

