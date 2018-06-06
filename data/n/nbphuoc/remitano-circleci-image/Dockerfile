FROM circleci/ruby:2.4.3-node-browsers  
LABEL description="Ruby + Node + Chrome + Haproxy"  
LABEL version="2.4.3"  
MAINTAINER Phuoc Nguyen <ba.phuoc.nbp@gmail.com>  
  
RUN echo deb http://httpredir.debian.org/debian jessie-backports main | sudo
tee /etc/apt/sources.list.d/backports.list  
RUN curl https://haproxy.debian.net/bernat.debian.org.gpg | sudo apt-key add -  
RUN echo deb http://haproxy.debian.net jessie-backports-1.8 main | sudo tee
/etc/apt/sources.list.d/haproxy.list  
RUN sudo apt-get update; true  
RUN sudo apt-get install -y haproxy=1.8.\\* -t jessie-backports  
RUN sudo apt-get install -y lsof  
RUN sudo apt-get install -y redis-server  

