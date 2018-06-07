FROM ubuntu:14.04  
  
RUN useradd -ms /bin/bash halyard && \  
apt-get update && \  
apt-get install -y apt-transport-https ca-certificates && \  
apt-get install -y curl && apt-get install -y software-properties-common && \  
curl -O
https://raw.githubusercontent.com/spinnaker/halyard/master/install/stable/InstallHalyard.sh
&& \  
bash InstallHalyard.sh \--user halyard  
USER halyard  

