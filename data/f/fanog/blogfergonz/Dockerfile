FROM node:boron  
  
# Crear directorio de la app  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Instalar dependencias  
COPY package.json /usr/src/app  
RUN npm install  
  
# Empaquetar codigo  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

