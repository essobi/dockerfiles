# Imagen base  
FROM ubuntu  
  
# Actualizamos los repositorios para instalar las herramientas adecuadas  
RUN apt-get update && apt-get install -y net-tools apache2  
  
# Exponemos los puertos típicos de apache  
EXPOSE 80  
# Copiamos los permisos de ejecución  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x entrypoint.sh  
  
CMD ["/entrypoint.sh"]

