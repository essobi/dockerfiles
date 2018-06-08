FROM debian:jessie  
  
RUN apt-get update && apt-get install --assume-yes --no-install-recommends \  
default-jre \  
wget \  
unzip  
  
RUN wget -q -O tla.zip https://tla.msr-
inria.inria.fr/tlatoolbox/products/TLAToolbox-1.5.2-linux.gtk.x86_64.zip &&
unzip tla.zip && rm tla.zip  
  
ENTRYPOINT ./toolbox/toolbox  

