# imagen base  
FROM node:latest  
  
# directorio de trabajo  
WORKDIR /app  
  
# copiamos archivos al nivel del Dockerfile  
ADD . /app  
  
# Dependencias  
RUN npm install  
RUN apt-get update && apt-get install vim -y  
  
# Abrir puerto  
EXPOSE 3000  
# comando  
CMD ["npm", "start"]  
  

