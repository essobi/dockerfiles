FROM centos  
  
MAINTAINER Hiroshi Takase <itshustletime@gmail.com>  
  
# Install Tools  
RUN rpm -i http://ftp-
srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN sed -i '/^\\[centosplus\\]$/,/^\\[/ s/^enabled=0$/enabled=1/'
/etc/yum.repos.d/CentOS-Base.repo  
RUN yum -y groupinstall "Development tools"  
RUN yum -y install libyaml libyaml-devel sqlite-devel zlib-devel readline-
devel git curl-devel libxml2-devel wget openssl openssl-devel  
  
# Install Ruby  
RUN cd /tmp && wget http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz  
RUN cd /tmp && tar zxvf ruby-2.1.2.tar.gz  
RUN cd /tmp/ruby-2.1.2 && ./configure && make && make install  
RUN gem install bundler --no-ri --no-rdoc -V  
RUN gem install rb-readline --no-ri --no-rdoc -V  
  
# Install Rails  
RUN gem install rails --no-ri --no-rdoc -V  
RUN echo rails -v  
  
EXPOSE 80

