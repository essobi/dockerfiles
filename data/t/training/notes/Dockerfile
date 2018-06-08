FROM ubuntu:14.04  
MAINTAINER Docker Education Team <education@docker.com>  
  
RUN apt-get update  
RUN apt-get install -y ruby ruby-dev libpq-dev build-essential  
RUN gem install sinatra bundler --no-ri --no-rdoc  
  
ADD Gemfile /opt/dockernotes/Gemfile  
ADD Gemfile.lock /opt/dockernotes/Gemfile.lock  
WORKDIR /opt/dockernotes  
RUN bundle install  
  
ADD . /opt/dockernotes  
  
EXPOSE 3000  
CMD bundle exec rails s  

