FROM node  
RUN npm install -g json-server  
VOLUME /data  
WORKDIR /data  
  
CMD ["json-server", "--watch", "db.json"]  
EXPOSE 3000

