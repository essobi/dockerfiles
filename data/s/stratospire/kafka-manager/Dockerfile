FROM java:openjdk-8-jdk  
  
MAINTAINER Ryan C Koch <ryanckoch@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ZK_HOSTS=localhost:2181 \  
KM_VERSION=1.3.3.14 \  
KM_CONFIGFILE="conf/application.conf"  
RUN curl -L https://github.com/yahoo/kafka-manager/archive/$KM_VERSION.tar.gz
-o /tmp/kafka-manager.tar.gz && \  
tar -xvzf /tmp/kafka-manager.tar.gz -C /tmp && \  
mv /tmp/kafka-manager-$KM_VERSION /tmp/kafka-manager && \  
cd /tmp/kafka-manager && \  
echo 'scalacOptions ++= Seq("-Xmax-classfile-name", "200")' >> build.sbt && \  
./sbt clean dist && \  
mkdir -p /opt && \  
unzip -d /opt ./target/universal/kafka-manager-${KM_VERSION}.zip && \  
mv /opt/kafka-manager-$KM_VERSION /opt/kafka-manager && \  
rm -fr /tmp/* /root/.sbt /root/.ivy2 && \  
printf '#!/bin/sh\nexec ./bin/kafka-manager -Dconfig.file=${KM_CONFIGFILE}
"${KM_ARGS}" "${@}"\n' > /opt/kafka-manager/km.sh && \  
chmod +x /opt/kafka-manager/km.sh  
  
WORKDIR /opt/kafka-manager  
  
EXPOSE 9000  
ENTRYPOINT ["./km.sh"]  

