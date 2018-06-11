FROM centos:latest  
  
MAINTAINER BEN CHAABEN Wissem <benchaaben.wissem@gmail.com>  
  
RUN yum -y update && \  
yum -y install curl && \  
curl -sL https://rpm.nodesource.com/setup | bash - && \  
yum -y install nodejs  
  
COPY . /app  
  
WORKDIR /app  
  
RUN npm install -g mocha && npm install  
  
ENTRYPOINT [ "mocha" ]  
  

