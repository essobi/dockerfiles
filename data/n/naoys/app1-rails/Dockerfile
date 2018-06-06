FROM ruby:2.3.1  
RUN apt-get update -qq && \  
apt-get install -y build-essential libpq-dev nodejs  
  
# Rails App  
RUN mkdir /app  
WORKDIR /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install  
ADD . /app  
RUN mkdir -p tmp/sockets  
  
# Expose volumes to frontend  
VOLUME /app/public  
VOLUME /app/tmp  
  
# Start Server  
# TODO: environment  
CMD bundle exec puma  

