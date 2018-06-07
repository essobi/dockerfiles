FROM ruby:2.4.2-slim  
MAINTAINER hmt <dev@hmt.im>  
  
RUN apt-get update && apt-get install -y \  
libmariadb-client-lgpl-dev \  
libmariadbd-dev \  
libpq-dev \  
sqlite3 \  
libsqlite3-dev \  
build-essential \  
git && \  
mkdir /app && \  
gem install rubygems-update bundler && \  
apt-get autoremove -y && rm -rf /var/lib/apt/lists/*  
  
ENV APP /app  
ENV LANG C.UTF-8  
WORKDIR $APP  
CMD bin/bundle exec puma  
  
ADD Gemfile* $APP/  
  
ENV BUNDLE_GEMFILE=$APP/Gemfile \  
BUNDLE_JOBS=2 \  
BUNDLE_PATH=/bundle  
  
RUN bundle install --without development test  
  
ADD . $APP  

