FROM alpine:3.7  
LABEL maintainer="walter AT dcc DOT ufmg DOT br"  
  
ENV SPARK_VERSION 2.3.0  
ENV SPARK_HADOOP_VERSION 2.7  
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf && \  
echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --update \  
curl openjdk8-jre-base openssh ruby bash cracklib-words supervisor procps \  
&& rm /var/cache/apk/*  
RUN curl
"http://ftp.unicamp.br/pub/apache/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop$SPARK_HADOOP_VERSION.tgz" | \  
tar -C /usr/local/ -xz | ln -s /usr/local/spark-$SPARK_VERSION-bin-
hadoop$SPARK_HADOOP_VERSION/ /usr/local/spark  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV PATH ${JAVA_HOME}/bin:${PATH}  
ENV LANG en_US.UTF-8  
CMD ["/bin/bash"]  

