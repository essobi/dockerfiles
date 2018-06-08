FROM centos:6  
MAINTAINER Michael Daffin <james1479@gmail.com>  
  
WORKDIR /scripts  
VOLUME /scripts  
  
ENV GOPATH=/go  
  
RUN yum install -y epel-release && \  
yum install -y git go python python-yaml python-requests && \  
yum clean all && \  
go get github.com/stretchr/testify/require github.com/stretchr/testify/assert  

