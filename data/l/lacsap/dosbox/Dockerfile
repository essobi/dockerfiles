FROM ubuntu:14.04  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
dosbox  
  
RUN mkdir /dosbox  
  
# Mounting the config and data directory  
VOLUME [/root/.dosbox]  
VOLUME [/dosbox]  
  
CMD /usr/bin/dosbox  

