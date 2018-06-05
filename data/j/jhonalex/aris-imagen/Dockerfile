FROM nginx:1.11-alpine  
  
LABEL Descripcion="Pequeña muestra de Nginx" Autor="Jhonny Gomez"
Version="v1.0.0"  
  
RUN mkdir -p /var/www/vhosts && touch /var/www/vhosts/prueba.txt  
  
COPY index.html /usr/share/nginx/html/  

