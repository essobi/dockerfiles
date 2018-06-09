#  
# Process Dockerfile  
#  
# Base image with spark pre-installed  
FROM falkonry/spark-base:j8.latest  
  
  
RUN apt-get update && apt-get install -y gfortran && apt-get install -y
libopenblas-base liblapack-dev  
  
# Expose port for Spark UI.  
EXPOSE 4040  
EXPOSE 8000  
RUN cd "$SPARK_HOME"/lib/ && \  
rm spark-assembly-1.6.0-hadoop2.6.0.jar && \  
curl -O https://storage.googleapis.com/spark-resources/spark-
assembly-1.6.0-hadoop2.6.0-hive-2.11.jar  
  
# Data volumes.  
VOLUME ["/var/lib/tercel"]  

