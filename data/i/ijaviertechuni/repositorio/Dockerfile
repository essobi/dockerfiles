FROM node:boron  
  
#Crear directorio de la APP  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
#Instalar las dependencias.  
COPY package.json /usr/src/app  
RUN npm install  
  
# Añadir ficheros desarrollo.  
COPY . /usr/src/app  
  
EXPOSE 8081  
#Levantar la aplicacion  
CMD ["npm", "start"]  

