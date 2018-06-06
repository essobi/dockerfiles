FROM qnib/d-node  
  
RUN npm install -g redis-commander  
ADD etc/consul.d/redis-commander.json /etc/consul.d/  
ADD etc/supervisord.d/redis-commander.ini /etc/supervisord.d/  
  

