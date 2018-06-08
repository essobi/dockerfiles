FROM alpine  
  
MAINTAINER Nicolas Lorin <androw95220@gmail.com>  
  
RUN apk add --update openjdk8-jre curl bash procps && rm -rf /var/cache/apk/*  
  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz
| tar -xz -C /usr/local/ && cd /usr/local && ln -s spark-2.1.1-bin-hadoop2.7
spark  
  
ADD scripts/*.sh /  
ADD scripts/spark-defaults.conf /spark-defaults.conf  
  
ENV SPARK_HOME=/usr/local/spark SPARK_MASTER_PORT=7077
SPARK_MASTER_WEBUI_PORT=8080 SPARK_WORKER_PORT=8888
SPARK_WORKER_WEBUI_PORT=8081  
ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_WORKER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
EXPOSE 8080 7077 8888 8081 4040 7001 7002 7003 7004 7005 7006  
CMD ["/usr/local/spark/bin/spark-shell"]  

