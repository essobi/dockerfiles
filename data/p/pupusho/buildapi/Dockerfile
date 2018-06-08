# Imagen raiz  
FROM node  
# carpeta raíz  
WORKDIR /apitechu  
# Copia de archivos  
ADD . /apitechu  
# instalo los paquetes necesarios  
RUN npm install  
# Volumen de la imagen  
VOLUME ["/logs"]  
# Puerto que expone  
EXPOSE 3000  
# Comando de iniciado  
CMD ["npm", "start"]  

