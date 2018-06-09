FROM node:7.3.0-alpine  
  
MAINTAINER joseangeldiazg <joseadiazg02@correo.ugr.es>  
  
#Añadimos usuario y grupo  
RUN addgroup -S ms && adduser -S -g ms tareas  
USER tareas  
  
  
#Creamos el directorio de la aplicación  
RUN mkdir -p /home/tareas/tareas  
WORKDIR /home/tareas/tareas  
  
#Instalamos las dependencias  
#Referencia https://nodejs.org/en/docs/guides/nodejs-docker-webapp/  
COPY package.json /home/tareas/tareas  
RUN npm install  
  
CMD [ "npm", "start" ]  

