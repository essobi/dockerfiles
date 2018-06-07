FROM ruby:2.2.4  
MAINTAINER Shuky Dvir <shuky.dvir@gmail.com>  
  
RUN mkdir /shopcomp  
WORKDIR /shopcomp  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
libxml2-dev \  
libxslt1-dev \  
git-core \  
curl \  
zip \  
libssl-dev \  
python-software-properties \  
libffi-dev \  
libmysqlclient-dev \  
vim-nox \  
supervisor \  
mysql-client \  
redis-tools \  
nodejs  
  
  
ADD Gemfile /shopcomp/Gemfile  
ADD Gemfile.lock /shopcomp/Gemfile.lock  
  
RUN gem install bundler --no-document \  
&& bundle config \--global path "$GEM_HOME" \  
&& bundle config \--global bin "$GEM_HOME/bin" \  
&& bundle config \--global --jobs 32 \  
&& bundle config build.nokogiri --use-system-libraries \  
&& bundle install \--retry=3  
  
  

