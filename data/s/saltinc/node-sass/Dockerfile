FROM node:5-slim  
  
RUN apt-get update && apt-get install -y git python && rm -rf
/var/lib/apt/lists/*  
  
RUN npm install -g node-sass  
  
WORKDIR /work  
  
RUN usermod -a -G users www-data  
  
RUN chown -R www-data:www-data /work  

