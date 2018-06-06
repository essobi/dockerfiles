FROM ruby:2.1.1  
MAINTAINER enogrob@gmail.com  
  
# Deploy confs app  
WORKDIR /usr/src/app  
COPY . ./  
RUN gem install bundler && bundle install && rake confs:init[yes]  

