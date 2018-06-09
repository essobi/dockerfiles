FROM ruby:2.3.0  
RUN \  
apt-get update -y && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
libpq-dev \  
nodejs \  
apt-utils \  
vim git wget libfreetype6 libfontconfig bzip2 time python-pip  
  
#phantomjs  
ENV PHANTOMJS_VERSION 2.1.1  
RUN \  
mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://s3.amazonaws.com/assets.staticdriver.com/phantomjs/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
RUN pip install awscli  
  
#RUN mkdir /app/user  
WORKDIR /app/user  
ADD Gemfile /app/user/Gemfile  
ADD Gemfile.lock /app/user/Gemfile.lock  
RUN bundle install  
ADD . /app/user  
CMD bundle exec puma -C config/puma.rb  

