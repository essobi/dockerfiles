FROM ruby:2.4.1  
RUN apt-get update && apt-get install -y build-essential  
RUN apt-get install -y nodejs npm  
RUN apt-get install -y libpq-dev  
  
RUN mkdir -p /usr/src/app  
ENV APP_HOME /usr/src/app/rails-app  
COPY app/* $APP_HOME  
COPY bin /usr/bin  
WORKDIR $APP_HOME

