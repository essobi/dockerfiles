# Creates pseudo distributed hadoop 2.7.0 with pig 0.15 and hive 1.2.1  
FROM sequenceiq/hadoop-docker:2.7.0  
MAINTAINER mmast  
  
# hadoop-common fixes  
ENV PATH $PATH:$HADOOP_PREFIX/bin  
  
# pig  
RUN curl -s http://apache.mirror.anlx.net/pig/pig-0.15.0/pig-0.15.0.tar.gz |
tar -xz -C /usr/local  
ENV PIG_HOME /usr/local/pig-0.15.0/  
RUN ln -s $PIG_HOME /usr/local/pig  
ENV PATH $PATH:$PIG_HOME/bin  
  
# hive  
RUN curl -s http://apache.mirror.anlx.net/hive/hive-1.2.1/apache-
hive-1.2.1-bin.tar.gz | tar -xz -C /usr/local  
ENV HIVE_HOME /usr/local/apache-hive-1.2.1-bin/  
RUN ln -s $HIVE_HOME /usr/local/hive  
ENV PATH $PATH:$HIVE_HOME/bin

