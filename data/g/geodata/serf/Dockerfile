##  
# Serf in a Docker image  
#  
# https://www.serfdom.io/  
#  
# Ubuntu 14.04 Trusty Tahr  
FROM phusion/baseimage:0.9.16  
# Install the application  
ADD . /usr/local/src/serf/  
RUN apt-get update -y && \  
apt-get install -y make unzip && \  
make -C /usr/local/src/serf -f /usr/local/src/serf/Makefile runit  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose the serf ports  
EXPOSE 7373 7946  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

