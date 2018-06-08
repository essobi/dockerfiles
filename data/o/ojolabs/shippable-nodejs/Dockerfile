FROM ojolabs/shippable-base:latest  
  
# Install a default nodejs for the system  
RUN add-apt-repository -y ppa:chris-lea/node.js && \  
apt-get update && \  
apt-get install -y nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g n  
  
# Preinstall common iojs versions  
RUN n io 2.5.0  
RUN n 4.0.0  
RUN n 4.1.0  
RUN n 4.1.2  
  
ENV NPM_VERSION 3.3.7  
RUN npm install -g npm@${NPM_VERSION}  
  
CMD [ "node" ]  

