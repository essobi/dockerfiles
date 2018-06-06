FROM debian:jessie  
MAINTAINER tgagor, https://github.com/tgagor  
  
RUN apt-get update  
  
# Install ClamAV  
RUN apt-get install -y clamav clamav-freshclam  
  
# Update ClamAV Definitions  
RUN freshclam  
  
CMD ["/usr/bin/clamscan"]  

