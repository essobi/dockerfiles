FROM guyk/erlang  
MAINTAINER Guy Klainer "guyk@dauup.com"  
ENV container docker  
  
# install rabbit  
RUN wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.4.2/rabbitmq-
server-3.4.2-1.noarch.rpm  
RUN rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc  
RUN yum -y install rabbitmq-server-3.4.2-1.noarch.rpm  
  
#config rabbit  
RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_management  
RUN echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config  
  
EXPOSE 5672 15672 4369  
CMD /usr/sbin/rabbitmq-server  
# ENTRYPOINT ["/usr/sbin/rabbitmq-server"]  

