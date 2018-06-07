  
FROM node:9.5.0  
  
VOLUME /cache  
  
RUN apt-get update && apt-get install -y ocaml libelf-dev  
  
# NPM: cache  
RUN npm config set cache /cache/.npm  
RUN npm config set spin false  
RUN npm config set progress false  

