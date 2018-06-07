FROM java:8  
MAINTAINER Simeon H.K. Fitch <fitch@datamininglab.com>  
  
# Spark version numbers and associated variables  
ENV SPARK_VERSION 1.2.1  
ENV HADOOP_VERSION 2.4  
ENV SPARK_ARTIFACT spark-${SPARK_VERSION}  
ENV SPARK_BASENAME ${SPARK_ARTIFACT}-bin-hadoop${HADOOP_VERSION}  
ENV SPARK_HOME /usr/local/spark  
  
# Spark bundle path  
ENV SPARK_BUNDLE
http://www.gtlib.gatech.edu/pub/apache/spark/${SPARK_ARTIFACT}/${SPARK_BASENAME}.tgz  
  
# Unpack and setup bundle  
RUN curl -s ${SPARK_BUNDLE} | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ${SPARK_BASENAME} ${SPARK_HOME}  
  
# Setup launch script  
COPY bootstrap.sh /etc/bootstrap.sh  
RUN chown root.root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
EXPOSE 4040 7077 8080  
# Setup runtime environment  
ENV PATH $PATH:${SPARK_HOME}/bin  
  
RUN adduser --disabled-password --gecos '' spark  
USER spark  
WORKDIR /home/spark  
  
# Launch script to start up Spark  
ENTRYPOINT ["/etc/bootstrap.sh"]  
  
# Default argument to bootstrap.sh  
CMD ["-shell"]  

