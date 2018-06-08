FROM node  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3030  
EXPOSE 80  
EXPOSE 443  
CMD ["npm", "run", "start:prod"]  

