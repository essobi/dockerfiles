FROM centos  
MAINTAINER PromptWorks <team@promptworks.com>  
  
RUN export NODE_VERSION=v0.10.25 && \  
cd /tmp && \  
yum list installed | cut -f 1 -d " " | uniq | sort > /tmp/pre && \  
wget http://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION.tar.gz && \  
tar -zxf node-$NODE_VERSION.tar.gz && \  
cd node-$NODE_VERSION && \  
yum install gcc-c++ make -y && \  
./configure && make && make install && \  
yum list installed | cut -f 1 -d " " | uniq | sort > /tmp/post && \  
diff /tmp/pre /tmp/post | grep "^>" | cut -f 2 -d ' ' | \  
xargs echo yum erase -y && \  
yum clean all && \  
rm -rf /tmp/*  

