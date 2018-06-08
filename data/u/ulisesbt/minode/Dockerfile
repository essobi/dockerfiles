#Imagen base  
FROM node:latest  
  
# Directorio de la app  
WORKDIR /app  
  
# Copia de archivos  
ADD . /app  
  
# Dependencias  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Puertos  
EXPOSE 3000  
# Variables de entorno (nosotros no tenemos)  
# Command  
CMD ["npm", "start"]  

