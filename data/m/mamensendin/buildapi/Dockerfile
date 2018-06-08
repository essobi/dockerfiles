#imagen raiz  
FROM node  
# CARPETA RAIZ  
WORKDIR /apitechu  
#copia de archivos  
ADD . /apitechu  
#Instalo los paquetes necesarios  
RUN npm install  
#volumen de la imagen  
VOLUME ["/logs"]  
# Puerto que expone  
EXPOSE 3000  
# Comando de inicio  
CMD ["npm", "start"]  

