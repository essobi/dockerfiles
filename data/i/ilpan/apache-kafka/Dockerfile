# Apache Kafka  
FROM ilpan/base-java  
MAINTAINER ilpan<pna.dev@outlook.com>  
  
ENV JENV_HOME /usr/local/.jenv  
ENV KAFKA_HOME $JENV_HOME/candidates/kafka  
  
ENV KAFKA_VERSION 1.0.1  
ENV SCALA_VERSION 2.11  
# install kafka  
RUN mkdir -p ${KAFKA_HOME} && cd $JENV_HOME/archives/ && \  
wget -c
https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
&& \  
tar -xzf kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz && mv
kafka_${SCALA_VERSION}-${KAFKA_VERSION} $KAFKA_HOME/${KAFKA_VERSION} && \  
bash -c "source ~/.jenv/bin/jenv-init.sh && jenv default kafka
${KAFKA_VERSION}" && \  
rm -rf $JENV_HOME/archives/*  
  

