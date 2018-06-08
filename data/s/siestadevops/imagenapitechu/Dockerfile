# Imagen origen  
FROM node  
  
# Carpeta raíz  
WORKDIR /apitechu  
  
# Copia de archivos [origen:carpeta de mi PC] [destino:carpeta en docker]  
ADD . /apitechu  
  
#Instalación de los paquetes necesarios  
RUN npm install  
  
#Volumen de la imagen (esta es la carpeta de mi contenedor, y luego en el run
le indicaré contra que  
#carpeta local del host lo mapeo)  
VOLUME ["/logs"]  
  
# Puerto que expone mi imagen  
EXPOSE 4000  
#Comando de iniciado: Cuando yo haga run en el contenedor que tiene que HACER  
CMD ["npm" , "start"]  

