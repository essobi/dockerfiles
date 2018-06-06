FROM mhart/alpine-node:6  
ENV SENTINEL_HOST ${SENTINEL_HOST}  
ENV SENTINEL_PORT ${SENTINEL_PORT}  
  
WORKDIR /src  
ADD . .  
  
RUN npm install --production  
RUN npm install -g redis-commander  
  
EXPOSE 5000  
EXPOSE 8081  
CMD ["sh", "-c", "npm start & redis-commander --sentinel-host $SENTINEL_HOST
\--sentinel-port $SENTINEL_PORT"]  

