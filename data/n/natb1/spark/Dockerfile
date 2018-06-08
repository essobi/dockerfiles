FROM smizy/hadoop-base:2.7.3-alpine as hadoop-base  
  
FROM alpine:3.6 as spark  
  
RUN apk add --no-cache curl tar bash openjdk8 python3  
RUN curl -O https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-
hadoop2.7.tgz  
RUN tar -xzf spark-2.2.0-bin-hadoop2.7.tgz  
COPY --from=hadoop-base /usr/local/hadoop-2.7/lib/native
/usr/local/hadoop-2.7/lib/native  
  
ENV LD_LIBRARY_PATH=/usr/local/hadoop-2.7/lib/native/:$LD_LIBRARY_PATH  
ENV SPARK_HOME $PWD/spark-2.2.0-bin-hadoop2.7  
ENV PYSPARK_PYTHON=python3  
ENV
PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH  
  
WORKDIR $SPARK_HOME  

