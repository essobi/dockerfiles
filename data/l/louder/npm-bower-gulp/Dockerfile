FROM node:4.2.2  
  
RUN npm upgrade -g npm  
RUN npm install -g gulp  
RUN npm install -g bower  
  
RUN git config \--global url."https://".insteadOf git://  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  

