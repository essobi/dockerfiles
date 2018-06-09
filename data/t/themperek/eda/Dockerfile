FROM centos:6  
MAINTAINER Tomasz Hemperek <hemperek@uni-bonn.de>  
  
RUN yum update -y  
RUN yum install git -y  
RUN yum install tar -y  
RUN yum groupinstall 'Development Tools' -y  
RUN yum clean all  
  
RUN git config --global http.sslverify false  
  

