# Para aprovechar la plantilla existente en hub.docker.com que instala Node y
NPM  
FROM node:boron  
  
# Crear directorio de la app  
RUN mkdir -p /usr/src/app  
  
# Indicar la carpeta de trabajo  
WORKDIR /usr/src/app  
  
# Instalar dependencias  
COPY package.json /usr/src/app  
RUN npm install  
  
RUN npm install -g bower  
RUN bower install polymerelements/iron-ajax --save --allow-root  
RUN bower install polymerelements/paper-spinner --save --allow-root  
RUN bower install polymerelements/iron-icons --save --allow-root  
  
# Empaquetar código  
COPY . /usr/src/app  
COPY ./src /usr/src/app  
COPY ./images /usr/src/app  
#COPY ./bower_components /usr/src/app  
# Exponer el puerto  
EXPOSE 8081  
# Lanzar servidor  
CMD [ "npm", "start" ]  

