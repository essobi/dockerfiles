FROM node:7.9.0-alpine  
  
RUN npm install pgb-weinre@0.9.1 -g --production  
  
USER node  
  
CMD ["weinre", "--boundHost", "0.0.0.0"]  

