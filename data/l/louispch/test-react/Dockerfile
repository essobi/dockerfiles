FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/app/public  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
RUN npm run build  
  
EXPOSE 5000  
# RUN npm run serve  
# CMD [ "npm", “run”, “serve” ]  
CMD npm run serve  

