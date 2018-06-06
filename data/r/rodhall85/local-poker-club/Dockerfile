FROM centos:centos6  
  
MAINTAINER rodhall@hotmail.co.uk  
  
# Enable EPEL for Node.js  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
  
# Install Node...  
RUN yum install -y npm  
  
# Install Mongo  
RUN \--name lpc-db -d mongo  
  
# Run app  
RUN \--name lpc --link lpc-db:mongodbo -p 8181:8181 -d rodhall85/local-poker-
club  
  
EXPOSE 8181  
CMD cd /src && node ./server/app.js  

