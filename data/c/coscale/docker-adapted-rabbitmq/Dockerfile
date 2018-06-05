FROM rabbitmq:3.6  
RUN rabbitmq-plugins enable rabbitmq_management  
  
LABEL
com.coscale.monitoring='[{"PluginType":"RABBITMQ","Configuration":{"HOSTNAME":["localhost"],"PORT":["15672"],"USERNAME":["guest"],"PASSWORD":["guest"],"AMQP
PORT":["5672"],"QUEUE":["coscale"]}}]'  

