FROM centos:centos7  
  
MAINTAINER Avast Viruslab Systems  
  
# install main packages:  
RUN yum -y update; yum clean all;  
  
RUN yum -y install epel-release; yum -y install perl-core; yum -y install
perl-App-cpanminus; yum -y install gcc  
RUN yum install -y gcc-c++  

