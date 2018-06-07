FROM geekykaran/headless-chrome-node-docker:latest  
  
RUN apt-get update && \  
apt-get install git -y && \  
apt-get clean autoclean  
  
RUN npm install -g ember-cli@2.15.1 bower  
  
EXPOSE 4200 35729  
WORKDIR /usr/src/app  

