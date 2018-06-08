FROM java:8-jdk  
  
MAINTAINER paladintyrion <paladintyrion@gmail.com>  
  
ENV SCALA_VERSION 2.11.11  
ENV SBT_VERSION 0.13.9  
ENV ZK_HOSTS=0.0.0.0:2181  
ENV KM_VERSION=1.3.3.14  
ENV KM_CONFIGFILE="conf/application.conf"  
ENV KM_USERNAME="paladin"  
ENV KM_PASSWORD="paladin"  
ENV KM_ARGS="-Dhttp.port=9449"  
RUN apt-get update -qq && \  
apt-get install -y wget curl unzip  
  
# Install scala  
RUN mkdir -p /opt && \  
curl -fsL
https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /opt  
ENV PATH=/opt/scala-${SCALA_VERSION}/bin:$PATH  
  
# Install sbt  
RUN curl -L -o /opt/sbt-$SBT_VERSION.deb
"https://dl.bintray.com/sbt/debian/sbt-${SBT_VERSION}.deb" && \  
dpkg -i /opt/sbt-${SBT_VERSION}.deb && \  
rm -f /opt/sbt-${SBT_VERSION}.deb && \  
apt-get update && \  
apt-get install sbt  
  
# Install kafka-manager  
RUN mkdir -p /tmp && \  
cd /tmp && \  
wget -q https://github.com/yahoo/kafka-manager/archive/${KM_VERSION}.tar.gz &&
\  
tar zxf ${KM_VERSION}.tar.gz && \  
cd /tmp/kafka-manager-${KM_VERSION} && \  
sbt clean dist && \  
unzip -d / ./target/universal/kafka-manager-${KM_VERSION}.zip && \  
rm -fr /tmp/* /root/.sbt /root/.ivy2 && \  
apt-get autoremove -y wget curl unzip sbt  
  
COPY start-kafka-manager.sh /kafka-manager-${KM_VERSION}/start-kafka-
manager.sh  
RUN chmod +x /kafka-manager-${KM_VERSION}/start-kafka-manager.sh  
  
WORKDIR /kafka-manager-${KM_VERSION}  
EXPOSE 9449  
ENTRYPOINT ["./start-kafka-manager.sh"]  

