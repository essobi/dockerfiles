FROM kyunam/docker-ubuntu-java  
MAINTAINER Kyunam Kim <kyunam_kim@esri.com>  
  
# Install Apache Spark  
# Download Spark to /tmp  
ADD http://www.carfab.com/apachesoftware/spark/spark-1.5.2/spark-1.5.2-bin-
hadoop2.6.tgz /tmp/spark-1.5.2-bin-hadoop2.6.tgz  
# Unzip in the root folder  
RUN tar -xvf /tmp/spark-1.5.2-bin-hadoop2.6.tgz  
# Delete the downloaded file  
RUN rm -f /tmp/spark-1.5.2-bin-hadoop2.6.tgz  
# Set SPARK_HOME environment variable  
ENV SPARK_HOME /spark-1.5.2-bin-hadoop2.6  
# Include SPARK_HOME/bin in PATH - https://github.com/docker/docker/issues/684  
ENV PATH $SPARK_HOME/bin:$PATH  
  
CMD ["bash"]  

