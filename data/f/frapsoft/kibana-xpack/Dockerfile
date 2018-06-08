FROM kibana  
  
LABEL maintainer "Maik Ellerbrock <opensource@frapsoft.com>"  
  
ENV VERSION 0.1.0  
  
RUN \  
apt-get update && \  
apt-get install -y \  
libfontconfig \  
libfreetype6 && \  
rm -rf /var/lib/apt/lists/* && \  
usr/share/kibana/bin/kibana-plugin install x-pack  

