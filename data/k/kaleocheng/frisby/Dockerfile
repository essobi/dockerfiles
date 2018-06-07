FROM node:alpine  
RUN npm install -g jest frisby  
WORKDIR /app  
RUN echo '{"name":"jest"}' > package.json  
CMD ["jest"]  

