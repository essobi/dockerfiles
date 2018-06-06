FROM ruby:2.3.1  
RUN apt-get update -qq && apt-get install -y build-essential  
RUN apt-get install -y libpq-dev libgd2-xpm-dev libxml2-dev libxslt1-dev
libssl-dev libcurl4-openssl-dev libreadline-dev libsqlite3-dev nodejs  
  
ENV APP_HOME /dictionary  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_HOME/  
RUN bundle install  
  
ADD . $APP_HOME  
  
EXPOSE 9292  
ENTRYPOINT puma -b tcp://0.0.0.0:9292 -e production  

