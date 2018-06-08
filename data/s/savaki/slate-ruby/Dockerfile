FROM ubuntu:14.04  
MAINTAINER Prognosio  
  
RUN apt-get update && apt-get install -y ruby ruby-dev rake build-essential  
RUN gem install json -v '1.8.3' && \  
gem install bundler  
  
WORKDIR /docs  
ADD Gemfile /docs/Gemfile  
ADD Gemfile.lock /docs/Gemfile.lock  
RUN cd /docs && bundle install  
  
EXPOSE 4567  
CMD ["bundle", "exec", "middleman", "build"]  
  

