# Dockerfile  
FROM ubuntu:14.10  
MAINTAINER Ernest Wu(wuboys@gmail.com)  
  
RUN apt-get update  
  
RUN apt-get install -y wget curl \  
build-essential git git-core \  
zlib1g-dev libssl-dev libreadline-dev \  
libyaml-dev libxml2-dev libxslt1-dev \  
software-properties-common  
  
# nginx  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get install -qq -y nginx  
  
#sqlite3  
RUN apt-get install -qq -y libsqlite3-dev sqlite3  
  
# mysql  
RUN apt-get install -qq -y mysql-server mysql-client libmysqlclient-dev  
  
# imagemagick  
RUN apt-get install -qq -y libmagickwand-dev imagemagick  
  
# nodejs  
RUN apt-get install -qq -y nodejs  
  
# qt  
RUN apt-get install -qq -y libqt4-dev  
  
# ruby-install  
RUN cd /tmp &&\  
wget -O ruby-install-0.5.0.tar.gz https://github.com/postmodern/ruby-
install/archive/v0.5.0.tar.gz &&\  
tar -xzvf ruby-install-0.5.0.tar.gz &&\  
cd ruby-install-0.5.0/ &&\  
make install  
  
# MRI Ruby 2.1.4  
RUN ruby-install ruby 2.1.4  
ENV PATH /opt/rubies/ruby-2.1.4/bin:$PATH  
RUN echo "gem: --no-document" > ~/.gemrc  
RUN gem install bundler  
  
# open-jdk  
RUN apt-get install -qq -y openjdk-7-jdk  
  
# tomcat8  
RUN apt-get install -qq -y tomcat8  
  
# foreman  
RUN gem install foreman  
  
# memcached  
RUN apt-get install -qq -y memcached  
  
# redis  
RUN apt-get install -qq -y redis-server  

