FROM ubuntu:xenial  
MAINTAINER atomney <atomney+docker@gmail.com>  
  
# Tell APT that humans aren't going to answer package questions  
ENV DEBIAN_FRONTEND noninteractive  
  
# Copy proxy file into container  
COPY 02proxy /etc/apt/apt.conf.d/02proxy  
  
# Copy scripts into container  
#COPY scripts /scripts  
# Update and install packages and remove apt proxy file and default desktop
image  
RUN apt-get update -y && \  
apt-get install -y wireshark openssh-server && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm /etc/apt/apt.conf.d/02proxy && \  
rm -rf /var/lib/apt/lists/*  
  
# Set the script to run on container launch  
CMD ["wireshark"]  

