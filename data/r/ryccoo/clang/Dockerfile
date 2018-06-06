FROM ubuntu:14.04  
MAINTAINER Richard Ludvigh "https://github.com/Ryccoo"  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV HOME /root  
ENV SHELL /bin/bash  
WORKDIR /home  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update  
RUN apt-get install -y autoconf make bison build-essential libssl-dev libyaml-
dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-
dev git curl python-software-properties software-properties-common ruby-full  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
RUN apt-get update  
  
RUN apt-get install -y clang-3.5  
  
RUN mkdir -p /usr/src/ruby  
WORKDIR /usr/src/ruby

