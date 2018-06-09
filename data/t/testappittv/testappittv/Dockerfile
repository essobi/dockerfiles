FROM centos:centos6  
  
MAINTAINER info@it-tv.co.il  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm  
  
RUN yum install -y npm  
#remark  
#remark 2  
COPY . /src  
  
RUN cd /src; npm install  
  
EXPOSE 8080  
CMD cd /src && node ./app.js  

