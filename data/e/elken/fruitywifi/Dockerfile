FROM ubuntu  
MAINTAINER elken  
  
ADD ./FruityWifi-master /FruityWifi-master  
  
RUN apt-get update && apt-get upgrade -y && cd /FruityWifi-master && /bin/sh
/FruityWifi-master/install-FruityWifi.sh  

