FROM jermorin/node-opencv:latest  
  
MAINTAINER Jérémy Morin <hi@jermor.in>  
  
RUN npm install opencv-server-socket  
  
EXPOSE 3000  
CMD ["node", "/node_modules/opencv-server-socket/dist/index.js"]  

