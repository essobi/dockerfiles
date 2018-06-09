FROM centos:centos7  
MAINTAINER RedSnapperRice  
  
# Install perl and wget  
RUN yum -y update && \  
yum -y install git perl wget which && \  
yum clean all  
  
# Install nodebrew, node and npm  
RUN curl -L git.io/nodebrew | perl - setup  
ENV PATH $HOME/.nodebrew/current/bin:$PATH  
RUN echo 'export PATH=$HOME/.nodebrew/current/bin:$PATH' >> $HOME/.bashrc && \  
source $HOME/.bashrc && \  
nodebrew install-binary stable && \  
nodebrew use stable

