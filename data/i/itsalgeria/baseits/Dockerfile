FROM phusion/baseimage:0.9.21  
MAINTAINER m.benyoub@itsolutions.dz  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Define some ENV variables  
# this will be used as the default backend option for confd  
ENV CONFD_BACKEND env  
# generate a locale and ensure it on system users  
RUN locale-gen en_US.UTF-8 && update-locale && echo 'LANG="en_US.UTF-8"' >
/etc/default/locale  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# add some system packages  
RUN apt-get update && apt-get -y -q install \  
sudo less \  
\--no-install-recommends  
  
# add some net-tools  
RUN apt-get -y -q install \  
net-tools  

