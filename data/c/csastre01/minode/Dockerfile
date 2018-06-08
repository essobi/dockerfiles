# imagen base  
FROM node:latest  
  
# Directorio trabajo de la app  
WORKDIR /app  
  
# Copiar Archivos a directorio trabajo  
ADD . /app  
  
# Dendencias. Lo que venga en el package.json. npm install busca en el
packge.jason y lo otro es para instalar vi  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Puerto. Es el 3000. Podría poner otro  
EXPOSE 3000  
# Variables de entorno NO HAY  
# Comando que ejecuta mi app  
CMD ["npm", "start"]  
# Alternativo  
# CMD ["node", "server.js"]  

