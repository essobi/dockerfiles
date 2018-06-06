FROM node  
  
RUN npm install -g redis-commander  
  
EXPOSE 8081  
CMD redis-commander --redis-host ${REDIS_PORT_6379_TCP_ADDR}  

