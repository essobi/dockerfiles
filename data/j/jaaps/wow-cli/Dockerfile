FROM centos:centos6  
  
RUN yum install -y epel-release  
RUN yum install -y nodejs npm  
RUN npm install -g wow-cli  
  
ENV WOWPATH /wow  
ENTRYPOINT ["/usr/bin/wow"]

