#################################################################  
# Dockerfile to build Zimbra Collaboration 8.7.11 container images  
# Based on Ubuntu 16.04  
# Created by Jorge de la Cruz  
#################################################################  
FROM ubuntu:16.04  
  
RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-
set-selections  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \  
wget \  
dialog \  
openssh-client \  
software-properties-common \  
bind9 bind9utils bind9-doc dnsutils \  
net-tools \  
sudo \  
rsyslog \  
unzip && \  
echo "Downloading Zimbra Collaboration 8.7.11" && mkdir -p /opt/zimbra-install
&& \  
wget -O /opt/zimbra-install/zimbra-zcs-8.7.11.tar.gz
https://files.zimbra.com/downloads/8.7.11_GA/zcs-8.7.11_GA_1854.UBUNTU16_64.20170531151956.tgz  
  
VOLUME ["/opt/zimbra"]  
  
EXPOSE 22 25 465 587 110 143 993 995 80 443 8080 8443 7071  
  
COPY opt /opt/  
  
CMD ["/bin/bash", "/opt/start.sh", "-d"]  

