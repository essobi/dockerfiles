FROM ubuntu:14.04  
MAINTAINER Akeda Bagus <admin@gedex.web.id>  
  
# Installation steps based on http://docs.mongodb.org/manual/tutorial/install-
mongodb-on-ubuntu/  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/mongodb.list  
RUN apt-get update  
RUN apt-get install -y -q mongodb-org  
  
VOLUME /data/db  
  
EXPOSE 27017  
CMD ["mongod"]  

