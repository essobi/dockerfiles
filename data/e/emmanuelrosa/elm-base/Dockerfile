FROM node:latest  
MAINTAINER Emmanuel Rosa "emmanuel_rosa@aol.com"  
ENV SRC="/source"  
RUN npm install -g elm@0.18.0 && mkdir $SRC  
WORKDIR $SRC  
VOLUME ["/root/.elm"]  
RUN elm-package install -y  

