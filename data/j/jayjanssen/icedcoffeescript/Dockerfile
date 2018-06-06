FROM node:latest  
  
RUN apt-get update --fix-missing && apt-get dist-upgrade -y && apt-get install
-y npm git  
RUN npm install -g iced-coffee-script  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# simple tests  
RUN node --version  
RUN npm --version  
RUN iced --version  
RUN node --version | grep v6.4.0 && \  
npm --version | grep 3.10.3 && \  
iced --version | grep 108.0.11  

