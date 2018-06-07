###############################################################################  
# This container will provide a mininum sized image that will contain  
# python 3.4 and pip  
###############################################################################  
  
FROM debian:jessie  
  
MAINTAINER Byron Kim (bkim@keplergrp.com)  
  
RUN \  
apt-get update -y \  
&& \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -yq \  
python3 \  
python3-pip \  
cron \  
&& \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
CMD python3 --version  

