#######################################################################  
# Liquidsoap Docker  
# http://liquidsoap.info/  
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
  
# Install Liquidsoap  
# + remove liquidsoap-plugin-opus due to
https://bugs.launchpad.net/ubuntu/+source/liquidsoap/+bug/1404657  
RUN apt-get -qq -y update && \  
apt-get -qq -y install alsa-base alsa-utils liquidsoap liquidsoap-plugin-all
&& \  
apt-get -qq -y remove liquidsoap-plugin-opus  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# copy default liquidsoap.liq to home dir  
COPY liquidsoap.liq /home/liquidsoap.liq  
  
# Adding daemon  
RUN mkdir /etc/service/liquidsoap  
COPY liquidsoap.sh /etc/service/liquidsoap/run  
RUN chmod +x /etc/service/liquidsoap/run  
  
VOLUME /config

