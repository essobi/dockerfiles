#######################################################################  
# Squeezelite  
# https://github.com/ralph-irving/squeezelite  
#######################################################################  
# Base image: https://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:0.9.22  
# Set correct environment variables  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV LC_ALL="C.UTF-8"  
ENV LANG="en_US.UTF-8"  
ENV LANGUAGE="en_US.UTF-8"  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Upgrading the operating system inside the container  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Install Squeezelite  
RUN apt-get -qq -y update && \  
apt-get -qq -y install alsa-base alsa-utils curl && \  
curl -o squeezelite.tar.gz -L
https://sourceforge.net/projects/lmsclients/files/squeezelite/linux/squeezelite-1.8.7-1052-ubuntu-
lts-x86_64.tar.gz/download && \  
tar -xvzf squeezelite.tar.gz && \  
mv squeezelite /usr/bin && \  
chmod +x /usr/bin/squeezelite && \  
rm -f LICENSE.txt && \  
rm -f squeezelite.tar.gz  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Adding daemon  
RUN mkdir /etc/service/squeezelite  
COPY squeezelite.sh /etc/service/squeezelite/run  
RUN chmod +x /etc/service/squeezelite/run  
  
VOLUME /config

