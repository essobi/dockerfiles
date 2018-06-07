FROM ruby:2.3  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
  
RUN mkdir /gems  
ADD Gemfile /gems/Gemfile  
ADD Gemfile.lock /gems/Gemfile.lock  
ENV BUNDLE_GEMFILE /gems/Gemfile  
  
RUN mkdir /app  
WORKDIR /app  
RUN bundle install  
  
EXPOSE 3000  
EXPOSE 80  
CMD rm -f tmp/pids/server.pid && bundle exec rails s -p 3000 -b '0.0.0.0'  
  
ONBUILD ADD . /app  

