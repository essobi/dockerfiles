FROM node:7.8  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm set progress false && npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Build  
RUN npm run build  
  
EXPOSE 5121  
ENV NODE_ENV=production  
CMD ["npm", "start"]

