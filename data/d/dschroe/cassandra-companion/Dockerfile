# Is The whole docker-pyThon-image necessary for cqlsh only?  
# Cqlsh can only be invoked wiTh version 2.7!  
FROM python:2.7-alpine  
  
RUN pip install cqlsh==5.0.3  
RUN apk add --no-cache bash  
  
COPY depends-on.sh .  
COPY run-db-schemas.sh .  
  
RUN chmod a+x depends-on.sh  
RUN chmod a+x run-db-schemas.sh  
  
CMD ./depends-on.sh $CASSANDRA_HOST $CASSANDRA_PORT && ./run-db-schemas.sh
$CASSANDRA_HOST $CASSANDRA_PORT $CQL_VERSION  

