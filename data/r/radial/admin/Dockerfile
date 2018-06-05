# Spoke Dockerfile for admin  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
openssh-server \  
supervisor \  
multitail \  
vim \  
postgresql-client &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
# Make a run directory hidden from wheel for this containers programs.  
RUN mkdir -p /var/local/run  
  
COPY supervisor /etc/supervisor  
  
COPY /entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

