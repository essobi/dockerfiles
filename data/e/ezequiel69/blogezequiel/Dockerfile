FROM node:boron  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
  
# Instalar dependencias  
RUN npm install -g \  
polymer-cli \  
bower  
  
COPY . /usr/src/app  
COPY ./src /usr/src/app  
COPY ./bower_components /usr/src/app  
COPY ./images /usr/src/app  
  
EXPOSE 8081  
CMD [ "npm", "start" ]  

