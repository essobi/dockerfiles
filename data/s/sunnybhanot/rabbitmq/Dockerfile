#####  
##  
# Dockerfile for RabbitMQ  
##  
#####  
FROM sunnybhanot/ubuntu  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F7B8CEA6056E8E56
\  
&& echo "deb http://www.rabbitmq.com/debian/ testing main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y rabbitmq-server \  
&& rabbitmq-plugins enable rabbitmq_management \  
&& echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5672 15672 4369  
  
CMD /usr/sbin/rabbitmq-server  

