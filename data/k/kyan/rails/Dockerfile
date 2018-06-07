FROM ruby:2.3-slim  
MAINTAINER Duncan Robertson <duncan@kyan.com>  
ENV REFRESHED_AT 2017-01-31  
# Install packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
ruby-dev \  
libgdbm-dev \  
libncurses5-dev \  
libpq-dev \  
mysql-client \  
libmysqlclient-dev \  
nodejs \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install RubyGems  
RUN gem update --system --no-rdoc --no-ri  
  
# Install Bundler  
RUN gem install bundler --no-rdoc --no-ri  
  
# Setup app location  
RUN mkdir -p /app  
WORKDIR /app  

