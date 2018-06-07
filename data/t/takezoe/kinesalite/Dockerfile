FROM node:latest  
MAINTAINER Naoki Takezoe <takezoe [at] gmail.com>  
  
RUN npm install -g kinesalite  
RUN mkdir /var/kinesalite  
  
EXPOSE 4567  
VOLUME /var/kinesalite  
  
ENTRYPOINT ["kinesalite", "--path", "/var/kinesalite"]

