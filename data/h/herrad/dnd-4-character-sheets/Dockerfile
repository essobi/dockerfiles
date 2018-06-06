FROM centos:centos6  
  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
  
RUN yum install -y npm  
  
COPY . /code  
  
RUN cd /code; npm install  
RUN cd /code; npm install -g grunt-cli; grunt  
  
ENV authRealm 178.62.64.215  
EXPOSE 3000  
CMD ["node", "/code/src/app.js"]

