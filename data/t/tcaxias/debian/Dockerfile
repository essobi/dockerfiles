FROM debian:jessie-backports  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
WORKDIR /app  
  
ENV \  
TERM=xterm \  
DEBIAN_FRONTEND="noninteractive" \  
APT="apt -yqq --no-install-recommends" \  
GOPATH="/tmp/go"  
RUN useradd -M app  
  
CMD bash  

