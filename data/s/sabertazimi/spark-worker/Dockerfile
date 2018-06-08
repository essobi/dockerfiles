FROM sabertazimi/spark-base-image:v2  
  
# WORKER  
COPY worker.sh /  
  
ENV SPARK_WORKER_WEBUI_PORT 8081  
ENV SPARK_WORKER_LOG /spark/logs  
ENV SPARK_MASTER "spark://spark-master:32769"  
EXPOSE 8081 22  
CMD service ssh start && /bin/bash /worker.sh  

