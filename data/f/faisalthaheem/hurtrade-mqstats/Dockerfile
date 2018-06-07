#mqstats  
FROM openjdk:8  
ADD
https://github.com/faisalthaheem/hurtrade/releases/download/v1.0.0-alpha/mqstats-1.0-jar-
with-dependencies.jar /cs.hur/mqstats-1.0-jar-with-dependencies.jar  
CMD ["sh","-c","java -jar /cs.hur/mqstats-1.0-jar-with-dependencies.jar --mq-
host $MQ_HOST \--mq-username $MQ_USERNAME \--mq-password $MQ_PASSWORD \--mq-
rabbitmq-management-base-url $MQ_MGMT_BASE_URL"]  

