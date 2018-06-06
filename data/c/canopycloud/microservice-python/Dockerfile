FROM ubuntu  
MAINTAINER Will Mayger  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main
universe" >> /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc  
RUN apt-key add rabbitmq-signing-key-public.asc  
RUN apt-get -y install rabbitmq-server  
RUN rabbitmq-server& sleep 1 && rabbitmqctl status && rabbitmqctl add_user
test testpass1 && rabbitmqctl add_vhost vhost && rabbitmqctl set_permissions
-p vhost test ".*" ".*" ".*"  
RUN git clone https://github.com/CanopyCloud/microservice-python  
RUN pip install -r /microservice-python/requirements.txt  
EXPOSE 80  
WORKDIR /microservice-python/  
  
CMD python /microservice-python/server.py

