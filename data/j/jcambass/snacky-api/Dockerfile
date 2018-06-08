FROM ruby:2.3  
# Install Build Essentials  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# Install git  
RUN apt-get install -y git  
  
# Install Ruby Dev Headers  
RUN apt-get install -y ruby-dev  
  
# NodeJs  
RUN apt-get install -y nodejs  
  
# MySQL client  
RUN apt-get install -y libpq-dev  
  
# Install bundler  
RUN gem install bundler  
  
ENV RAILS_ENV production  
  
ENV APP_HOME /snacky_api  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_Home/  
RUN bundle install  
ADD . $APP_Home

