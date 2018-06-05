FROM ruby:2.2.0  
MAINTAINER Matt Wright <matt@stitched.io>  
  
RUN apt-get update && apt-get install -y uuid-dev  
  
ENV APP_HOME /blurrily  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
EXPOSE 12021  
ADD Gemfile* $APP_HOME/  
RUN bundle install  
  
ADD . $APP_HOME  

