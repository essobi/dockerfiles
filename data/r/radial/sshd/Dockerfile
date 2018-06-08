# Spoke Dockerfile for sshd  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
openssh-server &&\  
apt-get clean  
  
# Login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Replace the default host keys with a new set on every build.  
RUN rm /etc/ssh/ssh_host_* &&\  
dpkg-reconfigure openssh-server  
  
RUN mkdir -p /var/run/sshd  
  
# Configure Spoke settings  
ENV SPOKE_NAME sshd  
ENV SPOKE_CMD ssh  
  
COPY /get_public_keys.sh /get_public_keys.sh  

