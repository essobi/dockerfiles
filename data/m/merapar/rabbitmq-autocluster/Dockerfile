  
FROM rabbitmq:3.6.6-management-alpine  
MAINTAINER Merapar  
  
RUN apk --update add bash coreutils curl erlang erlang-asn1 erlang-crypto
erlang-eldap erlang-erts erlang-inets erlang-mnesia erlang-os-mon erlang-
public-key erlang-sasl erlang-ssl erlang-syntax-tools erlang-xmerl xz  
  
COPY rabbitmq-env.conf /etc/rabbitmq/rabbitmq-env.conf  
COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config  
  
RUN chmod 777 /etc/rabbitmq/rabbitmq-env.conf &&\  
chmod 777 /etc/rabbitmq/rabbitmq.config  
  
RUN rabbitmq-plugins enable rabbitmq_shovel rabbitmq_shovel_management
rabbitmq_web_stomp  
  
COPY start.sh /usr/local/bin/start.sh  
ENTRYPOINT start.sh  

