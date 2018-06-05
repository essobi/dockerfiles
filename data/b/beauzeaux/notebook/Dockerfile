FROM ipython/notebook  
MAINTAINER Nick Beaulieu, beauzeaux@outlook.com  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
openjdk-7-jre-headless \  
wget \  
python-pip \  
&& \  
mkdir -p /opt/spark && \  
cd /opt/spark && \  
wget -q http://d3kbcqa49mib13.cloudfront.net/spark-1.3.0-bin-hadoop2.4.tgz \  
-O - | tar -xz --strip-components=1 && \  
mkdir -p /opt/spark/lib_managed/ && \  
wget -q https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-latest-
hadoop2.jar -O /opt/spark/lib_managed/gcs-connector.jar  
  
RUN pip install \  
j2cli  
  
COPY ./setup /opt/setup/  
RUN chmod +x /opt/setup/startup.sh  
ENTRYPOINT ["/opt/setup/startup.sh"]  
  
# set spark paths  
ENV PYTHONPATH
$PYTHONPATH:/opt/spark/python/lib/py4j-0.8.2.1-src.zip:/opt/spark/python  
ENV SPARK_HOME /opt/spark/  
ENV SPARK_CLASSPATH $SPARK_CLASSPATH:/opt/spark/lib_managed/gcs-connector.jar  
  
# override these if using Google cloud storage/ compute engine  
ENV GCS_BUCKET_ID BUCKETNAME  
ENV GCE_PROJECT_ID PROJECTID  

