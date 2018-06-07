FROM frolvlad/alpine-oraclejdk8:slim  
MAINTAINER lzaugg  
  
RUN apk add --update \  
curl bash ruby procps libstdc++ \  
&& rm /var/cache/apk/*  
  
ENV FLINK_VERSION 1.1.3_akka-2.4.12  
ENV FLINK_SCALA_VERSION scala_2.11  
ENV FLINK_CLASS_TO_RUN org.apache.flink.runtime.jobmanager.JobManager  
ENV FLINK_HOME /opt/flink  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV HADOOP_VERSION 2.7.3  
ENV HADOOP_URL
https://www.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz  
ENV HADOOP_CONF_DIR ${FLINK_HOME}/conf/hadoop  
  
# flink  
RUN mkdir -p /opt/  
  
RUN curl https://s3.eu-central-1.amazonaws.com/flink-
akka/flink-1.1.3_akka-2.4.12.tgz | tar -C /opt/ -xz | ln -s
/opt/flink-${FLINK_VERSION}/ ${FLINK_HOME}  
  
RUN curl $HADOOP_URL | tar -C /tmp -xz  
  
ADD conf/hadoop ${FLINK_HOME}/conf/hadoop  
ADD docker_flink-run.sh ${FLINK_HOME}/bin/  
ADD conf/log4j-docker.properties ${FLINK_HOME}/conf/  
ADD conf/logback-docker.xml ${FLINK_HOME}/conf/  
ADD conf/flink-conf.yaml ${FLINK_HOME}/conf/  
ADD docker_merge-yml-file.rb ${FLINK_HOME}/bin/  
ADD docker_merge-xml-with-yaml.rb ${FLINK_HOME}/bin/  
  
RUN mkdir -p /flink/log /flink/blob /flink/tmp /flink/state  
VOLUME [ "/flink/log", "/flink/blob", "/flink/tmp", "/flink/state"]  
  
# hadoop  
#RUN cp /tmp/hadoop-$HADOOP_VERSION/share/hadoop/tools/lib/{hadoop-aws-*,aws-
java-sdk-*,httpcore-*,httpclient-*} ${FLINK_HOME}/lib/  
RUN cp /tmp/hadoop-$HADOOP_VERSION/share/hadoop/tools/lib/hadoop-aws-*
${FLINK_HOME}/lib/ \  
&& cp /tmp/hadoop-$HADOOP_VERSION/share/hadoop/tools/lib/aws-java-sdk-*
${FLINK_HOME}/lib/ \  
&& cp /tmp/hadoop-$HADOOP_VERSION/share/hadoop/tools/lib/httpcore-*
${FLINK_HOME}/lib/ \  
&& cp /tmp/hadoop-$HADOOP_VERSION/share/hadoop/tools/lib/httpclient-*
${FLINK_HOME}/lib/ \  
&& rm -rf /tmp/hadoop-$HADOOP_VERSION  
  
USER root  
  
ENTRYPOINT [ "/opt/flink/bin/docker_flink-run.sh", "--configDir",
"/opt/flink/conf/"]  
  
CMD ["--executionMode", "cluster"]  
  
# 6123: jobmanager rpc  
# 6124: blobmanager  
# 6127: recovery  
# 8081: jobmanager web  
EXPOSE 6123 6124 6127 8081  

