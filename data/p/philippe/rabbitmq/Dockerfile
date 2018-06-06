FROM rabbitmq:3.6.9-management  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_consistent_hash_exchange  
  
ADD ./bin/ /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["rabbitmq-server"]

