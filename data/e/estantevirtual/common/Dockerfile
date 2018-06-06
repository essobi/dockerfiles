FROM jupyter/pyspark-notebook  
  
LABEL maintainer="EstanteVirtual <ti@estantevirtual.com.br>"  
  
USER root  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends sudo mysql-client && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "jovyan ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers  
  
ENV SPARK_JARS $SPARK_HOME/jars  
  
WORKDIR $SPARK_JARS  
  
ADD http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-
sdk-1.7.4.jar $SPARK_JARS/  
ADD http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.2/hadoop-
aws-2.7.2.jar $SPARK_JARS/  
ADD http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.45/mysql-
connector-java-5.1.45.jar $SPARK_JARS/  
ADD http://central.maven.org/maven2/org/elasticsearch/elasticsearch-
hadoop/6.0.0/elasticsearch-hadoop-6.0.0.jar $SPARK_JARS/  
ADD http://central.maven.org/maven2/joda-time/joda-time/2.9.9/joda-
time-2.9.9.jar $SPARK_JARS/  
  
RUN chmod 555 \  
aws-java-sdk-1.7.4.jar \  
hadoop-aws-2.7.2.jar \  
mysql-connector-java-5.1.45.jar \  
elasticsearch-hadoop-6.0.0.jar \  
joda-time-2.9.9.jar  
  
USER jovyan  
  
ENV APP_PATH /app/  
  
WORKDIR $APP_PATH  
  
RUN pip install python-dotenv==0.8.2 envparse==0.2.0 pprint==0.1 py4j==0.10.6
requests==2.18.4 pytest==3.4.2  
  
CMD bash -c "pip install -r requirements.txt && jupyter notebook"  

