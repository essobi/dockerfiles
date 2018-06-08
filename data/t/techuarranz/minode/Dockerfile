# Image Base  
FROM node:latest  
  
#Directorio de la APP  
WORKDIR /app  
  
#copio arhivos: todo lo que está a nivel del dockerfile  
ADD . /app  
  
#dependencias (lo que viene en el package.json)  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Puerto  
EXPOSE 3000  
#NO NECESITO DEFINIR VARIABLES DE ENTORNO  
# comand  
CMD ["npm", "start"]  

