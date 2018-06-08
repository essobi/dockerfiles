FROM ruby:latest  
  
MAINTAINER Monish Parajuli  
  
RUN apt-get update -qq && apt-get install -y build-essential libjpeg-progs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
RUN \  
npm install -g grunt-cli && \  
npm install -g bower && \  
npm install -g serverless && \  
npm install -g phantomjs-prebuilt --ignore-scripts && \  
gem install compass --no-rdoc --no-ri  
  

