FROM java:8-jdk  
MAINTAINER docker@reecerobinson.co.nz  
  
ENV APACHE_SPARK_VERSION=1.6.0  
ENV JAVA_HOME=/usr  
  
RUN mkdir /usr/local/spark-src && \  
curl -s http://d3kbcqa49mib13.cloudfront.net/spark-$APACHE_SPARK_VERSION.tgz |
tar -xz -C /usr/local/spark-src  
  
RUN apt-get update && \  
apt-get install -y gdebi  
  
WORKDIR /usr/local/spark-src/spark-$APACHE_SPARK_VERSION  
  
RUN ./make-distribution.sh --name hadoop-2.6-hive --tgz -Phadoop-2.6 -Phive
-Phive-thriftserver -Pyarn  
  
WORKDIR /usr/local  
  
RUN tar -xzf /usr/local/spark-
src/spark-$APACHE_SPARK_VERSION/spark-$APACHE_SPARK_VERSION-bin-
hadoop-2.6-hive.tgz && \  
rm /usr/local/spark-src/spark-1.6.0/spark-$APACHE_SPARK_VERSION-bin-
hadoop-2.6-hive.tgz  
  
RUN mv /usr/local/spark-$APACHE_SPARK_VERSION-bin-hadoop-2.6-hive spark  
  
COPY log4j.properties /usr/local/spark/conf/log4j.properties  
  
ENV SPARK_HOME /usr/local/spark  
  
ENV PATH $PATH:$SPARK_HOME/bin  
  
RUN mkdir /apps  
RUN mkdir -p /user/hive  
RUN mkdir /applib  
VOLUME ["/apps","/user/hive"]  
EXPOSE 4040 10000  
# update boot script  
COPY bootstrap.sh /etc/bootstrap.sh  
RUN chown root.root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENTRYPOINT ["/etc/bootstrap.sh"]  

