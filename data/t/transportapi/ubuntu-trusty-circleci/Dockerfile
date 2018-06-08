FROM ubuntu-upstart:trusty  
  
MAINTAINER Vladimir Blaskov <blaskov@gmail.com>  
  
# apt-show-versions does not play well with compressed indexes as discussed  
# here: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=617856  
RUN rm /etc/apt/apt.conf.d/docker-gzip-indexes && \  
apt-get update && \  
apt-get clean  
  
COPY locale /etc/default/locale  
RUN locale-gen en_US.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  

