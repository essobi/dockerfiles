FROM nimbix/base-ubuntu-nvidia:8.0-cudnn5-devel-ubuntu14.04  
MAINTAINER Nimbix, Inc.  
  
USER root  
ADD ./scripts /usr/local/scripts  
  
USER root  
RUN /usr/local/scripts/install-torch.sh  
  
ADD ./NAE/help.html /etc/NAE/help.html  
ADD ./NAE/AppDef.json /etc/NAE/AppDef.json  
  
USER nimbix  
WORKDIR /home/nimbix  

