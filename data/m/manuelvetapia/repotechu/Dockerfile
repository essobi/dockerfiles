##imagen de la que parto, 6.12.3, 6.12, 6, boron (6/Dockerfile)  
FROM node:6.12.3  
##carpeta de la app  
WORKDIR /miapp  
## copia todos los archivos de la carpte "." a la carpeta /miapp  
ADD . /miapp  
## podria poner los paquetes necesarios pero ya se encuentran instalados RUN
npm install  
RUN npm install  
##Puerto que expongo  
EXPOSE 3000  
##Comandos de inicio a modo de arreglo  
CMD ["npm", "start"]  

