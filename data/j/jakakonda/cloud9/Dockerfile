FROM ubuntu:latest  
  
ENV USERNAME=''  
ENV PASSWORD=''  
# Prepare env  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
build-essential \  
python \  
nodejs  
  
# Install Cloud9  
RUN git clone https://github.com/c9/core.git cloud9 && \  
cloud9/scripts/install-sdk.sh && \  
mkdir workspace  
  
# Clean  
RUN apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y  
  
EXPOSE 8080  
VOLUME ['/cloud9', '/workspace']  
  
ENTRYPOINT exec nodejs /cloud9/server.js -p 8080 -l 0.0.0.0 -a
${USERNAME}:${PASSWORD} -w /workspace  

