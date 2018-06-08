# FROM node:5.9.1  
FROM mhart/alpine-node:5.9  
WORKDIR "/var/www/"  
COPY package.json package.json  
  
# everything gets loaded in as a volume (in docker-compose.override.yml),
including gulp  
RUN sh -c "npm install --production"  
  
EXPOSE 8080  
CMD ["node", "./server/index.js"]  

