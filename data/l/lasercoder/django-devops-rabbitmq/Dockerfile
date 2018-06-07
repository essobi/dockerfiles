FROM centos:7  
RUN yum -y update  
  
RUN yum -y install wget  
  
RUN wget https://www.rabbitmq.com/releases/erlang/erlang-18.2-1.el6.x86_64.rpm  
  
RUN yum -y install erlang-18.2-1.el6.x86_64.rpm  
  
RUN wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.9/rabbitmq-
server-3.6.9-1.el7.noarch.rpm  
  
RUN yum -y install rabbitmq-server-3.6.9-1.el7.noarch.rpm  
  
# RUN rabbitmq-plugins enable rabbitmq_management  
CMD /usr/sbin/rabbitmq-server -detached  
  
EXPOSE 15672  
EXPOSE 5672  

