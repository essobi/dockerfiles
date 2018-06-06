FROM jupyter/minimal-notebook  
  
MAINTAINER Peter Wojciechowski <pwojciechowski@conversantmedia.com>  
  
ENV APACHE_SPARK_VERSION 2.2.1  
ENV HADOOP_VERSION 2.6  
ENV SCALA_VERSION 2.11  
ENV SPARK_HOME /usr/local/spark  
ENV KAFKA_VERSION 1.1.0  
ENV CONFLUENT_VERSION 4.1.0  
USER root  
  
COPY files/custom/* /home/$NB_USER/.jupyter/custom/  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
vim \  
curl \  
openjdk-8-jre-headless && \  
rm -rf /var/lib/apt/lists* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir /cnvr && \  
fix-permissions /home/$NB_USER/.jupyter && \  
fix-permissions /cnvr  
  
# Apache Spark Install  
RUN wget
https://ftp.wayne.edu/apache/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz \  
\--directory-prefix=/cnvr && \  
tar -zxvf /cnvr/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
-C /usr/local \--owner root --group root --no-same-owner && \  
cd /usr/local && \  
ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark && \  
echo "spark.jars.packages org.apache.kafka:kafka-
clients:${KAFKA_VERSION},io.confluent:kafka-avro-
serializer:${CONFLUENT_VERSION},org.apache.kafka:kafka_${SCALA_VERSION}:${KAFKA_VERSION},org.apache.spark:spark-
streaming-
kafka-0-10_${SCALA_VERSION}:${APACHE_SPARK_VERSION},org.apache.spark:spark-
sql-kafka-0-10_${SCALA_VERSION}:${APACHE_SPARK_VERSION},com.databricks:spark-
avro_${SCALA_VERSION}:4.0.0" \  
>> ${SPARK_HOME}/conf/spark-defaults.conf && \  
rm -f /cnvr/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \  
fix-permissions ${SPARK_HOME}/conf && \  
fix-permissions ${SPARK_HOME}  
  
# Apache Toree install  
USER $NB_USER  
RUN wget
https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0/snapshots/dev1/toree-
pip/toree-0.2.0.dev1.tar.gz \  
\--directory-prefix=/cnvr && \  
pip install --no-cache-dir \  
/cnvr/toree-0.2.0.dev1.tar.gz && \  
jupyter toree install --sys-prefix \  
\--kernel_name="Spark ${APACHE_SPARK_VERSION}" \  
\--spark_home=${SPARK_HOME} && \  
pip install jupyter -U && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER && \  
rm /cnvr/toree-0.2.0.dev1.tar.gz  
  
# Install RISE Slideshow  
RUN conda install --quiet --yes \  
-c damianavila82 rise && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
# Bash Kernel install  
RUN pip install bash_kernel && \  
python -m bash_kernel.install  
  
RUN if [ ! -d /home/$NB_USER/.jupyter ] ; then mkdir /home/$NB_USER/.jupyter ;
fi && \  
echo ' { "NotebookApp": { "password":
"sha1:dd3eb2b05a48:360469c5f465835a06217785281598f0b3360e7d" } } ' >
/home/$NB_USER/.jupyter/jupyter_notebook_config.json  
  
RUN mkdir /cnvr/jupyter  
WORKDIR /cnvr/jupyter  
  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.6-src.zip  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info --repositories
http://packages.confluent.io/maven/  
  
# start.sh will make sure that Lab is running and will start the above to get
Notebook online  
ENTRYPOINT start.sh jupyter lab  
  
# Run as the jovyan user  
USER $NB_UID  
  

