FROM jupyter/all-spark-notebook  
MAINTAINER Marco Capuccini, marco.capuccini@farmbio.uu.se  
  
USER root  
  
# Install Hadoop  
ADD bin/install-hadoop.sh tmp/install-hadoop.sh  
RUN tmp/install-hadoop.sh && rm -Rf tmp/  
  
# Set evnironment  
ENV HADOOP_HOME=/opt/hadoop/default  
ENV PATH=$PATH:$HADOOP_HOME/bin  
ENV PATH=$PATH:$HADOOP_HOME/sbin  
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME  
ENV HADOOP_COMMON_HOME=$HADOOP_HOME  
ENV HADOOP_HDFS_HOME=$HADOOP_HOME  
ENV YARN_HOME=$HADOOP_HOME  
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native  
ENV HADOOP_OPTS=-Djava.library.path=$HADOOP_HOME/lib  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64  
  
USER $NB_USER  

