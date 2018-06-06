FROM golang:1.6  
MAINTAINER Ceroic <ops@ceroic.com>  
  
# rsync is required for building kubectl  
RUN apt-get update && apt-get install -y rsync  
  
# Install kubectl  
ENV K8S_VERSION=1.2.4  
ADD https://github.com/kubernetes/kubernetes/archive/v${K8S_VERSION}.tar.gz
/src/kubernetes.tar.gz  
RUN cd /src && tar xzf /src/kubernetes.tar.gz && mv
/src/kubernetes-${K8S_VERSION} /src/kubernetes  
  
# Copy our makefile for building kubectl  
COPY Makefile /src/Makefile  
RUN cd /src && make kubectl  

