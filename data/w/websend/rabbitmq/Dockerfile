# NAME: Rabbitmq 3.6.5  
#  
# DESCRIPTION: Rabbitmq for development use  
#  
# NEEDED ENVS:  
#  
# USAGE EXAMPLE: docker run websend/rabbitmq  
# BUILD: docker build -t websend/rabbitmq:3.6.5-1 .  
FROM websend/debian:8.4  
MAINTAINER Ilja Krijger <i.krijger@websend.nl>  
  
RUN \  
wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \  
dpkg -i erlang-solutions_1.0_all.deb && \  
apt-get -q update && \  
apt-get install -yq logrotate && \  
apt-get install -yq esl-erlang=1:18.3.4 && \  
apt-get install -yq socat && \  
apt-get install -yq adduser && \  
apt-get install init-system-helpers  
  
RUN \  
wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.5/rabbitmq-
server_3.6.5-1_all.deb && \  
dpkg -i rabbitmq-server_3.6.5-1_all.deb  
  
RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_management  
  
ADD files/rabbitmq.config /etc/rabbitmq/  
  
RUN \  
chmod 0640 /etc/rabbitmq/rabbitmq.config && \  
chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.config  
  
EXPOSE 5672 15672  
ENTRYPOINT ["/usr/sbin/rabbitmq-server"]  

