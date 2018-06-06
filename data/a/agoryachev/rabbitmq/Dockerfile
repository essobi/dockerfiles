FROM rabbitmq:3.6.9-management  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_federation
rabbitmq_federation_management rabbitmq_consistent_hash_exchange
rabbitmq_shovel rabbitmq_shovel_management  
RUN apt-get update && apt-get -y install curl

