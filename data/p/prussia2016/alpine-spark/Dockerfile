FROM frolvlad/alpine-scala  
  
  
ENV SPARK_HOME /usr/local/spark  
  
  
ARG SPARK_VERSION=2.2.0  
ARG SPARK_BINARY_ARCHIVE_NAME=spark-${SPARK_VERSION}-bin-hadoop2.7  
ARG
SPARK_BINARY_DOWNLOAD_URL=http://d3kbcqa49mib13.cloudfront.net/${SPARK_BINARY_ARCHIVE_NAME}.tgz  
  
  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $JAVA_HOME/bin:$SCALA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH  
RUN apk add \--no-cache \--virtual=.build-dependencies wget ca-certificates &&
\  
apk add \--no-cache bash && \  
cd "/tmp" && \  
wget -qO - ${SPARK_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \  
cd /usr/local/ && \  
ln -s ${SPARK_BINARY_ARCHIVE_NAME} spark && \  
cp spark/conf/log4j.properties.template spark/conf/log4j.properties && \  
sed -i -e s/WARN/ERROR/g spark/conf/log4j.properties && \  
sed -i -e s/INFO/ERROR/g spark/conf/log4j.properties && \  
apk del .build-dependencies && \  
rm -rf "/tmp/"*  
  
USER root  
  
WORKDIR /root  
  
# Expose ports for monitoring.  
# SparkContext web UI on 4040 -- only available for the duration of the
application.  
# Spark master’s web UI on 8080.  
# Spark worker web UI on 8081.  
EXPOSE 4040 8080 8081  
  
  
CMD ["/bin/bash"]  

