# Spoke Dockerfile for clarity  
  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
ruby ruby-dev make g++ ruby-eventmachine ruby-json &&\  
gem install clarity &&\  
apt-get -qyV remove ruby-dev make g++ &&\  
apt-get -qyV autoremove &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
# Process startup info  
ENV SPOKE_NAME clarity  
  
COPY /entrypoint.sh /entrypoint.sh  
  
EXPOSE 80  

