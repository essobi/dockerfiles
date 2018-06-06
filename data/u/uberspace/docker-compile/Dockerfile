FROM centos:centos7  
  
MAINTAINER Uberspace <hallo@uberspace.de>  
LABEL name="CentOS 7 Compilation Environment"  
LABEL vendor="CentOS"  
  
RUN yum install -y epel-release  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y git ruby-devel python-pip python-devel libffi-devel
openssl-devel  
RUN gem install fpm  
RUN pip install gsutil  

