FROM ubuntu:17.04  
MAINTAINER RazzDazz  
# Using instructions from  
# http://docs.openhab.org/installation/linux.html  
  
ENV REFRESHED_AT 2017-06-20  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update packages to install java  
RUN apt-get -yqq update && \  
apt-get -yqq upgrade && \  
apt-get --no-install-recommends -yqq install openjdk-8-jre-headless && \  
rm -rf /var/lib/apt/lists/*  
# First, add the openHAB 2 Bintray repository key to your package manager and
allow Apt to use the HTTPS Protocol:  
RUN apt-get -yqq update && \  
apt-get -yqq upgrade && \  
apt-get -y install wget && \  
wget -qO -
'https://bintray.com/user/downloadSubjectPublicKey?username=openhab' | apt-key
add - && \  
apt-get -y install apt-transport-https && \  
rm -rf /var/lib/apt/lists/*  
# Add openhab repo to sources list, update and install openhab2 and addons  
RUN echo 'deb https://dl.bintray.com/openhab/apt-repo2 stable main' | tee
/etc/apt/sources.list.d/openhab2.list && \  
apt-get -yqq update && \  
apt-get -yqq install openhab2 && \  
apt-get -yqq install openhab2-addons && \  
rm -rf /var/lib/apt/lists/*  
# Expose Ports  
EXPOSE 5005 8080 8443  
# Expose Volumes  
# Site configuration  
# VOLUME /etc/openhab2  
# Log Files  
VOLUME /var/log/openhab2  
# Userdata like rrd4j databases:  
# VOLUME /var/lib/openhab2  
# Set workdir  
WORKDIR /usr/share/openhab2  
  
# run shell to keep container alive for testing  
CMD /bin/bash  

