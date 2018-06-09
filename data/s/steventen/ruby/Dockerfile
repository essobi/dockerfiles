# Base Image Build for Ruby && Rails Deployment  
FROM ubuntu:14.04  
MAINTAINER Steven Yue <jincheker@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
#RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
#echo 'debconf debconf/frontend select Dialog' | debconf-set-selections  
#Install essential packages  
RUN apt-get -y update  
RUN apt-get -y install build-essential zlib1g-dev libssl-dev libyaml-dev
libpcre3-dev libcurl4-openssl-dev libreadline-dev libxml2-dev  
RUN apt-get -y install python-software-properties software-properties-common  
RUN apt-get -y install curl git-core  
RUN apt-get -y install libmysqlclient-dev ruby-mysql  
  
# Install nodejs  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get -y update  
RUN apt-get -y install nodejs  
  
# Install ruby  
RUN curl -O ftp://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz  
RUN tar -xvzf ruby-2.1.2.tar.gz  
RUN cd ruby-2.1.2/ && ./configure --prefix=/usr/local \--disable-install-doc  
RUN cd ruby-2.1.2/ && make  
RUN cd ruby-2.1.2/ && make install  
RUN gem install bundler -N -f  
RUN rm -r ruby-2.1.2 ruby-2.1.2.tar.gz  
  
RUN echo 'gem: --no-document' > /usr/local/etc/gemrc

