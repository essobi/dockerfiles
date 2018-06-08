FROM ubuntu  
MAINTAINER obed.n.munoz@gmail.com  
  
RUN apt-get update -y  
RUN apt-get install -y rabbitmq-server  
RUN service rabbitmq-server start && rabbitmqctl add_user openstack secure  
RUN service rabbitmq-server start && rabbitmqctl set_permissions openstack
".*" ".*" ".*"  
  
EXPOSE 5672  
CMD ["rabbitmq-server"]  

