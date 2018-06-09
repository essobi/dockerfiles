FROM ubuntu:xenial  
  
MAINTAINER Lachlan Toohey <l.toohey@acfr.usyd.edu.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# get the packages first  
# this is the bare minimum to get the project to run  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
devscripts \  
dput \  
git \  
openssh-client \  
&& rm -rf /var/lib/apt/lists/*  
  
# these are needing when using the image, not right now  
COPY acfrmarine-archive-keyring.gpg /etc/apt/trusted.gpg.d/  
COPY acfr-marine-xenial.list /etc/apt/sources.list.d/  
  
RUN sed -i "s/archive.ubuntu.com/mirror.aarnet.edu.au/" /etc/apt/sources.list  

