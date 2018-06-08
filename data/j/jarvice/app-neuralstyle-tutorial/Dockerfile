FROM jarvice/app-torch:latest  
MAINTAINER Nimbix, Inc  
  
USER root  
ADD ./scripts /usr/local/scripts/neural-style  
USER nimbix  
RUN /bin/bash /usr/local/scripts/neural-style/install-neural-style.sh  
  
ADD ./NAE/AppDef.json /etc/NAE/AppDef.json  
USER nimbix  

