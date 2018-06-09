#Imagen base  
FROM node:9.2.0  
  
# Directorio de la app  
WORKDIR /app  
  
#copiar archivos del proyecto a la carpeta que va a usar docker  
ADD . /app  
  
#dependencias  
RUN npm install  
  
#puerto  
EXPOSE 3000  
EXPOSE 3001  
  
# comando de arranque  
CMD ["npm", "start"]  
  
#ejemplo de linea para la generacion de la Imagen  
#docker build -t mlopez/server .  
  
#docker run -p 3000:3000 --net techui --name server -d mlopez/server  
  
#ejecutar la Imagen  
#docker run -p 3000:3000 -d mlopez/server  
  
#docker logs  
#docker -it  
#docker login  
#docker push torru/techuiapi  
#docker ps  
  
#para entrar al contenido del contenedor  
#docker exec -it id_container  
  
#borrar contenido de la imagen  
#docker image rmi id_container  
  
#https://hub.docker.com/r/torru/techuiapi/  
  
#url para autobuild  
#https://cloud.docker.com/api/build/v1/source/11ba5905-b93b-46dc-8b86-1f9b4d4364f6/trigger/bd711f90-203e-46fe-b9b1-07a42cfe04cd/call/  

