FROM fedora:21  
  
MAINTAINER Praveen Kumar "kumarpraveen.nitdgp@gmail.com"  
RUN yum -y update && yum install -y @development-tools fedora-packager  
  
RUN useradd -m packager  
USER packager  
RUN mkdir ~/.ssh && chmod 700 ~/.ssh  

