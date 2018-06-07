#  
# Bases on https://registry.hub.docker.com/u/dockerfile/rabbitmq/  
#  
FROM centos:centos7  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
ENV RABBITMQ_VERSION 3.4.1  
#EPEL + Erlang  
RUN rpm -Uhv http://mirrors.einstein.yu.edu/epel/7/x86_64/e/epel-
release-7-2.noarch.rpm \  
&& yum install -y erlang  
  
#RabbitMQ  
RUN DIR=$(mktemp -d) \  
&& cd ${DIR} \  
&& rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc \  
&& curl -O -L http://www.rabbitmq.com/releases/rabbitmq-
server/v${RABBITMQ_VERSION}/rabbitmq-server-${RABBITMQ_VERSION}-1.noarch.rpm \  
&& yum install -y rabbitmq-server-${RABBITMQ_VERSION}-1.noarch.rpm \  
&& rabbitmq-plugins enable rabbitmq_management \  
&& echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config
\  
&& rm -rf ${DIR}  
  
# Aux folders  
RUN mkdir -p /var/lock/subsys/ \  
&& mkdir -p /opt/rabbitmq/log \  
&& mkdir -p /opt/rabbitmq/mnesia \  
&& chown -R rabbitmq:rabbitmq /opt/rabbitmq  
  
# Define environment variables.  
ENV RABBITMQ_LOG_BASE /opt/rabbitmq/log  
ENV RABBITMQ_MNESIA_BASE /opt/rabbitmq/mnesia  
  
# Define mount points.  
VOLUME ["/opt/rabbitmq/log", "/opt/rabbitmq/mnesia"]  
  
# Define working directory.  
WORKDIR /opt  
  
# Define default command.  
CMD ["rabbitmq-server"]  
  
# Expose ports.  
EXPOSE 5672  
EXPOSE 15672

