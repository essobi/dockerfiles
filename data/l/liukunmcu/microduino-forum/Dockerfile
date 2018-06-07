FROM liukunmcu/docker-node  
  
WORKDIR /app  
ADD . /app  
RUN apt-get update  
RUN apt-get install -y expect  
RUN npm install --production  
CMD ./setup.sh&&./nodebb upgrade&&cp config.json.bak config.json&&./nodebb
start && ./nodebb log  
EXPOSE 4567  

