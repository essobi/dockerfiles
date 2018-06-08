FROM ruby:2.3.1  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
postgresql-client && rm -rf /var/lib/apt/lists/*  
  
ENV APP_HOME /oak-api  
  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_HOME/  
RUN bundle install  
  
ADD . $APP_HOME  
  
RUN ["chmod", "+x", "./bin/docker-entrypoint"]  
ENTRYPOINT ["./bin/docker-entrypoint"]  

