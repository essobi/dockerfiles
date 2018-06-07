FROM rabbitmq:3.5-management  
MAINTAINER developers@khipu.com  
  
RUN groupmod -g 2000 rabbitmq && \  
usermod -u 2000 -g 2000 rabbitmq && \  
chown -R rabbitmq:rabbitmq /var/log/rabbitmq /var/lib/rabbitmq  
  
VOLUME /var/lib/rabbitmq  

