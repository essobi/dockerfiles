FROM php:7-apache  
MAINTAINER kujiy  
  
# Install fundamental softwares  
RUN apt-get update -y && apt-get install -y \  
iputils-ping \  
iproute \  
traceroute \  
wget \  
telnet \  
vim \  
curl \  
net-tools \  
dnsutils \  
&& apt-get clean all  
  
RUN a2enmod rewrite  

