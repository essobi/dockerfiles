FROM node:7.3.0-alpine  
  
MAINTAINER joseangeldiazg <joseadiazg02@correo.ugr.es>  
  
#Añadimos usuario y grupo  
RUN addgroup -S ms && adduser -S -g ms roles  
USER roles  
  
  
#Creamos el directorio de la aplicación  
RUN mkdir -p /home/roles/roles  
WORKDIR /home/roles/roles  
  
#Instalamos las dependencias  
#Referencia https://nodejs.org/en/docs/guides/nodejs-docker-webapp/  
COPY package.json /home/roles/roles  
RUN npm install  
  
CMD [ "npm", "start" ]  

