## Imagen de la que parto  
FROM node:boron  
## Carpeta de la app  
WORKDIR /miapp  
## Copia archivos  
ADD . /miapp  
## Comandos a ejecutar  
RUN ["npm", "install"]  
## Puerto que expongo  
EXPOSE 3000  
## Comando de inicio  
CMD ["npm", "start"]  

