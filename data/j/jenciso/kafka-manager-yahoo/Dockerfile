FROM hseeberger/scala-sbt  
  
MAINTAINER Juan Enciso <juan.enciso@gmail.com>  
  
ENV ZK_HOSTS=localhost:2181 \  
KM_VERSION=1.3.3.14  
RUN mkdir -p /tmp && \  
cd /tmp && \  
wget https://github.com/yahoo/kafka-manager/archive/${KM_VERSION}.tar.gz && \  
tar xxf ${KM_VERSION}.tar.gz && \  
cd /tmp/kafka-manager-${KM_VERSION} && \  
sbt clean dist && \  
unzip -d / ./target/universal/kafka-manager-${KM_VERSION}.zip && \  
rm -fr /tmp/${KM_VERSION} /tmp/kafka-manager-${KM_VERSION}  
  
WORKDIR /kafka-manager-${KM_VERSION}  
  
EXPOSE 9000  
ENTRYPOINT ["./bin/kafka-manager","-Dconfig.file=conf/application.conf"]  

