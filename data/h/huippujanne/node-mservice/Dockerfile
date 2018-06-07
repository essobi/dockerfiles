FROM node:8-alpine  
USER node:node  
COPY index.js /home/node/index.js  
WORKDIR /home/node  
RUN npm install node-rest-client micro  
CMD [ "/home/node/node_modules/.bin/micro", "index.js" ]  

