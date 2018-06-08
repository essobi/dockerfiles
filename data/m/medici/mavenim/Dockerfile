FROM maven:3.5.2-jdk-9-slim  
  
USER root  
  
# Increase the limits  
RUN \  
echo "* soft nofile 64000" >> /etc/security/limits.conf ;\  
echo "* hard nofile 64000" >> /etc/security/limits.conf ;\  
echo "root soft nofile 64000" >> /etc/security/limits.conf ;\  
echo "root hard nofile 64000" >> /etc/security/limits.conf  
  
# Installing ghostscript + imagemagick + file + sudo  
RUN \  
apt-get update && \  
apt-get install ghostscript imagemagick file sudo psmisc git -y && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

