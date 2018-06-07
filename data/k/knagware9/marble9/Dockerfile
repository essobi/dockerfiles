FROM node:6.11  
WORKDIR /  
RUN git clone https://github.com/knagware9/marbles  
WORKDIR /marbles  
RUN rm -rf node_modules && npm install && npm install -g gulp  
ADD marbles_container_service.json /marbles/config/marbles_local.json  
ADD blockchain_container_service.json /marbles/config/.  

