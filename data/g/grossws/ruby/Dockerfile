FROM grossws/centos:7-dev  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
RUN yum -y install ruby-devel rubygems \  
&& yum clean all \  
&& echo 'gem: --no-document' >> /etc/gemrc \  
&& gem install bundler  
  

