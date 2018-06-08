#imagen de la que se parte  
FROM node:boron  
#directorio de trabajo  
WORKDIR /miapp  
#copiar archivos  
Add . /miapp  
#Paquetes necesarios  
RUN npm install  
#puerto que se expone  
EXPOSE 3000  
#comandos a ejecutar  
CMD ["npm","start"]  

