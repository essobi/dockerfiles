FROM centos:centos6  
  
MAINTAINER nigelpoulton@hotmail.com  
  
# Enable EPEL for Node.js  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
  
# Install Node...  
RUN yum install -y npm  
  
RUN npm install yarn -g  
  
# Copy app to /build  
COPY . /build  
  
# Install app and dependencies into /build  
RUN cd /build; yarn  
  
EXPOSE 8080  
CMD cd /build && node ./src/index.js  

