FROM thumperj/oss-base  
ADD sensu.repo /etc/yum.repos.d/sensu.repo  
  
RUN yum -y update; yum clean all; \  
yum -y install wget && \  
wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-
server-3.6.1-1.noarch.rpm && \  
wget
https://www.rabbitmq.com/releases/erlang/erlang-18.3-1.el7.centos.x86_64.rpm
&& \  
rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc; \  
yum -y install \  
logrotate \  
erlang-18.3-1.el7.centos.x86_64.rpm \  
rabbitmq-server-3.6.1-1.noarch.rpm \  
redis \  
python \  
sensu \  
uchiwa \  
nginx \  
python-pip; yum clean all  
  
ENV RABBITMQ_LOG_BASE=/data/log RABBITMQ_MNESIA_BASE=/data/mnesia  
  
VOLUME ["/data/log", "/data/mnesia"]  
  
RUN mkdir -p /var/run/sensu-server  
RUN chown sensu:sensu /var/run/sensu-server  
RUN pip install pika  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisor.conf  
  
EXPOSE 80 443 3000 4567 5671 5672 6379 15672  

