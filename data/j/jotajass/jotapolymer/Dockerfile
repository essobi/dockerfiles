FROM node:boron  
  
# Crear directorio de la aplicacion  
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
RUN bower install polymerelements/app-layout --save --allow-root  
RUN bower install polymerelements/app-route --save --allow-root  
RUN bower install polymerelements/paper-icon-button --save --allow-root  
RUN bower install polymerelements/iron-pages --save --allow-root  
RUN bower install polymerelements/iron-selector --save --allow-root  
RUN bower install polymerelements/paper-item --save --allow-root  
RUN bower install polymerelements/paper-listbox --save --allow-root  
RUN bower install collaborne/paper-alert-dialog --save --allow-root  
RUN bower install polymerelements/paper-card --save --allow-root  
RUN bower install polymerelements/paper-fab --save --allow-root  
RUN bower install polymerelements/paper-menu-button --save --allow-root  
RUN bower install polymerelements/paper-dialog --save --allow-root  
RUN bower install polymerelements/iron-form --save --allow-root  
RUN bower install polymerelements/paper-input --save --allow-root  
RUN bower install polymerelements/paper-button --save --allow-root  
RUN bower install polymerelements/paper-toast --save --allow-root  
  
# Empaquetar codigo  
COPY . /usr/src/app  
COPY ./src /usr/src/app  
#COPY ./bower_components /usr/src/app  
COPY ./images /usr/src/app  
  
# Exponer puerto  
EXPOSE 8081  
# CMD lanza el motor de Docker  
CMD [ "npm", "start" ]  

