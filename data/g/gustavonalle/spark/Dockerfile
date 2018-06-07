FROM alpine:3.7  
MAINTAINER gustavonalle  
  
RUN echo "LANG=en_GB.UTF-8" > /etc/locale.conf  
  
ENV SPARK_VERSION 2.3.0  
ENV SPARK_HADOOP_VERSION 2.7  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --update \  
curl openjdk8 openssh ruby bash cracklib-words supervisor procps \  
&& rm /var/cache/apk/*  
  
RUN curl
"http://mirror.vorboss.net/apache/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop$SPARK_HADOOP_VERSION.tgz" | tar -C /usr/local/ -xz | ln -s
/usr/local/spark-$SPARK_VERSION-bin-hadoop$SPARK_HADOOP_VERSION/
/usr/local/spark  
ADD start-spark.sh /usr/local/spark/  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV PATH ${JAVA_HOME}/bin:${PATH}  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN sed -i 's/nohup --/nohup/g' /usr/local/spark/sbin/spark-daemon.sh  
  
EXPOSE 5555 8080 7077 9080 9081 57600 7600 8181 9990 4040 55200 45700  
ENV LANG en_US.UTF-8  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

