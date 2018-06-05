#Spark base image  
FROM ubuntu  
  
RUN apt-get update && apt-get install -y \  
wget \  
default-jdk \  
python-pip \  
scala && cd / && mkdir spark && cd /spark && \  
wget https://www.apache.org/dist/spark/spark-1.6.3/spark-1.6.3-bin-
hadoop2.6.tgz && \  
tar -xvf spark-1.6.3-bin-hadoop2.6.tgz && \  
cd / && mkdir hadoop && cd /hadoop && \  
wget
https://www.apache.org/dist/hadoop/common/hadoop-2.9.0/hadoop-2.9.0.tar.gz &&
\  
tar -xvf hadoop-2.9.0.tar.gz  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64  
ENV SPARK_HOME /spark/spark-1.6.3-bin-hadoop2.6  
ENV HADOOP_HOME /hadoop/hadoop-2.9.0  
ENV PYSPARK_PYTHON python  
ENV PATH $PATH:$SPARK_HOME/bin  
ENV PATH $PATH:$HADOOP_HOME/bin  
ENV MESOSCLUSTER 158.42.104.137  
ENV MESOSPORT 5050  
ENV HDFSINTERNAL 10.0.0.21  
ENV HDFSPORT 9000  
ENV EXECUTOR_MEMORY 512M  
ENV EXECUTOR_CORES 4  
RUN pip install --upgrade pip && \  
pip install flask && \  
pip install flask-restful && \  
pip install requests && \  
pip install snakebite  
  
COPY ./core-site.xml /hadoop/hadoop-2.9.0/etc/hadoop  
COPY ./hdfs-site.xml /hadoop/hadoop-2.9.0/etc/hadoop  
COPY ./dqrest /dqrest  
COPY ./spark-py /bigSEA  
ENV FLASK_APP /dqrest/app.py  
  
RUN mkdir /db  
RUN touch /db/profiling_log.db  
  

