# Imagen base  
FROM node:latest  
  
# Directorio de trabajo de la app  
WORKDIR /server  
  
#Copio archivos  
ADD . /server  
  
#Dependencias  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
#Puerto  
EXPOSE 3000  
  
#Comando  
CMD ["npm", "start"]  

