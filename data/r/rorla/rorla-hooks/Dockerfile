FROM seapy/ruby:2.1.2  
MAINTAINER ChangHoon Jeong <iamseapy@gmail.com>  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq  
RUN apt-get install -qqy iptables ca-certificates lxc  
  
# Install Docker from Docker Inc. repositories.  
RUN apt-get install -qqy apt-transport-https  
RUN echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9  
RUN apt-get update -qq  
RUN apt-get install -qqy lxc-docker-1.0.0  
  
WORKDIR /app  
  
#(required) Install App  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install --without development test  
ADD . /app  
  
EXPOSE 8443  
CMD bundle exec ruby server.rb

