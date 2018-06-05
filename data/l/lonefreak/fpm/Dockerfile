FROM centos:6.6  
MAINTAINER Fabricio Leotti <fabricio.leotti@gmail.com>  
RUN yum install -y gcc rpm-build ruby ruby-devel rubygems tar wget which &&
yum clean all  
RUN gem install fpm --no-rdoc --no-ri

