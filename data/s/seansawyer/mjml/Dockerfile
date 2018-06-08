FROM centos:centos7  
  
MAINTAINER Sean Sawyer github.com/seansawyer  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
  
RUN yum -y install nodejs  
  
RUN npm install mjml  
  
ENV PATH $PATH:/node_modules/.bin  
  
RUN adduser --uid 1000 mjml  
  
USER mjml  

