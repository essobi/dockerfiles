FROM impulsecloud/ic-ubuntu:latest  
# Forked from tutum/haproxy  
MAINTAINER Johann du Toit <johann@winkreports.com>  
  
# Install RabbitMQ  
RUN wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-
key add - && \  
echo "deb http://www.rabbitmq.com/debian/ testing main" | tee
/etc/apt/sources.list.d/rabbitmq.list && \  
apt-get update && \  
apt-get install -y rabbitmq-server pwgen && \  
rabbitmq-plugins enable rabbitmq_management && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "ERLANGCOOKIE" > /var/lib/rabbitmq/.erlang.cookie  
RUN chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie  
RUN chmod 400 /var/lib/rabbitmq/.erlang.cookie  
  
# Add scripts  
ADD run.sh /run.sh  
ADD set_rabbitmq_password.sh /set_rabbitmq_password.sh  
RUN chmod 755 ./*.sh  
  
# Enable management  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
  
EXPOSE 5672 15671 15672  
CMD ["/run.sh"]  

