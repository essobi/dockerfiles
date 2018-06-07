# Imagen base  
FROM node:latest  
  
# Directorio de la app  
WORKDIR /app  
  
# Copio archivos  
ADD . /app  
  
# Dependencias  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Puerto --> el de la aplicación (npm run start)  
EXPOSE 3000  
# Comando  
CMD ["npm", "start"]  

