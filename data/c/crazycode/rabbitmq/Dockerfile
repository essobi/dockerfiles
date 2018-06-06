FROM debian:wheezy  
  
MAINTAINER crazycode  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add files.  
ADD bin/rabbitmq-start /usr/local/bin/  
  
RUN apt-get update \  
&& apt-get install -y wget  
  
# Install RabbitMQ.  
RUN wget -qO - http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-
key add -  
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >
/etc/apt/sources.list.d/rabbitmq.list  
RUN apt-get update && \  
apt-get install -y rabbitmq-server && \  
apt-get -qq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rabbitmq-plugins enable rabbitmq_management && \  
echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config &&
\  
chmod +x /usr/local/bin/rabbitmq-start  
  
# Define environment variables.  
ENV RABBITMQ_LOG_BASE /data/log  
ENV RABBITMQ_MNESIA_BASE /data/mnesia  
  
# Define mount points.  
VOLUME ["/data/log", "/data/mnesia"]  
  
# Define working directory.  
WORKDIR /data  
  
# Expose ports.  
EXPOSE 5672  
EXPOSE 15672  
# Define default command.  
CMD ["rabbitmq-start"]  

