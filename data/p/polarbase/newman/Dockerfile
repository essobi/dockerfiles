FROM node:alpine  
ENV NEWMAN_VERSION 3.8.2  
RUN npm install -g newman@${NEWMAN_VERSION};  
  
WORKDIR /etc/newman  
CMD ["newman"]  

