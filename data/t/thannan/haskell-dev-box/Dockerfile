FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y curl git && \  
curl -sSL https://get.haskellstack.org/ | sh  
  
RUN stack setup  
  
ENV PATH "$PATH:/root/.local/bin"  
ADD stack-config.yaml /tmp/  
RUN rm ~/.stack/config.yaml && \  
cp /tmp/stack-config.yaml ~/.stack/config.yaml && \  
stack update  

