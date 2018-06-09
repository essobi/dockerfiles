FROM reetawwsum/hadoop  
  
MAINTAINER Reet Awwsum <reetawwsum@yahoo.com>  
  
RUN curl http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz |
tar -xz -C /usr/local  
RUN ln -s /usr/local/spark-2.1.0-bin-hadoop2.7 /usr/local/spark  
  
ENV SPARK_HOME /usr/local/spark  
  
RUN mkdir $SPARK_HOME/yarn-remote-client  
ADD yarn-remote-client $SPARK_HOME/yarn-remote-client  
  
RUN mkdir $SPARK_HOME/local-jars  
ADD local-jars $SPARK_HOME/local-jars  
  
ADD log4j.properties $SPARK_HOME/conf/log4j.properties  
  
RUN $HADOOP_BOOTSTRAP && \  
hdfs dfsadmin -safemode leave && \  
hdfs dfs -put $SPARK_HOME/jars /spark  
  
ENV PATH $PATH:$SPARK_HOME/bin  
ENV LD_LIBRARY_PATH /usr/local/hadoop/lib/native/:$LD_LIBRARY_PATH  
  
ENV PYSPARK_PYTHON /usr/local/bin/python2.7  
ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH  
ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH  
  
RUN pip install -i https://pypi.anaconda.org/hyoon/simple toree  
RUN jupyter toree install  
  
ADD notebooks /usr/local/src/notebooks  
  
WORKDIR /usr/local/src/notebooks  
  
ADD bootstrap.sh /usr/local/src/bootstrap.sh  
RUN chown root:root /usr/local/src/bootstrap.sh  
RUN chmod 700 /usr/local/src/bootstrap.sh  
  
ENTRYPOINT ["/usr/local/src/bootstrap.sh"]  

