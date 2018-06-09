# Ntipa RabbitMQ  
FROM ubuntu:trusty  
MAINTAINER Tindaro Tornabene <tindaro.tornabene@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
ADD rabbitmq-signing-key-public.asc /tmp/rabbitmq-signing-key-public.asc  
RUN apt-key add /tmp/rabbitmq-signing-key-public.asc  
  
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >
/etc/apt/sources.list.d/rabbitmq.list  
RUN apt-get -y update  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN apt-get install -yqq inetutils-ping net-tools rabbitmq-server  
  
RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_management  
RUN /usr/sbin/rabbitmq-plugins enable enable rabbitmq_stomp  
RUN /usr/sbin/rabbitmq-plugins enable enable rabbitmq_shovel  
RUN echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config  
  
ADD set_rabbitmq_password.sh /set_rabbitmq_password.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
RUN /run.sh  
  
#ENV RABBITMQ_MNESIA_DIR /data/  
ENV RABBITMQ_LOG_BASE /data/log  
ENV RABBITMQ_MNESIA_BASE /data/mnesia  
  
# Define mount points.  
VOLUME ["/data/log", "/data/mnesia"]  
  
# Define working directory.  
WORKDIR /data  
  
# Add files.  
ADD rabbitmq-start /usr/local/bin/  
RUN chmod +x /usr/local/bin/rabbitmq-start  
  
USER root  
  
EXPOSE 5672 15672 4369 61613 25672 4369  
CMD ["/usr/local/bin/rabbitmq-start"]

