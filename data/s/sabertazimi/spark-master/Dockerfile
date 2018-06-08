FROM sabertazimi/spark-base-image:v2  
  
# MASTER  
COPY master.sh /  
  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV SPARK_MASTER_LOG /spark/logs  
  
EXPOSE 4040 8080 7077 6066 22  
CMD service ssh start && /bin/bash /master.sh  

