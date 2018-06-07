FROM ubuntu:trusty  
  
MAINTAINER team@lastbackend.com  
  
# Install RabbitMQ  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F7B8CEA6056E8E56
&& \  
echo "deb http://www.rabbitmq.com/debian/ testing main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y rabbitmq-server pwgen && \  
rabbitmq-plugins enable rabbitmq_management && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "ERLANGCOOKIE" > /var/lib/rabbitmq/.erlang.cookie  
RUN chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie  
RUN chmod 400 /var/lib/rabbitmq/.erlang.cookie  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
EXPOSE 5672  
EXPOSE 15672  
CMD ["/init.sh"]

