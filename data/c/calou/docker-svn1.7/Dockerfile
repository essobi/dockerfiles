FROM debian:7.9  
MAINTAINER Sébastien Gruchet <gruchet@gmail.com>  
  
ENV SVN_VERSION 1.7.22-1  
ENV OWNER svn  
  
RUN apt-get -y -qq update && apt-get install -y -qq wget  
RUN echo "deb http://opensource.wandisco.com/debian/ wheezy svn17" >
/etc/apt/sources.list.d/wandisco-subversion.list  
RUN wget -q -O - http://opensource.wandisco.com/wandisco-debian.gpg | apt-key
add - && \  
apt-get -y -qq update && apt-get install -y wget
subversion=${SVN_VERSION}+WANdisco libsvn1=${SVN_VERSION}+WANdisco  
  
VOLUME /work  
WORKDIR /work  
  

