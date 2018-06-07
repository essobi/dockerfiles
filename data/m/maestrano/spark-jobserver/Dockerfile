FROM velvia/spark-jobserver:0.6.2.mesos-0.28.1.spark-1.6.1  
ADD config/docker.conf /app/docker.conf  
  
ENTRYPOINT ["app/server_start.sh","--packages","org.apache.spark:spark-
core_2.10:1.6.1,org.apache.spark:spark-sql_2.10:1.6.1,org.mongodb.spark:mongo-
spark-connector_2.10:1.0.0"]  
  
EXPOSE 80  

