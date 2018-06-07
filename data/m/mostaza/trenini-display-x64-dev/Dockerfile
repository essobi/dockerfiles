FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# update system  
RUN apt-get -y update && apt-get -y upgrade  
# build tools  
RUN apt-get -y --no-install-recommends install build-essential yasm  
RUN apt-get -y --no-install-recommends install fakeroot  
  
RUN apt-get -y --no-install-recommends install libqt4-dev  
  
RUN apt-get -y --no-install-recommends install libpci3

