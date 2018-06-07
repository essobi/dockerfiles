FROM node:6-alpine  
  
ENV NEWMAN_VERSION="3.9.4"  
RUN npm install -g newman@${NEWMAN_VERSION}  
  
WORKDIR /etc/newman  
  
ENTRYPOINT ["newman"]  

