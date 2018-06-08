# Very basic/default mongodb (x64) install for testing/playground only.  
FROM centos:centos6  
  
MAINTAINER "ray hassan" ray@nutanix.com  
  
RUN groupadd mongod  
RUN useradd mongod -g mongod  
  
COPY mongodb.repo /etc/yum.repos.d/mongodb.repo  
RUN yum update -y yum && yum install -y mongodb-org  
  
EXPOSE 27017  
RUN mkdir -p /data/db  
RUN chown -R mongod:mongod /data/db  
RUN chown -R mongod:mongod /var/log/mongodb  
  
ENV HOSTNAME mongodb-host  
USER mongod  
WORKDIR /home/mongod  
  
#ENTRYPOINT /usr/bin/mongod  
#CMD --dbpath /data/db  

