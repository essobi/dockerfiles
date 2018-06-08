# DOCKER-VERSION 1.3.0  
#  
# Mono-based image with the Asp.Net vnext K Version Manager (KVM)  
FROM mono:3.10  
MAINTAINER Matteo Spreafico  
  
RUN apt-get update && apt-get -y install curl git-core  
  
ENV HOME /root  
RUN mozroots --import --sync  
RUN /bin/bash -c "curl
https://raw.githubusercontent.com/aspnet/Home/master/kvminstall.sh | sh &&
source ~/.kre/kvm/kvm.sh && kvm upgrade"  

