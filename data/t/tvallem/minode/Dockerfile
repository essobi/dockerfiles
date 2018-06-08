# Imagen base sobre la última versión  
FROM node:latest  
  
# Directorio de la app (el que queramos)  
WORKDIR /app  
  
# Copia de archivos (todos los ficheros que están a nivel del fichero
Dockerfile, en el directorio raíz de la aplicación)  
ADD . /app  
  
# Dependencias (en este caso, las que están dentro del package.json)  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
#Puertos (en el arranque del contenedor debo asociar este puerto del
contenedor al puerto físico de la máquina donde se levanta el contenedor)  
EXPOSE 3000  
# Variables de entorno (no tengo)  
# Comandos (la primera es el comando principal y el resto suelen ser los
parámetros)  
CMD ["npm", "start"]  

