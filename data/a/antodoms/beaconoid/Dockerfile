FROM ruby:2.4-slim  
MAINTAINER antodoms(antodoms@gmail.com)  
  
RUN apt-get update && apt-get install -qq -y --no-install-recommends git-core
curl zlib1g-dev build-essential nodejs apt-utils libssl-dev libreadline-dev
libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-
dev python-software-properties libffi-dev postgresql-client-common postgresql-
client libpq-dev libmagickwand-dev imagemagick  
  
ENV INSTALL_PATH /beaconoid  
RUN mkdir -p $INSTALL_PATH  
WORKDIR $INSTALL_PATH  
  
COPY Gemfile Gemfile.lock ./  
  
RUN gem install bundler && bundle install --jobs 20 --retry 5  
  
COPY . .  
  
#ADD . /beaconoid  
#EXPOSE 80

