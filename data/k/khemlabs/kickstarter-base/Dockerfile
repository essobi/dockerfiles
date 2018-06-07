############################################################  
# Dockerfile to build NodeJS 4 Installed Containers  
# Based on Node:4.4.3  
############################################################  
  
FROM node:4.4.3  
  
ARG LISTEN_PORT=3000  
ARG API_HOST=/  
  
EXPOSE $LISTEN_PORT  
  
# Install dependencies  
RUN npm install -g gulp \  
forever \  
bower  
CMD [/bin/bash]  

