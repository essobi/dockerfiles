FROM garage/ruby20  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
## Rails uses node.js as JS environment  
RUN /var/garage/install nodejs  
  
# Build tooling and dev headers  
RUN /var/garage/install git build-essential \  
libxml2-dev libxslt1-dev \  
libsqlite3-dev \  
zlib1g-dev  
  
# OPTIONAL  
# /var/garage/install imagemagick libmagickwand-dev &&\  
# /var/garage/install libmysqlclient-dev &&\  
# /var/garage/install libpq-dev &&\  
# /var/garage/install libqt4-webkit libqt4-dev &&\  
# /var/garage/install libcurl4-openssl-dev &&\  
# This is so slow  
# RUN gem install rails -v '~>3'  
# Update base gems (--prerelease to use bundler 1.5)  
RUN gem update --prerelease && gem cleanup  
  
# Much faster, I guess  
RUN echo "source 'http://rubygems.org'\n gem 'rails', '~> 3'" > /tmp/Gemfile
&&\  
bundle install --gemfile /tmp/Gemfile --jobs 2 --retry 3 --full-index  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 3000  
ENV GARAGE_PROVIDES rails rackup sprockets

