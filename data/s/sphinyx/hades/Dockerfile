FROM ruby:2.4.1  
MAINTAINER Huynh Quang Thao "huynhquangthao@gmail.com"  
RUN sed -i ' 1 s/.*/& contrib/' /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
dnsutils \  
libpq-dev \  
lsof \  
nodejs \  
postgresql \  
vim  
  
ENV APP_HOME /webapp  
ENV SET_CONTAINER_TIMEZONE true  
ENV CONTAINER_TIMEZONE Asia/Ho_Chi_Minh  
ENV LANG C.UTF-8  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
COPY Gemfile* $APP_HOME/  
  
RUN gem install bundler --no-ri --no-rdoc && bundle install --jobs 20 --retry
5  
  
# Copy the main application.  
COPY . $APP_HOME  
  
RUN mkdir -p $APP_HOME/log  
RUN touch $APP_HOME/log/sidekiq.log  
  
RUN ["chmod", "+x", "./docker-entrypoint.sh"]  
ENTRYPOINT ["./docker-entrypoint.sh"]

