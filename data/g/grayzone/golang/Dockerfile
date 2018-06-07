FROM grayzone/centos  
  
MAINTAINER Albert Wang  
  
  
RUN yum -y install golang git && yum clean all  
RUN yum -y update && yum clean all  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:$PATH  

