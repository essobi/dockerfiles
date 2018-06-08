# Spark  
FROM martinz/spark-base:latest  
  
# Expose TCP ports 7077 8080  
EXPOSE 7077 8080 8888 8081  
ENV SPARK_WORKER_PORT 8888  
ADD files /root/spark_singlenode_files  
  
RUN chown root.root /root/spark_singlenode_files/default_cmd  
RUN chmod 700 /root/spark_singlenode_files/default_cmd

