FROM rabbitmq:3-management  
  
RUN rabbitmq-plugins enable \--offline \  
rabbitmq_federation \  
rabbitmq_federation_management \  
rabbitmq_shovel \  
rabbitmq_shovel_management \  
rabbitmq_mqtt  
  
RUN apt-get update  
RUN apt-get install -y build-essential zip wget git python xsltproc erlang-dev
erlang-src  
  
RUN mkdir /rabbitmq  
WORKDIR /rabbitmq  
  
RUN git clone https://github.com/rabbitmq/rabbitmq-public-umbrella.git  
WORKDIR /rabbitmq/rabbitmq-public-umbrella  
  
RUN git clone https://github.com/rabbitmq/rabbitmq-server.git  
RUN git clone https://github.com/rabbitmq/rabbitmq-erlang-client.git  
RUN git clone https://github.com/rabbitmq/rabbitmq-codegen.git  
RUN git clone https://github.com/rabbitmq/rabbitmq-auth-mechanism-ssl  
  
ADD . /rabbitmq//rabbitmq-public-umbrella/udp-exchange  
WORKDIR /rabbitmq//rabbitmq-public-umbrella/udp-exchange  
  
RUN make  
  
RUN cp -r build/app/rabbit_udp_exchange-0.0.0
/usr/lib/rabbitmq/lib/rabbitmq_server-*/plugins  
RUN rabbitmq-plugins enable \--offline rabbit_udp_exchange  
  
EXPOSE 5672 15672 25672  

