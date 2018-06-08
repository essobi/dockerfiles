FROM centos:7  
MAINTAINER Liam Galvin <liam@liam-galvin.co.uk>  
  
RUN yum install -y ruby-devel rubygems gcc make rpmdevtools tar wget rpm-build
\  
&& gem install fpm \  
&& yum clean all \  
&& mkdir /src  
  
WORKDIR /src/  

