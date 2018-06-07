FROM node  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm set progress=false  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 8484  
CMD [ "npm", "start" ]  

