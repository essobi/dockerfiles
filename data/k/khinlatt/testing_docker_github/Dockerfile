#FROM node:0.10-onbuild  
# replace with app's default port  
#EXPOSE 8888  
#RUN npm --version  
#FROM centos:centos6  
FROM centos:centos6  
  
# Enable EPEL for Node.js  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
# Install Node.js and npm  
RUN yum install -y npm  
# Bundle app source  
COPY . /src  
  
# like cd  
WORKDIR /src  
# Install app dependencies  
RUN npm install  
  
EXPOSE 8080  
CMD node index.js  

