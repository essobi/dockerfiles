#################################################################  
# This docker image build file creates an image that contains  
# nginx, passenger, rvm with ruby on rails. It is intended for you  
# to use as a base for your project. Or as a template for your dockerfile.  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Component: docker-base  
# Author: peenuty <peenuty@gmail.com>  
#################################################################  
#####  
# Building: sudo docker build -t peenuty/rails-passenger-nginx .  
# Open it up: sudo docker run -t -i -p 80:80 bash -l  
FROM ubuntu:12.04  
MAINTAINER Richard Gill <richard@rgill.co.uk>  
  
# reduce output from debconf  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# Setup all needed dependencies  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install curl libcurl4-gnutls-dev git libxslt-dev libxml2-dev
libpq-dev libffi-dev imagemagick  
  
# Install rvm, ruby, rails, rubygems, passenger, nginx  
ENV RUBY_VERSION 2.1.0  
ENV RAILS_VERSION 4.0.0  
ENV PASSENGER_VERSION 4.0.37  
# All rvm commands need to be run as bash -l or they won't work.  
RUN \curl -sSL https://get.rvm.io | bash -s stable --rails  
RUN echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc  
RUN /bin/bash -l -c 'rvm requirements'  
RUN /bin/bash -l -c 'rvm install $RUBY_VERSION && rvm use $RUBY_VERSION
--default'  
RUN /bin/bash -l -c 'rvm rubygems current'  
  
RUN /bin/bash -l -c 'gem install passenger --version $PASSENGER_VERSION'  
RUN /bin/bash -l -c 'passenger-install-nginx-module --auto-download --auto
--prefix=/opt/nginx'  
  
RUN /bin/bash -l -c 'gem install bundler'  
RUN /bin/bash -l -c 'gem install rails --version=$RAILS_VERSION'  
  
#You need a javascript runtime to run rails  
RUN apt-get -y install nodejs  
  
RUN mkdir -p /var/log/nginx/  
  
# Just to make things safer.  
ENV RAILS_ENV development  
  
# You'll need to override the default nginx.conf with you're own.  
# I've provided a sample in the github project.  
#ADD local/path/to/nginx.conf /opt/nginx/conf/nginx.conf  
# You'll obviously want to expose some ports.  
#EXPOSE 22  
#EXPOSE 80  
#EXPOSE 443  

