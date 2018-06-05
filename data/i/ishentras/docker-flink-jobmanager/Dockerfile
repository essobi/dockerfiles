FROM alpine:3.3  
MAINTAINER lzaugg  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --update \  
curl openjdk8 bash ruby procps \  
&& rm /var/cache/apk/*  
  
ENV FLINK_VERSION 1.1.2_akka-2.4.9  
ENV FLINK_SCALA_VERSION scala_2.11  
ENV FLINK_CLASS_TO_RUN org.apache.flink.runtime.jobmanager.JobManager  
ENV FLINK_HOME /opt/flink  
  
RUN mkdir -m 777 -p /opt/  
  
RUN curl https://s3.eu-
central-1.amazonaws.com/flink-1.1.2-akka-2.4.9/flink-1.1.2_akka-2.4.9.tar.gz |
tar -C /opt/ -xz | ln -s /opt/flink-${FLINK_VERSION}/ ${FLINK_HOME}  
  
ADD docker_flink-run.sh ${FLINK_HOME}/bin/  
ADD conf/log4j-docker.properties ${FLINK_HOME}/conf/  
ADD conf/logback-docker.xml ${FLINK_HOME}/conf/  
ADD conf/flink-conf.yaml ${FLINK_HOME}/conf/  
ADD docker_merge-yml-file.rb ${FLINK_HOME}/bin/  
  
RUN chmod -R 777 ${FLINK_HOME}/conf/  
RUN mkdir -m 777 -p /flink/log /flink/blob /flink/tmp /flink/state  
VOLUME [ "/flink/log", "/flink/blob", "/flink/tmp", "/flink/state"]  
  
USER root  
  
ENTRYPOINT [ "/opt/flink/bin/docker_flink-run.sh", "--configDir",
"/opt/flink/conf/"]  
  
CMD ["--executionMode", "cluster"]  
  
# 6123: jobmanager rpc  
# 6124: blobmanager  
# 8081: jobmanager web  
EXPOSE 6123 6124 8081  

