FROM node:boron  
# Create app directory  
RUN mkdir -p /usr/src/konkerlogistica  
WORKDIR /usr/src/konkerlogistica  
# Install app dependencies  
COPY package.json /usr/src/konkerlogistica/  
RUN npm install  
# Bundle app source  
COPY . /usr/src/konkerlogistica  
EXPOSE 443  
EXPOSE 80  
CMD [ "npm", "start" ]  

