FROM centos:centos6  
  
MAINTAINER Dave Newton <dave.newton@vitals.com>  
  
ADD bin/rabbitmq-start /usr/local/bin/  
  
RUN rpm -Uvh \  
http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
&& \  
yum update -y && \  
yum install -y which wget tar tree erlang && \  
cd /opt && \  
wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.3.1/rabbitmq-
server-3.3.1-1.noarch.rpm && \  
yum install -y rabbitmq-server-3.3.1-1.noarch.rpm && \  
rabbitmq-plugins enable rabbitmq_management && \  
yum clean all && \  
echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config &&
\  
chmod +x /usr/local/bin/rabbitmq-start  
  
ENV RABBITMQ_LOG_BASE /data/log  
ENV RABBITMQ_MNESIA_BASE /data/mnesia  
  
VOLUME ["/data/log", "/data/mnesia"]  
  
WORKDIR /data  
  
CMD ["rabbitmq-start"]  
  
EXPOSE 5672  
EXPOSE 15672  

