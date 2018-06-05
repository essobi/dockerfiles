# This docker file contains build environment  
FROM ubuntu:18.04  
MAINTAINER krytin <krytin.vitaly@apriorit.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y libssl-dev libcrypto++-dev uuid-dev libsnappy-dev build-
essential cmake \  
libguestfs-dev libedit-dev libc6-dev-x32 libelf-dev \  
snapd git autoconf linux-headers-4.15.0-20-generic  
  
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*

