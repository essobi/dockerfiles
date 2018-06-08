FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
  
# Install app dependencies  
COPY package.json /usr/app/  
RUN yarn  
  
# Bundle app source  
COPY . /usr/app  
# Precompile with babel  
RUN npm run build  
  
CMD [ "npm", "run", "serve"]

