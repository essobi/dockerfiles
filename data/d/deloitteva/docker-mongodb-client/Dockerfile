FROM mongo:3.0.1  
MAINTAINER Justin Grant "http://www.justinleegrant.com"  
# copy test queries for MongoDB  
COPY test_queries/*.js /bootstrap/test_queries/  
  
# default command  
CMD ["sh", "-c", "exec mongo
$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"]  

