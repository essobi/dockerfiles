FROM node:8.4  
WORKDIR /starterfiles  
ADD . .  
  
RUN apt-get -y update && \  
apt-get -y install build-essential  
  
RUN npm install -g gulp && \  
npm install -g node-gyp && \  
npm install  
  
CMD gulp  

