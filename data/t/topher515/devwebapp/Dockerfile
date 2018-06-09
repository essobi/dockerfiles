FROM debian:wheezy  
  
MAINTAINER Chris Wilcox <ckwilcox@gmail.com>  
  
  
WORKDIR /opt/app  
  
RUN apt-get update  
RUN apt-get install -y libxslt-dev libxml2-dev  
RUN apt-get -y install python python-dev python-pip build-essential git  
RUN apt-get -y install curl  
  
# Web app  
RUN pip install Flask sqlalchemy  
  
# Development  
# Build  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get -y install nodejs npm  
RUN npm install -g gulp  
# http://stackoverflow.com/questions/22115400/why-do-we-need-to-install-gulp-
globally-and-locally  
WORKDIR /opt/  
RUN npm install gulp  
RUN npm install gulp-less  
RUN npm install gulp-concat  
RUN npm install gulp-coffee  
RUN npm install gulp-imagemin  
RUN npm install del  
WORKDIR /opt/app  
  
# Database  
# TODO  
# Useful  
RUN pip install supervisor  
  
VOLUME ["/opt/app"]  
  
EXPOSE 8080

