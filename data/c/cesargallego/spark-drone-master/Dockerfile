FROM ubuntu:16.10  
MAINTAINER BBVA-LABS  
  
# software versions  
ENV ALLUXIO_VERSION=1.4.0 \  
SPARK_VERSION=2.1.0 \  
HADOOP_VERSION=2.7 \  
WORK_PATH="/usr/local"  
# Install requriments and the main packages  
RUN apt-get update \  
&& apt-get install -y sudo vim nano curl openjdk-8-jdk scala python3.6
python3.6-dev curl gcc \  
&& curl https://bootstrap.pypa.io/get-pip.py | python3.6 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -fSL http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz -o spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz \  
&& tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \  
&& mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${WORK_PATH}/spark \  
&& rm -rf alluxio-${ALLUXIO_VERSION}*  
  
RUN curl -fSL
http://downloads.alluxio.org/downloads/files/${ALLUXIO_VERSION}/alluxio-${ALLUXIO_VERSION}-spark-
client-jar-with-dependencies.jar -o alluxio-${ALLUXIO_VERSION}-spark-client-
jar-with-dependencies.jar \  
&& mv alluxio-${ALLUXIO_VERSION}-spark-client-jar-with-dependencies.jar
${WORK_PATH}/spark/  
  
ADD data /  
RUN pip3 install -r /bootstrap/requirements.txt  
  
RUN chown root:root /bootstrap/*.sh && chmod a+x /bootstrap/*.sh  
  
ENTRYPOINT ["/bootstrap/bootstrap.sh"]  

