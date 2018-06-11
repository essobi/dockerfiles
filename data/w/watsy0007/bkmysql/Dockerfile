FROM ruby:2.3  
RUN apt-get update && apt-get -y install rsyslog cron mysql-client  
  
WORKDIR /app  
  
ADD Gemfile Gemfile.lock ./  
RUN bundle install --deployment --without development:test \--jobs 4  
  
ADD . /app  
CMD bundle exec ./scheduler.rb

