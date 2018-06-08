FROM node:boron  
#Image de la que parto  
WORKDIR /miapp  
#Carpeta de la app  
ADD . /miapp  
#Copia los archivos  
RUN npm install  
#Componentes  
EXPOSE 3000  
#Puerto que expongo  
CMD ["npm", "start"]  
#Comando de inicio  

