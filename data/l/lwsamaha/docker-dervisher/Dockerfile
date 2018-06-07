FROM debian:wheezy  
MAINTAINER lwsamaha  
  
# tools  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
python-pip  
RUN pip install -U pip  
RUN pip install boto  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get clean autoclean && \  
apt-get autoremove  
  
# dervisher  
RUN pip install dervisher  
# ENTRYPOINT ["dervisher"]  

