FROM node:0.12  
# Create folder to store and run the app  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# install project npm modules  
# We install to a directory above the project so that modules will still be
found  
# but won't be overridden when mounting the project directory for development  
# Any modules we want to override (for local testing can be mounted in via the  
# host machine) and will take preference being in the project directory  
ONBUILD COPY ./package.json /usr/src/  
ONBUILD WORKDIR /usr/src  
ONBUILD RUN npm install  
  
# Reset working dir for runing project commands  
ONBUILD WORKDIR /usr/src/app  

