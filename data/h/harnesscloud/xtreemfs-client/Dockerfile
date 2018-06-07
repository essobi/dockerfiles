FROM phusion/baseimage  
MAINTAINER Christoph Kleineweber <kleineweber@zib.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qy update  
RUN apt-get -qy dist-upgrade  
RUN apt-get -qy install wget  
  
RUN echo "deb
http://download.opensuse.org/repositories/home:/xtreemfs/xUbuntu_14.04 ./" >>
/etc/apt/sources.list  
RUN wget -q
http://download.opensuse.org/repositories/home:/xtreemfs/xUbuntu_14.04/Release.key
-O - | sudo apt-key add -  
RUN apt-get -qy update  
RUN apt-get -qy install xtreemfs-client  
  

