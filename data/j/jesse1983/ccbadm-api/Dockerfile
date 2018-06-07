FROM ruby:2.2.3  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
ENV APP_HOME /app  
ENV BUNDLE_PATH /bundle  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
ADD Gemfile $APP_HOME/Gemfile  
ADD Gemfile.lock $APP_HOME/Gemfile.lock  
RUN gem install bundler  
RUN bundle install  
ADD . $APP_HOME

