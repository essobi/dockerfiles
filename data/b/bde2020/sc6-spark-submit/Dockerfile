FROM bde2020/spark-submit:2.1.0-hadoop2.7  
ENV ENABLE_INIT_DAEMON=false  
ENV SPARK_APPLICATION_PYTHON_LOCATION=  
ENV SPARK_MASTER_NAME=sc6-spark-master  
ENV SPARK_APPLICATION_ARGS=  
ENV SPARK_MASTER_URL=spark://sc6-spark-master:7077  
ENV SPARK_MASTER_PORT=7077  
ENV SPARK_APPLICATION_MAIN_CLASS=eu.bde.spark.job.sc6.App  
ENV SPARK_APPLICATION_JAR_LOCATION=/app/eu-bde-spark-job-sc6-1.0.0-jar-with-
dependencies.jar  
ENV SPARK_DURATION=10000  
ENV APP_NAME=sc6-csv-to-rdf  
ENV SPARK_HOME=/spark  
ENV KAFKA_METADATA_BROKER_LIST=sc6-kafka-1:9092  
ENV ZK_CONNECT=sc6_zoo_1:31202/kafka  
ENV KAFKA_TOPIC=sc6-flume-agent-001  
ENV KAFKA_GROUP_ID=sc6  
  
ENV VIRTUOSO_HOST=http://bde-virtuoso.poolparty.biz/sparql-graph-crud-auth  
ENV VIRTUOSO_DEFAULT_GRAPH=urn:sc6:test:from:aksw  
ENV VIRTUOSO_USER=dba  
ENV VIRTUOSO_PASS=XXXXXX  
  
#ENV DEBUG=true  
COPY eu-bde-spark-job-sc6-1.0.0-jar-with-dependencies.jar /app/  
  
COPY wait-for-step.sh /  
COPY execute-step.sh /  
COPY finish-step.sh /  
#COPY submit.sh /  
ADD startup.sh /  
  
RUN chmod +x /startup.sh  
  
CMD ["/bin/bash", "/startup.sh"]  

