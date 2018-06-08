FROM golang:1.9.0-stretch  
  
MAINTAINER Noel Cower <ncower@gmail.com>  
  
# git - For cloning packages  
# openssl - Cloning via https  
# ca-certificates - Cloning via https  
# make \- Building  
# openssh-client - Cloning via ssh, key injected over volume  
RUN echo 'deb http://httpredir.debian.org/debian stretch-backports main' >
/etc/apt/sources.list.d/stretch-backports.list && \  
apt-get update && apt-get install -y \--no-install-recommends -t stretch-
backports libc6 git openssl ca-certificates openssh-client jq m4  
  
ONBUILD RUN RUN apt-get update && apt-get install -y \--no-install-recommends
-t stretch-backports libc6 git openssl ca-certificates openssh-client jq m4  

