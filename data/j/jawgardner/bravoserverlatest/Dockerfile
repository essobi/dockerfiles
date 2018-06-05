FROM ruby:2.2.0  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# for postgres  
RUN apt-get install -y libpq-dev  
  
ENV APP_HOME /bravoserver  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_HOME/  
RUN bundle install  
  
ADD . $APP_HOME  

