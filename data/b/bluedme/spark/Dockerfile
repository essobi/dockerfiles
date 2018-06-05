FROM bluedme/oracle-java8:latest  
  
MAINTAINER bluedme  
  
RUN apt-get update && \  
apt-get install -y curl  
  
ENV SPARK_VERSION=1.6.0-bin-hadoop2.6  
# fetch & install spark  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_VERSION.tgz |
tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-$SPARK_VERSION spark  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $SPARK_HOME/bin:$PATH  
  
# default command.  
CMD ["bash"]  

