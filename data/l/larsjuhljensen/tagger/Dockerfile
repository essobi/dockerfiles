# Base container with tools dependencies for the Reflect project  
#  
# VERSION 1  
FROM centos:7.2.1511  
MAINTAINER lars.juhl.jensen@gmail.com  
  
# install base dependencies  
RUN yum -y install hg swig gcc gcc-c++ make python-devel boost boost-devel  
  
WORKDIR /app  
  
# clone and build tagger  
RUN hg clone https://hg@bitbucket.org/larsjuhljensen/tagger \  
&& cd tagger \  
&& make  
  
VOLUME /data  
WORKDIR /data  
ENTRYPOINT ["/app/tagger/tagcorpus"]  

