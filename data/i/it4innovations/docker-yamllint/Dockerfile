FROM ubuntu:xenial  
  
RUN apt-get clean && \  
apt-get update -y && \  
apt-get install -y locales && \  
apt-get install -y python3-pkg-resources && \  
apt-get install -y yamllint  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

