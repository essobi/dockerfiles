# Imagen base  
FROM node:latest  
  
# Directorio de trabajo de la app  
WORKDIR /app  
  
# Copia de archivos: Hay que ejecutar en el directorio de la aplicacion (o
donde se referencia en .)  
ADD . /app  
  
# Dependencias: Le forzamos a que busque las dependencias del desarrollo Node
que empaquetamos  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Puerto a exponer fuera del contenedor  
EXPOSE 3000  
# Comando de ejecución de la aplicacion, primero comando principal y luego
parametros  
CMD ["npm", "start"]  

