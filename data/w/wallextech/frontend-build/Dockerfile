FROM ubuntu:latest  
  
MAINTAINER Wallex <admin@wallextech.com>  
  
ENV working_dir /var/www  
  
USER root  
  
RUN apt-get update && apt-get install -y curl git \  
bzip2 libfontconfig # For phanstomJS \  
ruby-full  
  
# Get the NoddeJS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash && \  
apt-get install -y nodejs  
  
# Set the node path  
RUN PATH=/usr/bin/node:$PATH  
  
# Pull down some npm pakcages  
RUN npm install -g grunt-cli karma-cli jasmine jasmine-core  
  
# Pull down PhantomJS  
RUN npm install phantomjs-prebuilt karma-phantomjs-launcher  
  
# Install and upgrade pip  
RUN apt-get install -y python-pip python-dev build-essential groff  
RUN pip install --upgrade pip  
  
# Install AWS CLI  
RUN pip install awscli  
  
# Make a directry for deployment  
RUN mkdir $working_dir -p  
  
# Switch to the working directory  
WORKDIR $working_dir  

