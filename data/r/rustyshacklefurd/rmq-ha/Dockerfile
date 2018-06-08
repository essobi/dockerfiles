FROM rabbitmq  
RUN apt-get -qq update && apt-get install curl -y  
  
RUN curl -sL -o /tmp/rabbitmq-autocluster-0.8.0.ez \  
https://github.com/rabbitmq/rabbitmq-
autocluster/releases/download/0.8.0/autocluster-0.8.0.ez  
  
RUN mv /tmp/rabbitmq-autocluster-0.8.0.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.11/plugins  
  
RUN curl -sL -o /tmp/rabbitmq_aws-0.8.0.ez \  
https://github.com/rabbitmq/rabbitmq-
autocluster/releases/download/0.8.0/rabbitmq_aws-0.8.0.ez  
  
RUN mv /tmp/rabbitmq_aws-0.8.0.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.11/plugins  
  
RUN rabbitmq-plugins enable --offline \  
rabbitmq_management \  
autocluster \  
rabbitmq_aws  
  
RUN apt-get remove --purge curl -y && rm -rf /var/lib/apt/lists/*  
  
COPY ha-setup.sh ./  
  
RUN chmod +x ha-setup  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 4369 5671 5672 15671 15672 25672  
  
CMD ["rabbitmq-server"]  

