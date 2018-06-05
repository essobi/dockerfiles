FROM profideo/php-5.6.20-fpm  
  
# Configure logstash-forwarder  
RUN echo 'deb http://packages.elastic.co/logstashforwarder/debian stable main'
| tee /etc/apt/sources.list.d/logstashforwarder.list  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add
-  
RUN apt-get -qq update && apt-get install logstash-forwarder  
RUN mkdir -p /etc/pki/tls/certs  
COPY files/logstash-forwarder.crt /etc/pki/tls/certs/logstash-forwarder.crt  
RUN chown profideo:profideo /etc  
  
# Node  
RUN apt-get update && apt-get install -y curl python-software-properties  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get update && apt-get install -y nodejs  
RUN mkdir -p /home/profideo/.npm  
RUN chown -R profideo /home/profideo/.npm  
RUN npm install -g less  
RUN npm install -g bower  
  
# PHP configuration  
COPY files/php.ini /usr/local/etc/php/php.ini  
  
# Supervisor  
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

