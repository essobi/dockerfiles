FROM ubuntu:wily  
MAINTAINER Silvano Cirujano Cuesta <silvanociru@gmx.net>  
  
RUN apt-get update && \  
apt-get install -y \  
\--no-install-recommends \  
kde-runtime \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD /bin/bash  
  

