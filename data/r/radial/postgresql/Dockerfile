# Spoke Dockerfile for PostgreSQL  
  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
postgresql postgresql-client postgresql-contrib &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
# Process startup info  
ENV SPOKE_NAME postgresql  
ENV SPOKE_CMD /usr/bin/psql  
  
COPY /entrypoint.sh /entrypoint.sh  

