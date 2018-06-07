#  
# --build-arg port=port_number  
#  
FROM node:carbon  
  
ARG port=3000  
ENV PORT=$port  
  
WORKDIR /hatmelia/server  
  
# Install app dependencies  
COPY package.json package-lock.json ./  
  
RUN npm install \--only=production  
  
# Bundle app source  
COPY . .  
  
# start the server  
CMD [ "npm", "start" ]  

