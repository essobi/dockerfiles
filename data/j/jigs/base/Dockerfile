FROM ubuntu:trusty  
MAINTAINER Ian McCracken <ian.mccracken@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update, then set the locale  
RUN apt-get update -qq && locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
# Upgrade packages  
RUN apt-get upgrade -yqq  
  
# Fix some issues with APT packages.  
# See https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local --rename --add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
RUN apt-get install -yqq curl git-core build-essential

