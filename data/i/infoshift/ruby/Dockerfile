FROM infoshift/rbenv  
MAINTAINER Jesse Panganiban <jesse.panganiban@infoshiftinc.com>  
  
ENV RUBY_VERSION 2.1.2  
# Install dependencies  
RUN apt-get update  
RUN apt-get install -y git-core curl zlib1g-dev build-essential \  
libssl-dev libreadline-dev libyaml-dev \  
libsqlite3-dev sqlite3 libxml2-dev \  
libxslt1-dev libcurl4-openssl-dev \  
nodejs python-software-properties  
  
# Disable ri and rdoc  
RUN echo 'gem: --no-ri --no-rdoc' >> ~/.gemrc  
  
# Install ruby  
RUN rbenv install ${RUBY_VERSION} && \  
rbenv global ${RUBY_VERSION}  
  
# Install bundler  
RUN gem install bundler --no-ri --no-rdoc && \  
rbenv rehash  

