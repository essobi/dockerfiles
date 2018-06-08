FROM centos:centos6  
# Enable EPEL for Node.js  
#ENV http_proxy=http://proxy.hmri.com.au:3128  
ENV MQ_SERVER=192.168.99.100:5672  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
# Install Node.js and npm  
RUN yum install -y nodejs  
RUN yum install -y npm  
  
# Bundle app source  
COPY . /src  
# Install app dependencies  
RUN cd /src; npm install  
  
EXPOSE 8080  
CMD ["node", "/src/index.js"]

