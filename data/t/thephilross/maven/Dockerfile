# MAVEN docker container  
FROM ubuntu:14.04  
MAINTAINER Philipp Ross, philippross369@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
build-essential \  
libnetcdf-dev \  
qt4-dev-tools \  
wget  
  
RUN wget http://genomics-
pubs.princeton.edu/mzroll/release/src/maven_682.tar.gz && \  
tar -xzvf maven_682.tar.gz && \  
cd maven_682 && \  
qmake && \  
make && \  
cd /usr/bin/ && \  
ln -s /maven_682/bin/maven .  
  
CMD ["/usr/bin/maven"]  

