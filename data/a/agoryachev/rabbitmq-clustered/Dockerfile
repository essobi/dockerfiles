FROM rabbitmq:management  
  
COPY rabbitmq-clustered /usr/local/bin/  
  
RUN apt-get update && apt-get install -y telnet curl && rm -rf
/var/lib/apt/lists/*  
  
CMD ["rabbitmq-clustered"]  

