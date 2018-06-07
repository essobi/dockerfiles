FROM ubuntu:14.04  
MAINTAINER Kyle Manna <kyle@kylemanna.com>  
  
RUN apt-get install -y curl  
RUN curl
http://download.opensuse.org/repositories/home:/xtreemfs/xUbuntu_14.04/Release.key
| apt-key add -  
RUN echo "deb
http://download.opensuse.org/repositories/home:/xtreemfs/xUbuntu_14.04 ./" >
/etc/apt/sources.list.d/xtreemfs.list  
RUN apt-get update  
RUN apt-get install -y xtreemfs-client xtreemfs-server  
  
EXPOSE 30638  

