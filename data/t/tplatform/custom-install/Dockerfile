FROM debian:jessie  
  
RUN apt-get update && apt-get install -y curl mysql-client php5 php5-mysql  
  
ADD run.sh /tmp/run.sh  
RUN chmod +x /tmp/run.sh  
  
WORKDIR /tmp  
  
VOLUME /var/www/html  
  
ENTRYPOINT ["/tmp/run.sh"]  
  

