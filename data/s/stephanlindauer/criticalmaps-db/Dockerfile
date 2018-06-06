FROM node:7-alpine  
  
RUN npm install -g node-pg-migrate pg --silent  
  
COPY migrations/ /migrations/  
  
ENTRYPOINT ["pg-migrate"]  

