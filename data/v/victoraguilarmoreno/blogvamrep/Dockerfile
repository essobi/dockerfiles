FROM node:boron  
##con esto me olvido de definir que que hay que instalar , es una plantilla de
la web en github  
  
##crear directorio de la app  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/scr/app  
  
## instalar las dependencies ¿donde estan? en package json  
COPY package.json /usr/src/app  
RUN npm install  
  
# Empaquetar codigo , copiamos todo el codigo , pero pedire que no se copien
cierto fichero para que sean mas ligeros y se los descargue  
COPY . /usr/src/app  
  
# al meter express en un contedor no se puede ver el puerto , necesito abrir
un puerto de salida al contenedor  
#expon el 80 81 y luego lanzo igual que la linea de comandos  
# para lanzarlo en la consola hay que poner sudo docker run -p 8082:8081 -d
vam/blogvam y sale una clave que indica que ok  
#el 8081 esta dentro del contenedor y el 8082 es el exterior  
#para ejecutarlo poner en la consola curl http://localhost:8082  
EXPOSE 8081  
CMD [ "npm", "start"]  

