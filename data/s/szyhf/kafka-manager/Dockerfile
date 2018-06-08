FROM anapsix/alpine-java:jdk8  
# update by: https://github.com/sheepkiller/kafka-manager-docker/tree/alpine  
MAINTAINER Back Yu <yhfszb@gamil.com>  
  
ENV JAVA_MAJOR=8 \  
JAVA_UPDATE=77 \  
JAVA_BUILD=03  
ENV JAVA_HOME=/opt/jdk1.${JAVA_MAJOR}.0_${JAVA_UPDATE} \  
ZK_HOSTS=localhost:2181 \  
KM_VERSION=1.3.3.7 \  
KM_REVISION=05b2829653f7da15857ab03f3cbd669e4014333a \  
KM_CONFIGFILE="conf/application.conf"  
RUN apk add --no-cache git wget && \  
mkdir -p /tmp && \  
cd /tmp && \  
git clone https://github.com/yahoo/kafka-manager && \  
cd /tmp/kafka-manager && \  
git checkout ${KM_REVISION} && \  
echo 'scalacOptions ++= Seq("-Xmax-classfile-name", "200")' >> build.sbt && \  
./sbt clean dist && \  
unzip -d / ./target/universal/kafka-manager-${KM_VERSION}.zip && \  
rm -fr /tmp/* /root/.sbt /root/.ivy2 && \  
printf '#!/bin/sh\nexec ./bin/kafka-manager -Dconfig.file=${KM_CONFIGFILE}
"${KM_ARGS}" "${@}"\n' > /kafka-manager-${KM_VERSION}/km.sh && \  
chmod +x /kafka-manager-${KM_VERSION}/km.sh && \  
rm -fr /kafka-manager-${KM_VERSION}/share \  
apk del git  
  
WORKDIR /kafka-manager-${KM_VERSION}  
  
EXPOSE 9000  
ENTRYPOINT ["./km.sh"]

