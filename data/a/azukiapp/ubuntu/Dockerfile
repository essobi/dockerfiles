# The container includes:  
#  
# azukiapp/ubuntu:  
# * Ubuntu 14.04  
# * Git  
# * VIM  
#  
  
FROM ubuntu:trusty  
MAINTAINER Azuki <support@azukiapp.com>  
  
#
==============================================================================  
# Ubuntu Linux 14.04  
#
==============================================================================  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN apt-get update \  
&& apt-get upgrade -yq \  
&& apt-get -yq install \  
build-essential \  
python \  
ca-certificates \  
curl \  
wget \  
bindfs \  
vim \  
git-core \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

