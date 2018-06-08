FROM node:carbon  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
ENV NODE_ENV=production  
  
# Bundle app source  
COPY . /usr/src/app  
  
RUN npm run build  
EXPOSE 3000  
CMD [ "npm", "start" ]

