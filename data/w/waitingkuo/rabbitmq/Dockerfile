# RabbitMQ  
# ========  
#  
# Build:  
#  
# docker build -t waitingkuo/rabbitmq .  
#  
# Run:  
#  
# docker run -d -h rabbithost -p :5672 -p :15672 -v
/path/to/rabbitmq/mnesia:/var/lib/rabbitmq/mnesia -v
/path/to/log:/var/log/rabbitmq waitingkuo/rabbitmq  
#  
# VERSION 0.1  
#  
FROM ubuntu:latest  
MAINTAINER waitingkuo0527@gmail.com  
  
  
# Hack for initctl no being available in Ubuntu  
# https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
# Install RabbitMQ  
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" | tee
/etc/apt/sources.list.d/rabbitmq.list  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 0x056E8E56  
RUN apt-get update  
RUN apt-get install -y rabbitmq-server  
  
# Enable Management tool  
RUN rabbitmq-plugins enable rabbitmq_management  
  
# Export port for amqp and web console  
EXPOSE 5672 15672  
CMD /usr/sbin/rabbitmq-server  

