#
------------------------------------------------------------------------------  
# Based on a work at https://github.com/docker/docker.  
#
------------------------------------------------------------------------------  
# Pull base image.  
FROM ubuntu:bionic  
MAINTAINER Lucius Amora <reture@msn.com>  
  
#
------------------------------------------------------------------------------  
# Install Packages  
RUN apt-get update \  
&& apt install -y curl supervisor nodejs git build-essential nginx \  
sshfs openssh-server tmux net-tools vim man autoconf \  
libfuse-dev libboost-all-dev libssl-dev libxml2-dev \  
clang-tools libclang-dev clang-format clang-tidy libllvm6.0-dbg lldb lld \  
golang rustc cmake luajit python3 ruby default-jdk \  
&& sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/'
/etc/supervisor/supervisord.conf \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

