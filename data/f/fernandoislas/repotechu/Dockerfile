#imagen de la que parto  
FROM node:slim  
#carpeta de la app  
WORKDIR /miapp  
#Copia todos los archivos de api a la nueva app  
ADD . /miapp  
#paquetes necesarios  
RUN npm install  
#Puerto que expongo  
VOLUME /datos  
EXPOSE 3000  
#Comando de inicio  
CMD ["npm", "start"]  

