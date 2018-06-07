FROM node:5.0.0-slim  
  
RUN apt-get update && apt-get install -y vim && apt-get clean  
  
RUN npm install -g nodemon; \  
npm install express; \  
npm install underscore;  
  
ADD . /app  
  
WORKDIR /app  
  
VOLUME ["/app"]  
  
EXPOSE 8000  
#CMD ["nodemon","app.js"]  
CMD nodemon -L --watch app.js  

