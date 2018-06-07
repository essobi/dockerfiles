#imagen base  
FROM node:latest  
  
#directorio de la app  
WORKDIR /app  
  
#copio archivos  
ADD . /app  
  
# dependencias  
#RUN npm install  
RUN npm install  
RUN apt-get update  
Run apt-get install -y vim  
#puerto  
EXPOSE 3000  
#comand  
CMD ["npm", "start"]  

