FROM amazonlinux  
MAINTAINER Luciano Mammino <https://loige.co>  
ARG NODE_VERSION=8.10.0  
RUN yum groupinstall -yq "Development Tools"  
  
# The /var/lang is where AWS installs Node.  
RUN mkdir -p /tmp; \  
curl -vvv
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.gz | \  
tar -zxvC /tmp/  
WORKDIR /tmp/node-v${NODE_VERSION}  
RUN mkdir -p /var/lang; \  
./configure --prefix=/var/lang; \  
make all install  
  
RUN mkdir -p /var/task/lib  
  
ENV LD_LIBRARY_PATH /var/task/lib  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/var/lang/bin  
  
RUN yum install -y sudo && yum clean all  
  
WORKDIR /var/task  
  
ENTRYPOINT ["node"]  

