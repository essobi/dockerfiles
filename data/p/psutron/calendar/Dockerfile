FROM node:6  
# Create app directory  
WORKDIR /usr/src/app  
  
# Bundle app source  
COPY . .  
RUN npm install --save mongodb  
RUN npm install  
EXPOSE 3000  
CMD [ "npm", "start" ]

