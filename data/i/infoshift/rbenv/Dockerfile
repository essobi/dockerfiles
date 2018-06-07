FROM ubuntu:14.04  
MAINTAINER Jesse Panganiban <jesse.panganiban@infoshiftinc.com>  
  
RUN apt-get update  
RUN apt-get install -y build-essential git-core curl  
  
RUN git clone https://github.com/sstephenson/rbenv.git /rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/rbenv/plugins/ruby-build  
  
ENV RBENV_ROOT /rbenv  
ENV PATH /rbenv/bin:$PATH  
ENV PATH /rbenv/shims:$PATH  

