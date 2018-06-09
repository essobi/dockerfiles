FROM node:alpine  
  
ADD package.json package.json  
RUN npm install  
  
ADD . .  
  
COPY config-template.json config.json  
  
LABEL databox.type="databox-app-server"  
  
EXPOSE 8080 8181  
CMD ["npm","start"]

