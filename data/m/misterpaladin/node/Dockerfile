FROM node:4.4.4  
MAINTAINER Eugene Min <e.min@milax.com>  
  
RUN apt-get update -y && apt-get install -y sudo  
RUN npm i -g npm  
RUN npm i -g gulp-cli  
RUN npm i -g coffee-script  
RUN npm i -g bower  
ENV DEBIAN_FRONTEND noninteractive  
RUN useradd -ms /bin/bash node  
RUN echo "node ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers  
USER node  
VOLUME ["/home/node"]  
WORKDIR /home/node

