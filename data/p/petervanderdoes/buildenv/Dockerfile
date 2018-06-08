FROM ubuntu:trusty  
  
# Set the env variables to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
# Upstart and DBus have issues inside docker. Work around it  
#RUN dpkg-divert --local --rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Installing the build environment  
RUN apt-get install -y build-essential devscripts fakeroot quilt dh-make dh-
exec automake libdistro-info-perl less vim  

