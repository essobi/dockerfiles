FROM ruby:2.3.3  
RUN gem install bundler --version '1.14.6'  
  
RUN apt-get update -qq && apt-get install -y build-essential  
RUN gem install bundler --no-rdoc --no-ri  
  
ENV APP_HOME /estuary  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_HOME/  
RUN bundle install  
  
ADD . $APP_HOME  

