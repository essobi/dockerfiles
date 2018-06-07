FROM ruby:2.4-slim  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
curl  
RUN mkdir /myapp  
WORKDIR /myapp  
ADD Gemfile /myapp/Gemfile  
#ADD Gemfile.lock /myapp/Gemfile.lock  
RUN bundle install  
ADD ./progit2-ja /myapp  
ADD Gemfile /myapp/Gemfile  
ADD Rakefile /myapp/Rakefile  
RUN rm /myapp/Gemfile.lock  

