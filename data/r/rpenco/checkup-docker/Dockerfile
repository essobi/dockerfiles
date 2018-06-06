FROM node:6.5  
MAINTAINER R. Penco <github.com/rpenco>  
  
WORKDIR /  
  
# install server  
RUN git clone https://github.com/rpenco/checkup-server src  
  
WORKDIR /src  
  
RUN npm install  
  
# install client  
RUN git clone https://github.com/rpenco/checkup-client public  
  
WORKDIR public  
  
RUN npm install  
  
# share config and db  
ENV CONFIGFILE "/src/shared/configuration.yml"  
ENV DBFILE "/src/shared/db.json"  
EXPOSE 8080  
# start both  
WORKDIR /src  
  
RUN npm install -g concurrently http-server  
  
CMD [ "concurrently", "npm run start:prod", "http-server -p 8085" ]  

