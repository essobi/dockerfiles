FROM nitrousio/ubuntu:latest  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
RUN \  
mkdir -p /usr/local/opt/nvm && \  
/bin/bash -c 'chown -R $NITROUS_USERNAME:$NITROUS_USERNAME /usr/local/opt/nvm'  
  
RUN echo 'source /usr/local/opt/nvm/nvm.sh' >> /etc/profile  
  
USER $NITROUS_USERNAME  
  
# nvm 0.22.0 - 20141226  
# node 0.10.35 - 20141222  
RUN \  
/bin/bash -c \  
'git clone https://github.com/creationix/nvm.git /usr/local/opt/nvm && \  
cd /usr/local/opt/nvm && git checkout v0.22.0 2>/dev/null && \  
source /usr/local/opt/nvm/nvm.sh && \  
nvm install 0.10.35 && \  
nvm alias default 0.10.35'  
  
USER root  

