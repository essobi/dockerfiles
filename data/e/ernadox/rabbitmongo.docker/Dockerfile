FROM rabbitmq:3-management  
  
COPY scripts/install.mongo.sh /usr/local/bin/  
RUN chmod 777 /usr/local/bin/install.mongo.sh &&
/usr/local/bin/install.mongo.sh  
  
ENV RABBITMQ_DEFAULT_USER=messagebus  
ENV RABBITMQ_DEFAULT_PASS=messagebus  
ENV RABBITMQ_DEFAULT_VHOST=sports_api  
  
#COPY scripts/start.sh /usr/local/bin/  
#RUN chmod 777 /usr/local/bin/start.sh  
RUN apt-get update && apt-get install -y openssh-server apache2 supervisor  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
COPY scripts/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY scripts/docker-mongo-entrypoint.sh /usr/local/bin/docker-mongo-
entrypoint.sh  
RUN chmod 777 /usr/local/bin/docker-mongo-entrypoint.sh  
  
EXPOSE 4369 5671 5672 25672 15672 27017  
CMD ["/usr/bin/supervisord"]  

