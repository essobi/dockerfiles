FROM java:8  
  
RUN apt-get update && apt-get -y install curl && rm -fr /var/lib/apt/lists/*  
  
ENV SPARK_RELEASE=spark-1.3.0-bin-hadoop2.4  
  
RUN curl --silent http://d3kbcqa49mib13.cloudfront.net/$SPARK_RELEASE.tgz |
gunzip | tar x -C / && \  
mv /$SPARK_RELEASE /spark && \  
cd /spark/lib && \  
curl --silent -O https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-
latest-hadoop2.jar && \  
echo export SPARK_CLASSPATH=$SPARK_CLASSPATH:/spark/lib/gcs-connector-latest-
hadoop2.jar > /spark/conf/spark-env.sh  
  
ADD core-site.xml /spark/conf/  
  
WORKDIR /spark  

