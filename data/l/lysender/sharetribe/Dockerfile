FROM ubuntu:xenial  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -y update && \  
apt-get -y install nodejs curl git libxml2 ruby ruby-dev && \  
apt-get -y install build-essential mysql-client libmysqlclient-dev libxslt-dev
libxml2-dev sphinxsearch imagemagick supervisor && \  
gem install bundler --no-ri --no-rdoc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Create directory for Sharetribe  
RUN mkdir -p /opt/sharetribe  
WORKDIR /opt/sharetribe  
  
ADD Gemfile /opt/sharetribe/Gemfile  
ADD Gemfile.lock /opt/sharetribe/Gemfile.lock  
RUN bundle install  
  
EXPOSE 3000  
CMD ["supervisord", "-n"]  

