FROM openjdk:8  
ADD
https://github.com/faisalthaheem/hurtrade/releases/download/v1.0.0-alpha/webauth-1.0-jar-
with-dependencies.jar /cs.hur/webauth-1.0-jar-with-dependencies.jar  
CMD ["sh","-c","java -jar /cs.hur/webauth-1.0-jar-with-dependencies.jar
--redis-server $REDIS_SERVER \--mq-host $MQ_HOST \--mq-username $MQ_USERNAME
\--mq-password $MQ_PASSWORD \--db-host $DB_HOST \--db-username $DB_USERNAME
\--db-password $DB_PASSWORD"]  
  

