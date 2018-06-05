FROM ubuntu:14.04  
  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common build-essential  
  
RUN \  
apt-add-repository ppa:brightbox/ruby-ng-experimental && \  
apt-get update && \  
apt-get install -y ruby2.1 ruby2.1-dev ruby2.1-doc  
  
CMD ruby -v  

