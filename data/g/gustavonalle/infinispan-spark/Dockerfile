FROM fedora:20  
MAINTAINER gustavonalle  
  
ENV INFINISPAN_VERSION 8.0.0.Final  
ENV SPARK_VERSION 1.4.0  
ENV SPARK_HADOOP_VERSION 2.6  
RUN (yum -y install words tar unzip supervisor java-1.8.0-openjdk-devel; \  
yum -y autoremove; \  
yum -y clean all;)  
  
RUN curl
"http://mirror.vorboss.net/apache/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop$SPARK_HADOOP_VERSION.tgz" | tar -C /usr/local/ -xz | ln -s
/usr/local/spark-$SPARK_VERSION-bin-hadoop$SPARK_HADOOP_VERSION/
/usr/local/spark  
ADD start-spark.sh /usr/local/spark/  
  
RUN curl "https://repo1.maven.org/maven2/org/infinispan/server/infinispan-
server-build/$INFINISPAN_VERSION/infinispan-server-
build-$INFINISPAN_VERSION.zip" > /server.zip && unzip /server.zip -d
/usr/local && rm /server.zip && ln -s /usr/local/infinispan-server-*
/usr/local/infinispan-server  
RUN sed -i 's/-Xmx512/-Xmx4096/g' /usr/local/infinispan-
server/bin/standalone.conf  
ADD start-infinispan.sh /usr/local/infinispan-server/bin/  
  
ADD java_home.sh /etc/profile.d/java_home.sh  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 5555 8080 7077 9080 9081 57600 7600 8181 9990 11211 11222 4040 55200
45700  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

