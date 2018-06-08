# docker image to build Spark environment  
FROM mosaicoon/java-8-alpine-bash  
  
MAINTAINER Mosaicoon S.P.A.  
  
  
#Set Bootstrap  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
USER root  
  
#Set Versions  
#ENV SCALA_VERSION 2.11.7  
ENV SPARK_VERSION 1.6.1  
ENV HADOOP_VERSION 2.6  
ENV SBT_VERSION 0.13.11  
#############  
####MAVEN####  
#############  
ENV MAVEN_VERSION="3.3.9"  
ENV MAVEN_HOME=/usr/local/mvn  
  
RUN apk add --update wget && \  
cd /tmp && \  
wget "http://apache.panu.it/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz" && \  
tar -zxvf "apache-maven-$MAVEN_VERSION-bin.tar.gz" && \  
mv "apache-maven-$MAVEN_VERSION" "$MAVEN_HOME" && \  
ln -s "$MAVEN_HOME/bin/mvn" /usr/bin/mvn && \  
apk del wget && \  
rm /tmp/* /var/cache/apk/*  
  
#############  
####SPARK####  
#############  
#Set Spark Environment  
ENV SPARK_HOME /usr/local/spark-"${SPARK_VERSION}"-bin-
hadoop"${HADOOP_VERSION}"  
ENV PATH "${SPARK_HOME}"/bin:$PATH  
#ENV SPARK_MASTER_IP 0.0.0.0  
#ENV SPARK_LOCAL_IP 127.0.0.1  
#ENV SPARK_MASTER_PORT 7077  
#ENV SPARK_MASTER_WEBUI_PORT 8080  
#ENV SPARK_WORKER_WEBUI_PORT 8081  
#ENV SPARK_WORKER_CORES 2  
#ENV SPARK_WORKER_MEMORY 1g  
#ENV SPARK_DAEMON_MEMORY 3g  
ENV SPARK_PUBLIC_DNS 52.19.94.1  
#ENV SPARK_WORKER_INSTANCES  
WORKDIR /usr/local  
  
#Install Spark  
RUN wget
"http://mirrors.muzzy.it/apache/spark/spark-"${SPARK_VERSION}"/spark-"${SPARK_VERSION}"-bin-
hadoop"${HADOOP_VERSION}".tgz" && \  
tar -zxf spark-"${SPARK_VERSION}"-bin-hadoop"${HADOOP_VERSION}".tgz && rm
spark-"${SPARK_VERSION}"-bin-hadoop"${HADOOP_VERSION}".tgz  
RUN echo 'export PATH=$PATH:/usr/lib/spark/spark-"${SPARK_VERSION}"-bin-
hadoop"${HADOOP_VERSION}"' > /etc/profile.d/spark.sh && chmod 755
/etc/profile.d/spark.sh  
  
WORKDIR /  
  
EXPOSE "${SPARK_MASTER_WEBUI_PORT}" "${SPARK_MASTER_PORT}"
"${SPARK_WORKER_WEBUI_PORT}" 4040 6066  
CMD ["./etc/bootstrap.sh","-DFOREGROUND"]  
  

