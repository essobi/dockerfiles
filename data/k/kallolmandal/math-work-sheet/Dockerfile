FROM node  
  
MAINTAINER Kallol Mandal  
  
COPY . /var/www  
  
WORKDIR /var/www  
  
RUN npm install -g bower  
  
RUN npm install --production  
  
ENTRYPOINT ["npm","run", "start"]

