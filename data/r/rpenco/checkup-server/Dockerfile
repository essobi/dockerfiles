FROM node:6.5  
MAINTAINER R. Penco <github.com/rpenco>  
  
RUN mkdir -p /src  
  
WORKDIR /src  
  
RUN git clone https://github.com/rpenco/checkup-server .  
  
RUN npm install \  
&& npm run compile  
  
VOLUME /src/shared  
  
ENV CONFIGFILE "/src/shared/configuration.yml"  
ENV DBFILE "/src/shared/db.json"  
EXPOSE 8080  
CMD [ "npm", "run", "start:only" ]  

