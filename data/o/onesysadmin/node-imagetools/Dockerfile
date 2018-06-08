FROM node:0.11  
  
# imagemagick already included in buildpack-deps, parent of node image  
RUN apt-get update \  
&& apt-get install -yq pdftk poppler-utils  

