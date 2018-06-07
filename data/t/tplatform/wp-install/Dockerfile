FROM debian:jessie  
  
RUN apt-get update && apt-get install -y curl mysql-client php5 php5-mysql  
RUN curl -O "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar" && chmod +x wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp  
  
ADD run.sh /tmp/run.sh  
RUN chmod +x /tmp/run.sh  
  
WORKDIR /tmp  
  
VOLUME /var/www/html  
  
ENTRYPOINT ["/tmp/run.sh"]  
  

