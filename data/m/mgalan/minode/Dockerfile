# Imagen base  
FROM node:latest  
  
# Directorio de la app  
WORKDIR /app  
  
# Copio archivos  
ADD . /app  
  
# Dependencias  
RUN npm install  
  
# Puerto  
EXPOSE 3000  
CMD ["npm", "start"]

