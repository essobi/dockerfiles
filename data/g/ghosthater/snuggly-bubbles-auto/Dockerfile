FROM node:carbon  
  
# Create app directory  
WORKDIR /app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package.json ./  
  
RUN npm run setup  
  
# Bundle app source  
COPY . .  
  
EXPOSE 80  
CMD [ "npm", "run", "start" ]  

