FROM ruby:2.3.3  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# for postgres  
RUN apt-get install -y libpq-dev  
  
# for nokogiri  
RUN apt-get install -y libxml2-dev libxslt1-dev  
  
# for capybara-webkit  
RUN apt-get install -y libqt4-webkit libqt4-dev xvfb  
  
# for a JS runtime  
RUN apt-get install -y nodejs  
  
ENV APP_HOME /contact-list  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
# add Gemfile and Gemfile.lock from host to docker container  
ADD Gemfile $APP_HOME/Gemfile  
ADD Gemfile.lock $APP_HOME/Gemfile.lock  
RUN bundle install  
  
ADD . $APP_HOME  

