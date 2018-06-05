FROM node  
MAINTAINER Melissa Anderson <melissa@happypunch.com>  
  
# Set the version of NarraFirma  
ENV NF_VERSION 0.9.2  
# Temporary superuser name and password. These should be overridden when  
# the container is run  
ENV NF_SUPERUSER superuser  
ENV NF_PASSWORD password  
  
# Get dependencies  
RUN apt-get install curl  
RUN npm install -g typescript  
  
# Run as a non-privileged user  
RUN groupadd -r narrafirma && useradd -r -m -g narrafirma narrafirma  
USER narrafirma  
WORKDIR /home/narrafirma  
  
# Get narrafirma  
RUN curl -LO
https://github.com/pdfernhout/narrafirma/archive/v$NF_VERSION.tar.gz  
RUN tar -xzvf v$NF_VERSION.tar.gz  
  
# Compile the javascript. true is set to allow the build to complete despite
tsc errors.  
WORKDIR /home/narrafirma/narrafirma-$NF_VERSION/webapp/js  
RUN tsc; true  
  
# Run the application  
WORKDIR /home/narrafirma/narrafirma-$NF_VERSION/server  
CMD node admin.js update-superuser $NF_SUPERUSER $NF_PASSWORD && node
NarraFirmaServer.js  

