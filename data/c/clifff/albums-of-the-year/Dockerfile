# Dockerfile - Rails container  
FROM ubuntu  
MAINTAINER Clif Reeder clifreeder@gmail.com  
  
RUN apt-get -y install python-software-properties  
RUN apt-add-repository -y ppa:brightbox/ruby-ng-experimental  
# for supervisord  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install build-essential git-core redis-server wget zlib1g-dev
libssl-dev libxslt-dev libxml2-dev nodejs ruby1.9.3 supervisor  
RUN gem install bundler  
  
WORKDIR /tmp  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN bundle install  
  
# setup supervisord  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME ["/opt/albums_of_the_year"]  
WORKDIR /opt/albums_of_the_year  
  
EXPOSE 3000  
CMD ["/usr/bin/supervisord"]  

