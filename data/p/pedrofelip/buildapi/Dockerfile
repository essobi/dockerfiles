# Imagen Raiz  
FROM node  
#carpeta raiz  
WORKDIR /apitechu  
#copia de archivos  
ADD . /apitechu  
#Instalo los paquetes necesarios  
RUN npm install  
RUN npm install nodemailer  
RUN npm install cors  
#volumen de la imagen  
VOLUME ["/logs"]  
# puerto que expone  
EXPOSE 3000  
# Comando de inicio  
CMD ["npm","start"]  

