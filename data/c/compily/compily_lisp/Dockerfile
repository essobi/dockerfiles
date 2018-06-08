FROM ubuntu:16.04  
MAINTAINER Ephraim Rothschild  
RUN mkdir -p /compilebox/usercode && chmod -R 777 /compilebox/usercode  
  
# Update the repository sources list  
#RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
ENV DEBIAN_FRONTEND noninteractive  
ADD example.lisp /compilebox/usercode/  
  
RUN apt-get install -y clisp  
  
RUN echo "nobody: clisp" | cat >> /etc/sudoers  
  
RUN apt-get install -y bc

