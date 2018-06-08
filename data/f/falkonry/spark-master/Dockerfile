  
FROM docker.io/falkonry/spark-base:spark-2.2.0  
# Install a tool to be able to modify /etc/hosts file  
# Ref: https://github.com/hiteshjasani/nim-mungehosts  
ADD https://github.com/hiteshjasani/nim-
mungehosts/releases/download/v0.1.1/mungehosts /usr/local/bin/mungehosts  
RUN chmod 755 /usr/local/bin/mungehosts  
  
# Spark Master Port  
EXPOSE 7077  
# Spark Master Web UI Port  
EXPOSE 8080  
# Start up script  
COPY start.sh /start.sh  
  
# Configuration  
#ENV SPARK_MASTER_HOST  
ENTRYPOINT ["/start.sh"]  

