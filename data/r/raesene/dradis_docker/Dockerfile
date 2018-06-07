FROM ubuntu:16.04  
MAINTAINER Rory McCune <rorym@mccune.org.uk>  
  
  
#Add the brightbox PPA manually to avoid installing loads of software  
RUN echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu xenial main "
>> /etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C3173AA6  
  
#Pre-requisites  
RUN apt update -qq && \  
apt install -y ruby2.3 nodejs git gcc ruby2.3-dev make libmysqlclient-dev
libsqlite3-dev g++ && \  
apt clean && rm -rf /var/lib/apt/lists/*  
  
#Clone the repo  
RUN git clone \--depth=1 https://github.com/dradis/dradis-ce.git  
  
WORKDIR /dradis-ce  
  
#Need to run setup twice, which needs doing for reasons unexplainable  
RUN ruby bin/setup && bundle install && \  
ruby bin/setup  
  
#Bind to all interfaces explicitly as the default is localhost only  
CMD ["bundle","exec","rails","server","-b","0.0.0.0"]  

