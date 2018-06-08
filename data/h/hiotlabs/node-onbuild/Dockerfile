FROM node:latest  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install packeges to a directory above the project. Modules will still be
found  
# but won't be overridden when mounting the project directory for development.  
# Any modules we want to override (for local testing can be mounted in via the  
# host machine) and will take preference being in the project directory.  
ONBUILD WORKDIR /usr/src  
ONBUILD COPY package.json /usr/src/  
ONBUILD RUN npm install  
ONBUILD COPY . /usr/src/app  
  
# Reset working dir for running project.  
ONBUILD WORKDIR /usr/src/app  
# Make all local package binaries available.  
ONBUILD ENV PATH ../node_modules/.bin:$PATH  
  
# Don't use npm for running node, it doesn't forward SIGTERM.  
CMD [ "node", "app.js" ]  

