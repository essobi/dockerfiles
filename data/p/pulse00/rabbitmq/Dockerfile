FROM stackbrew/ubuntu:13.10  
MAINTAINER Robert Gruendler <robert@dubture.com>  
  
# Install RabbitMQ  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade &&
DEBIAN_FRONTEND=noninteractive apt-get install -y rabbitmq-server  
RUN rabbitmq-plugins enable rabbitmq_management  
  
# Add scripts  
ADD run.sh /run.sh  
ADD set_rabbitmq_password.sh /set_rabbitmq_password.sh  
RUN chmod 755 ./*.sh  
  
EXPOSE 5672 15672  
CMD ["/run.sh"]

