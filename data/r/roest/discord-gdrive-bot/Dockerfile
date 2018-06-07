FROM node:carbon  
  
# Create app directory  
WORKDIR /usr/src/app  
  
RUN apt-get update && apt-get install -y \  
imagemagick \  
ghostscript \  
poppler-utils  
  
# Install app dependencies  
COPY package*.json ./  
  
RUN npm install --only=production  
  
# Bundle app source  
COPY . .  
  
CMD [ "node", "bot" ]

