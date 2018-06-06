# DOCKER-VERSION 1.5  
FROM rabbitmq:management  
  
MAINTAINER Elmar Athmer <elmar@athmer.org>  
  
# consistent hashing is required for the application  
RUN rabbitmq-plugins enable \--offline rabbitmq_consistent_hash_exchange  

