FROM node  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
nano vim \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/ \  
&& \  
npm install -g sqlectron-term \  
&& \  
rm -rf ~/.npm/ /tmp/*  
  
ENV EDITOR=nano  
  
ENTRYPOINT [ "sqlectron-term" ]  

