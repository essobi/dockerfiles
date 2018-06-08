FROM dpatriot/docker-awscli-java8  
MAINTAINER Shago Vyacheslav <v.shago@corpwebgames.com>  
  
RUN \  
curl -s http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.4.tgz |
tar -xz -C /usr/local/ \  
&& cd /usr/local \  
&& ln -s spark-2.0.2-bin-hadoop2.4 spark  
  
RUN \  
curl -s http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.38/mysql-connector-java-5.1.38.jar -o /usr/local/spark/jars/mysql-
connector-java.jar \  
&& curl -s http://central.maven.org/maven2/org/apache/commons/commons-
csv/1.2/commons-csv-1.2.jar -o /usr/local/spark/jars/commons-csv-1.2.jar \  
&& curl -s https://s3.amazonaws.com/redshift-
downloads/drivers/RedshiftJDBC41-1.1.10.1010.jar -o
/usr/local/spark/jars/RedshiftJDBC41-1.1.10.1010.jar \  
&& curl -s http://central.maven.org/maven2/com/databricks/spark-
redshift_2.10/2.0.1/spark-redshift_2.10-2.0.1.jar -o
/usr/local/spark/jars/spark-redshift.jar \  
&& curl -s http://central.maven.org/maven2/com/amazonaws/aws-java-
sdk-s3/1.10.75.1/aws-java-sdk-s3-1.10.75.1.jar -o /usr/local/spark/jars/aws-
java-sdk-s3-1.10.75.1.jar \  
&& curl -s http://central.maven.org/maven2/com/databricks/spark-
avro_2.10/3.1.0/spark-avro_2.10-3.1.0.jar -o /usr/local/spark/jars/spark-
avro.jar \  
&& curl -s http://central.maven.org/maven2/com/eclipsesource/minimal-
json/minimal-json/0.9.4/minimal-json-0.9.4.jar -o
/usr/local/spark/jars/minimal-json.jar \  
&& curl -s http://central.maven.org/maven2/com/databricks/spark-
csv_2.10/1.5.0/spark-csv_2.10-1.5.0.jar -o /usr/local/spark/jars/spark-csv.jar
\  
&& curl -s
http://central.maven.org/maven2/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar
-o /usr/local/spark/jars/gson-2.2.4.jar \  
#&& curl -s http://central.maven.org/maven2/com/amazon/emr/emr-dynamodb-
hive/4.2.0/emr-dynamodb-hive-4.2.0.jar -o /usr/local/spark/jars/emr-dynamodb-
hive-4.2.0.jar \  
#&& curl -s http://central.maven.org/maven2/com/amazon/emr/emr-dynamodb-
hadoop/4.2.0/emr-dynamodb-hadoop-4.2.0.jar -o /usr/local/spark/jars/emr-
dynamodb-hadoop-4.2.0.jar \  
&& curl -s http://central.maven.org/maven2/com/amazonaws/aws-java-sdk-
dynamodb/1.10.75.1/aws-java-sdk-dynamodb-1.10.75.1.jar -o
/usr/local/spark/jars/aws-java-sdk-dynamodb-1.10.75.1.jar \  
&& curl -s http://central.maven.org/maven2/com/amazonaws/aws-java-sdk-
core/1.10.75.1/aws-java-sdk-core-1.10.75.1.jar -o /usr/local/spark/jars/aws-
java-sdk-core-1.10.75.1.jar  
  
ADD scripts/start-master.sh /start-master.sh  
ADD scripts/start-worker /start-worker.sh  
ADD scripts/spark-shell.sh /spark-shell.sh  
ADD scripts/spark-defaults.conf /usr/local/spark/conf/spark-defaults.conf  
ADD scripts/log4j.properties /usr/local/spark/conf/log4j.properties  
ADD scripts/remove_alias.sh /remove_alias.sh  
ADD scripts/docker-run-spark-env.sh /usr/local/bin/docker-run-spark-env.sh  
ADD scripts/script-runner.sh /usr/local/bin/script-runner.sh  
ADD scripts/sql-runner.sh /usr/local/bin/sql-runner.sh  
ADD lib/emr-ddb-hadoop.jar /usr/local/spark/jars/emr-ddb-hadoop.jar  
ADD lib/emr-ddb-hive.jar /usr/local/spark/jars/emr-ddb-hive.jar  
  
RUN apt-get update \  
&& apt-get install -y python-pandas \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install requests --upgrade  
  
RUN pip install elasticsearch zdesk boto3  
  
ENV SPARK_HOME /usr/local/spark  
  
ENV SPARK_DRIVER_CLASSPATH="/usr/local/spark/jars/mysql-connector-java.jar"  
ENV SPARK_JARS="/usr/local/spark/jars/spark-
avro.jar,/usr/local/spark/jars/spark-
redshift.jar,/usr/local/spark/jars/RedshiftJDBC41-1.1.10.1010.jar,/usr/local/spark/jars/minimal-
json.jar"  
ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_WORKER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV SPARK_WORKER_PORT 8888  
ENV SPARK_WORKER_WEBUI_PORT 8081  
ENV DRIVER_MEMORY 1G  
  
EXPOSE 8080 7077 8888 8081 4040 7001 7002 7003 7004 7005 7006  
ENTRYPOINT ["script-runner.sh"]  

