FROM node:alpine  
  
# Create app directory  
WORKDIR /usr/src/gallery_ui  
  
# Install app dependencies  
COPY package.json package-lock.json yarn.lock ./  
  
RUN npm install  
  
# Bundle app  
COPY . .  
  
EXPOSE 4200  
RUN npm run build  
  
CMD ["npm", "start"]  

