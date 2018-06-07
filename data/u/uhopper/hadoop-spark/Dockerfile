FROM uhopper/hadoop:2.8.1  
ENV SPARK_VERSION 2.1.2  
ENV SPARK_BIN_URL
https://www.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-without-hadoop.tgz  
  
ENV SPARK_HOME=/opt/spark-$SPARK_VERSION  
  
RUN set -x \  
&& curl -fSL "$SPARK_BIN_URL" -o /tmp/spark.tar.gz \  
&& tar -xvf /tmp/spark.tar.gz -C /opt \  
&& mv /opt/spark-$SPARK_VERSION-* $SPARK_HOME \  
&& rm -f /tmp/spark.tar.gz  
  
WORKDIR $SPARK_HOME  
ENV PATH $SPARK_HOME/bin:$PATH  
  
ADD spark-entrypoint.sh /  
ADD spark-historyserver.sh /  
ADD spark-master.sh /  
ADD spark-slave.sh /  
  
RUN chmod a+x \  
/spark-entrypoint.sh \  
/spark-historyserver.sh \  
/spark-master.sh \  
/spark-slave.sh  
  
RUN echo "export SPARK_DIST_CLASSPATH=$(hadoop classpath)" >>
/opt/spark-$SPARK_VERSION/conf/spark-env.sh  
  
ENTRYPOINT ["/spark-entrypoint.sh"]  

