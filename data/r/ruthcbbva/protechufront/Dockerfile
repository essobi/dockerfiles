# Imagen base  
FROM node:latest  
  
# Directorio de trabajo de la app  
WORKDIR /app  
  
#Copio archivos  
ADD /build/default /app/build/default  
ADD package.json /app  
ADD server.js /app  
  
#Dependencias  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
#Puerto  
EXPOSE 2990  
  
#Comando  
CMD ["npm", "start"]  

