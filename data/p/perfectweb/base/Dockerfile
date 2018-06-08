FROM ubuntu:16.04  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
ENV DISPLAY=:0  
ENV GPU_FORCE_64BIT_PTR=1  
ENV GPU_MAX_HEAP_SIZE=100  
ENV GPU_USE_SYNC_OBJECTS=1  
ENV GPU_MAX_ALLOC_PERCENT=100  
ENV GPU_SINGLE_ALLOC_PERCENT=100  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq  
RUN apt-get install -qqy libcurl4-openssl-dev git make automake gcc g++
libssl-dev pkg-config libtool autoconf libcurl3-gnutls wget libgmp-dev
libjansson-dev cmake build-essential  

