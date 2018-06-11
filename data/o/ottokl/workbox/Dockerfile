FROM ubuntu:16.04  
  
MAINTAINER Otto Lote <otto@lote.no>  
LABEL Description="Ubuntu image with basic dev tools for quick deployment to
kubernetes cluster" \  
Usage="kubectl run workbox -it --image ottokl/workbox --restart=Never --rm
bash" \  
Version="1.0"  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y \  
nmap \  
inetutils-ping \  
dnsutils \  
mongodb \  
vim \  
python \  
python3 \  
python-pip \  
python3-pip \  
ssh  
  
  
CMD "bash"  

