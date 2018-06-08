FROM ruby:2.4.0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install --assume-yes apt-utils \  
build-essential libpq-dev \  
net-tools \  
libxml2-dev libxslt1-dev \  
mysql-client libmysqlclient-dev \  
nodejs \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY Gemfile* /tmp/  
  
WORKDIR /tmp  
RUN bundle install  

