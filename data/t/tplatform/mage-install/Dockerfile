FROM debian:jessie  
  
RUN apt-get update && apt-get install -y wget curl zip unzip rsync mysql-
client php5 php5-mysql php5-mcrypt  
  
ADD run.sh /tmp/run.sh  
RUN chmod +x /tmp/run.sh  
  
WORKDIR /tmp  
  
VOLUME /var/www/html  
  
ENTRYPOINT ["/tmp/run.sh"]  
  

