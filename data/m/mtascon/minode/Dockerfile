# Imagen base  
FROM node:latest  
  
# Directorio de la app  
WORKDIR /app  
  
# Copio archivos del proyecto Node.js  
ADD . /app  
  
# Dependencias  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Puerto  
EXPOSE 3000  
# Command  
CMD ["npm","start"]  

