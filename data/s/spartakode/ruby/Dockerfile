FROM ubuntu:14.04  
MAINTAINER Adnan Issadeen <adnan.issadeen@live.com>  
  
RUN apt-get update && apt-get install wget curl sqlite3 -y --force-yes  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \curl -sSL https://get.rvm.io |
bash -s stable  

